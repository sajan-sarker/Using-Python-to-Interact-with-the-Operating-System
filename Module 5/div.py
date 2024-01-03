def enhance_read_and_divide(filename):
    try: 
        with open(filename) as file:
            data = file.readline()
        if len(data) < 2:
            raise ValueError
        
        n1 = int(data[0])
        n2 = int(data[1])

        return n1/n2
    except FileNotFoundError:
        return "Error: File not found!"
    except ValueError:
        return "Not Enough data in the file."
    except ZeroDivisionError:
        return "Divition error: {zde}"
    
print(enhance_read_and_divide("./Module 5/div.txt"))