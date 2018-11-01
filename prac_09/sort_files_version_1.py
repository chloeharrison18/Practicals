import os
import shutil

def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir("FilestoSort/FilestoSort")
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    try:
        os.mkdir('doc')
        os.mkdir('docx')
        os.mkdir('png')
        os.mkdir('gif')
        os.mkdir('txt')
        os.mkdir('xls')
        os.mkdir('xlsx')
        os.mkdir('jpg')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if "docx" in filename:
            shutil.move(filename,'docx')
        elif "doc" in filename:
            shutil.move(filename, 'doc')
        elif "png" in filename:
            shutil.move(filename, 'png')
        elif "gif" in filename:
            shutil.move(filename, 'gif')
        elif "txt" in filename:
            shutil.move(filename, 'txt')
        elif "xlsx" in filename:
            shutil.move(filename, 'xlsx')
        elif "xls" in filename:
            shutil.move(filename, 'xls')
        elif "jpg" in filename:
            shutil.move(filename, 'jpg')
        else:
            pass



main()