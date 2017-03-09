#importing some libraries
%matplotlib inline

import numpy as np
import pandas as pd
import dicom
import os
import scipy.ndimage
import matplotlib.pyplot as plt

from skimage import measure, morphology
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

INPUT_FOLDER = '../Projects/LungCancer/PatientData/sample_images'
patients = os.listdir(INPUT_FOLDER)
patients.sort()

#load scans in given folder path to INPUT_FOLDER
def load_scan(path):
    slices = [dicom.read_file(path + '/' + s) for s in oslistdir(path)]
    slices.sort(key = lambda x: float(x.ImagePositionPatient[2]))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness

        return slices


