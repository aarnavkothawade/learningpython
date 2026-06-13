class MatUtils:
    def __init__(self):
        pass

    @staticmethod
    def sum(a, b):
        return a+b
    
    @classmethod 
    def description(cls):
        print("This is a utility class for math operations.")

# a = MatUtils
# print(a.sum(1,2))
# a.description()

print(MatUtils.sum(1,2))
MatUtils.description()