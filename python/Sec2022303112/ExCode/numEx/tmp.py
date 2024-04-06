def b64en(path_in, path_out):
    with open(path_in, 'rb')  as file_object:
        binary = file_object.read()
        
        IndexOfLastTriple = len(binary) // 3 * 3
        for i in range(0, IndexOfLastTriple):







b64en("../testCase/testData/pic.jpg", "../testCase/testData/pic.txt")