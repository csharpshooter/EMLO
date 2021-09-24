import os
import csv


class TestClass:

    def test_check_if_model_file_present_in_root_folder(self):
        assert os.path.isfile('model.pth') == False

    def test_check_if_data_folder_present_in_root_folder(self):
        assert os.path.isdir('./data') == False

    def test_check_if_metrics_csv_present_in_root_folder(self):
        assert os.path.isfile('metrics.csv') == True

    def test_validate_train_accuracy_greater_than_70_pct(self):
        with open("metrics.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                if row.__len__() > 0 and row[0].__contains__('Train'):
                    assert (float(row[0].split(':')[1]) > 70) == True

    def test_validate_test_accuracy_greater_than_70_pct(self):
        with open("metrics.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                if row.__len__() > 0 and row[0].__contains__('Test'):
                    assert (float(row[0].split(':')[1]) > 70) == True

    def test_validate_dog_class_accuracy_greater_than_70_pct(self):
        with open("metrics.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                if row.__len__() > 0 and row[0].__contains__('dogs'):
                    assert (float(row[1]) > 70) == True

    def test_validate_cat_class_accuracy_greater_than_70_pct(self):
        with open("metrics.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                if row.__len__() > 0 and row[0].__contains__('cats'):
                    assert (float(row[1]) > 70) == True
