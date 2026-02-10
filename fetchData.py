import kaggle


kaggle.api.authenticate()

kaggle.api.dataset_download_files('xdxd003/ff-c23',path='.',unzip=True)