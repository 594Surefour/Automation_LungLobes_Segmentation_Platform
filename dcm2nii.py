import SimpleITK as sitk

file_path = './dcm' #dicom存放文件夹
series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(file_path)
series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(file_path)

series_reader = sitk.ImageSeriesReader()
series_reader.SetFileNames(series_file_names)

image3D = series_reader.Execute()
sitk.WriteImage(image3D, './seg/img.nii')