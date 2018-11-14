#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:58:47 2018
this script is for Visualization of nii file(MRI)
@author: liujing
"""
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
'''
img1 = nib.load('./data/ADNI/AD/wwmAD_002_S_0619_118678.nii')
img_arr1 = img1.get_data()
plt.imshow(img_arr1[50])
plt.show()

img2 = nib.load('./data/ADNI/MCI/wwmMCI_002_S_0729_78654.nii')
img_arr2 =img2.get_data()
plt.imshow(img_arr2[50])
plt.show()

img3 = nib.load('./data/ADNI/normal/wwmNL_002_S_0295_118692.nii')
img_arr3 =img3.get_data()
plt.imshow(img_arr3[50])
plt.show()

img4 = nib.load('./data/301/AD/w3_AD001.nii')
img_arr4 =img4.get_data()
plt.imshow(img_arr4[50])
plt.show()

img5 = nib.load('./data/301/AD/w3_AD001_mpr.nii')
img_arr5 =img5.get_data()
plt.imshow(img_arr5[50])
plt.show()

img6 = nib.load('./data/301/normal/w1_NC002.nii')
img_arr6 =img6.get_data()
plt.imshow(img_arr6[50])
plt.show()

img7 = nib.load('./data/301/normal/w1_NC002_mpr.nii')
img_arr7 =img7.get_data()
plt.imshow(img_arr7[50])
plt.show()
'''
img8 = np.load('./data/train/AD/wwmAD_002_S_0619_48617.nii_conv.npy')
plt.imshow(img8[0,:,:,1,1])
plt.show()