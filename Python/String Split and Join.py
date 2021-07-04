def split_and_join(line):
    line = line.split(" ") #first splitted string to words and  join them with - sign.
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
