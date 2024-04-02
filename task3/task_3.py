import os


def read_file(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines
    

def union() -> None:
    files = [file for file in os.listdir() if file.endswith(".txt")]
    files = sorted(files, key=lambda x: len(read_file(x)))
    with open("result.txt", "w") as result_file:
        for file_name in files:
            lines = read_file(file_name)
            result_file.write(f"{file_name}\n{len(lines)}\n")
            for line in lines:
                result_file.write(line)
            result_file.write("\n")


def main() -> None:
    union()


if __name__ == '__main__':
    main()