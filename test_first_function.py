import pytest
from main import Mashey_Assessment
import sample_expected_asteroid_closest_approach

class TestClass:

    def __init__(self):
        
        # To use the api_data.json file in all functions of the class
        self.file1 = "asteroid_closest_approach.json"
        self.file2 = "sample_expected_asteroid_closest_approach.json"
        self.data1 = None
        self.data2 = None
        self.json_file1 = None
        self.json_file2 = None


    def test(self):

        with open(self.file1) as self.json_file1:
            self.data1 = json.load(self.json_file1)

        with open(self.file2) as self.json_file2:
            self.data2 = json.load(self.json_file2)

        temp1 = self.data1[0]

        temp2 = self.data2

        
        assert temp1 == temp2


        self.json_file1.close()
        self.json_file2.close()

    