# EMLO Assignment 1
----------------------
## Name : Abhijit Mali
----------------------
## Notes 
---------------------------------------------------------------------------------------------------------------------------
1. Used Resnet 18 model for training.
2. Saved per epoch training and test loss and accuracy along with class level accuracy in [metrics.csv](https://github.com/csharpshooter/EMLO/blob/main/A1/metrics.csv)
3. For first 1000 images commit metrics stored [metricsv1.csv](https://github.com/csharpshooter/EMLO/blob/main/A1/metricsv1.csv) and for the second 2000 images metrics stored in [metrics.csv](https://github.com/csharpshooter/EMLO/blob/main/A1/metrics.csv)
4. Wrote following 7 test cases in [test.py](https://github.com/csharpshooter/EMLO/blob/main/A1/test.py). Used pytest for writing unit tests.
   - test_check_if_model_file_present_in_root_folder
   - test_check_if_data_folder_present_in_root_folder
   - test_check_if_metrics_csv_present_in_root_folder
   - test_validate_train_accuracy_greater_than_70_pct
   - test_validate_test_accuracy_greater_than_70_pct
   - test_validate_dog_class_accuracy_greater_than_70_pct
   - test_validate_cat_class_accuracy_greater_than_70_pct
5. [![Tests Status](https://github.com/csharpshooter/EMLO/actions/workflows/python-app.yml/badge.svg)](https://github.com/csharpshooter/EMLO/actions/workflows/python-app.yml)
6. First model 1000 images train test loss and accuracy:
   - Train Accuracy: 98.1
   - Test Accuracy: 93.5
   - Cats Accuracy: 94.5
   - Dogs Accuracy: 92.5
7. Second model 2000 images train test loss and accuracy:
   - Train Accuracy: 98.1
   - Test Accuracy: 93.5
   - Cats Accuracy: 94.5
   - Dogs Accuracy: 92.5


