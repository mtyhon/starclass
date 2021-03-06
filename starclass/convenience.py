#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Training set convenience functions.

.. codeauthor:: Rasmus Handberg <rasmush@phys.au.dk>
"""

import os
from . import training_sets as tsets
from . import RFGCClassifier, SLOSHClassifier, XGBClassifier, SortingHatClassifier, MetaClassifier

#--------------------------------------------------------------------------------------------------
def get_classifier(classifier_key):
	"""
	Get class for given classifier key.

	Parameters:
		classifier_key (str): Classifier keyword. Choices can be found in :func:`classifier_list`.

	Returns:
		:class:`BaseClassifier`: Class for the classifier.

	.. codeauthor:: Rasmus Handberg <rasmush@phys.au.dk>
	"""
	ClassificationClass = {
		'rfgc': RFGCClassifier,
		'slosh': SLOSHClassifier,
		#'foptics': FOPTICSClassifier,
		'xgb': XGBClassifier,
		'sortinghat': SortingHatClassifier,
		'meta': MetaClassifier
	}.get(classifier_key, None)

	if ClassificationClass is None:
		raise ValueError("Invalid classifier key specified")

	return ClassificationClass

#--------------------------------------------------------------------------------------------------
def get_trainingset(tset_key):
	"""
	Get training set class for given training set key.

	Parameters:
		tset_key (str): Training set keyword. Choices can be found in :func:`trainingset_list`.

	Returns:
		:class:`TrainingSet`: Class for the training set.

	.. codeauthor:: Rasmus Handberg <rasmush@phys.au.dk>
	"""
	TsetClass = {
		'keplerq9v2': tsets.keplerq9v2,
		'keplerq9': tsets.keplerq9,
		'keplerq9-linfit': tsets.keplerq9linfit,
		'tdasim': tsets.tdasim,
		'tdasim-raw': tsets.tdasim_raw,
		'tdasim-clean': tsets.tdasim_clean
	}.get(tset_key, None)

	if TsetClass is None:
		raise ValueError("Invalid training set key specified")

	return TsetClass

#--------------------------------------------------------------------------------------------------
def trainingset_available(tset_key):

	# Point this to the directory where the training sets are stored
	INPUT_DIR = os.environ.get('STARCLASS_TSETS')
	if INPUT_DIR is None:
		INPUT_DIR = os.path.join(os.path.dirname(__file__), 'training_sets', 'data')
	elif not os.path.isdir(INPUT_DIR):
		raise IOError("The environment variable STARCLASS_TSETS is set, but points to a non-existent directory.")

	# Use the other function to ensure that tset_key is correct:
	get_trainingset(tset_key)

	return os.path.isfile(os.path.join(INPUT_DIR, tset_key, 'todo.sqlite'))
