import pytest
from main import Mashey_Assessment
import json
from sample_expected_asteroid_closest_approach import Sample

class TestClass:

    def test(self):

        with open("asteroid_closest_approach.json") as json_file1:
            data1 = json.load(json_file1)

        with open("sample_expected_asteroid_closest_approach.json") as json_file2:
            data2 = json.load(json_file2)

        temp1 = data1[0]

        print(temp1)
        
        temp2 = data2

        assert temp1 == temp2


        json_file1.close()
        json_file2.close()

    