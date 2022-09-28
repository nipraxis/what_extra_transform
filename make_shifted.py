""" Make shifted volume for exercise
"""

import scipy.ndimage as snd

import nibabel as nib

from nipraxis import fetch_file

func_path = fetch_file('ds108_sub001_t1r1.nii')
img = nib.load(func_path)
data = img.get_fdata()

unshifted_vol = data[..., 9]

nib.save(nib.Nifti1Image(unshifted_vol, None, img.header),
         'unshifted_vol.nii')

shifted_vol = snd.shift(unshifted_vol, [-3, 5, 2])

nib.save(nib.Nifti1Image(shifted_vol, None, img.header),
         'shifted_vol.nii')
