import unittest
########################################
# Merge sort code
########################################

def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            result += z
            z = []
        else:
            result += y
            y = []
    return result
    

########################################
# Testing code
########################################

## Add code here ##

class MergeSortTester(unittest.TestCase):
    def test_case_1(self):
        """
        The test_case_1 function tests the user defined list.
        It calls the merge_sort function which takes the user defined list and return the sorted list using Merge Sort
        algorithm.
        After running the algorithm, it checks the correctness of the output with the one that user expects.

        """
        list = [5,4,1,3,2]
        got = merge_sort(list)
        expected = [1,2,3,4,5]
        self.assertEqual(got,expected)


    def test_case_2(self):
        """
        The test_case_2 function tests the user defined list.

        It calls the merge_sort function which takes the user defined list and return the sorted list using Merge Sort
        algorithm.
        It first checks if the user defined list and the merge sorted list has the same number of elements or not.
        After checking the equality of number of elements, it checks the correctness of the output with the one that
        user expects.


        """

        list = [10.5,9.4,8.3,7.2,6.1,5.9,4.8,3.7,2.6,1.5]
        got = merge_sort(list)
        expected = [1.5,2.6,3.7,4.8,5.9,6.1,7.2,8.3,9.4,10.5]

        self.assertCountEqual(list,expected)
        self.assertEqual(got, expected)


########################################
# Main
########################################
if __name__=="__main__":
    unittest.main()