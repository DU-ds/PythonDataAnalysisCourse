#!/usr/bin/env python3
import re

def file_extensions(filename):
    lst = []
    dikt = {}
    with open(filename, "r") as f:
        for line in f:
            extension = extension_regex(line)
            line = line.rstrip() # could use strip() also
            if len(extension) == 0:
                lst.append(line)
            else:
                if extension in dikt:
                    files = dikt[extension]
                    files.append(line)
                    dikt[extension] = files
                else:
                    dikt[extension] = [line]
    return (lst, dikt)


def extension_regex(s, exclude = False):
    """
    Args:
        s: string
            filename
        exclude: boolean
            default false. Set to true to exclude files 
            like .foo from be considered as foo files.
            e.g. when false .bashrc is a bashrc file
    Returns:
        extension:
            file extension of s. Returns the empty string "" if s has no extension.
            
            Note: without exclude .files like .bashrc will be considered as bashrc files
    """
    regex = "[.]{1}(\w+)\n*\Z" #\n* bc newline may or may not be there (e.g. file could end on last line)
    if exclude:
        regex = "\w+" + regex
    result = re.findall(regex, s) # returns a list
    if len(result) == 0:
        return "" #no extension
    else:
        return result[0] # string in list


def main():
    result = file_extensions("src/filenames.txt")
    # filename = "/home/du_ds/Documents/Git/PythonDataAnalysisCourse/hy-data-analysis-with-python-summer-2019/part02-e07_file_extensions/src/filenames.txt"
    # result = file_extensions(filename)
    no_extension = result[0]
    extension_dict = result[1]
    print("%d files with no extension" % len(no_extension))
    keys = sorted(extension_dict)
    # for file_type in keys:
    #     n = len(extension_dict[file_type])
    #     print("%s %d" % (file_type, len(extension_dict[file_type])))

if __name__ == "__main__":
    main()
