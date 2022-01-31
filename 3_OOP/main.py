from shapes import Circle, Rectangle
import pickle

def read_bin(shapes_list):
    with open("shapes_bin.bin", "rb") as file:
        loaded_file = pickle.load(file)

    return loaded_file

def write_bin(shapes_list):
    with open("shapes_bin.bin", "wb") as file:
        pickle.dump(shapes_list,file)



def main():


    circle1 = Circle(3.00, (0, 0))
    circle2 = Circle(5.00, (0,0))

    rec1 = Rectangle(2.00, 4.00, (5, 3))
    rec2 = Rectangle(3.00, 5.00, (5, 10))

    shapes_list = []
    shapes_list.append(circle1)
    shapes_list.append(circle2)
    shapes_list.append(rec1)
    shapes_list.append(rec2)

    write_bin(shapes_list)
    loaded_file = read_bin(shapes_list)

    print(loaded_file)

if __name__ == "__main__":
    main()