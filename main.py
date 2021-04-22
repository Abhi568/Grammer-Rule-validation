from tkinter import*
import tkinter as tk
master = Tk()
master.geometry("850x700")
master.title('English Rule Program(Vigocare)')
background_image = PhotoImage(file="background.png")
background_label = Label(master, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

input_file = StringVar()
token_file = StringVar()
input_file_name = ""
token_file_name = ""
inputFile_name = ""
tokenFile_name = ""

def Add_Input_File():
    global inputFile_name
    input_file_name = input_file.get()
    for char in input_file_name:
        if char != '\n':
            inputFile_name += char
    print(inputFile_name)

def Add_Token_File():
    global tokenFile_name
    token_file_name = token_file.get()
    for char in token_file_name:
        if char != '\n':
            tokenFile_name += char
    print(tokenFile_name)


def View_Input_File():
    def openFile():
        tf = open("inputs.txt", "r")
        data = tf.read()
        txtarea.insert(END, data)
        tf.close()

    ws = Tk()
    ws.title("Input File")
    ws.geometry("400x450")
    ws['bg'] = 'blue'

    txtarea = Text(ws, width=40, height=20)
    txtarea.pack(pady=20)
    Button(ws, text="Open File", command=openFile,
           bg='blue', fg='pink').place(x=150, y=380)

    ws.mainloop()


def View_Token_File():
    def openFile():
        tf = open("tokens.txt", "r")
        data = tf.read()
        txtarea.insert(END, data)
        tf.close()

    ws = Tk()
    ws.title("Token File")
    ws.geometry("400x450")
    ws['bg'] = 'blue'

    txtarea = Text(ws, width=40, height=20)
    txtarea.pack(pady=20)
    Button(ws, text="Open File", command=openFile,
           bg='blue', fg='pink').place(x=150, y=380)
    ws.mainloop()


def Readme_content():
    readme = Tk()
    readme.title("Readme File")
    readme.geometry("500x500")
    readme['bg'] = 'blue'
    txtarea = Text(readme, width=53, height=46, bg='hotpink', font=20 ,fg="black")
    txtarea.pack(pady=10)
    text= " "*25+"Please read instructions carefully :"
    text1 = "\n1) By default your Input File name is : inputs.txt \n2) By default your Token File name is : tokens.txt and after entering names of both files, you need to click at add buttons otherwise you will not  get any output .\n3) On clicking Result button a file get created in your current folder where you have put your all files. "
    text2 = "\n4) Everytime you need to delete your previous created O/P file otherwise everytime new output will get appened with previous created O/P file, You can view your input and token files by just clicking on the button 'View Input File' and 'View Token File'"
    text3 = "\n5) Put all your files in a single folder and don't make any mistake in names while writing the name of Input and Tokens files and ensure that you have also clicked the 'add' button , just after writing the name of files. Be Careful:-)"
    text4 = "\n6) You can't edit the Input file and Token File by just clicking on the buttons ('View Input File' and 'View Token File ), it looks like that it is editable but it is not , because you can write in it from outside but it will not affect the actual files contents."
    text5 = "\n7) ** Steps ** -> Write name of input file as 'inputs.txt' , then click at 'add' button -> Enter the second file name as 'tokens.txt'and then click at 'add' button -> Click at 'Result' button -> check you folder a text file has been created ,name will be 'output.txt' "
    text6 = "\n8) Add button is not for adding contents in the files from outside it is only for letting the program to know about the name of files.\n9) If it shows any error, kindly close the project and open it again."
    all_text=text+text1+text2+text3+text4+text5+text6
    txtarea.insert(END, all_text)
    readme.mainloop()


def Result():
    token_dict = dict()
    token_obj = open('tokens.txt', 'r')
    token_list = token_obj.readlines()
    token_obj.close()

    for token in token_list:
        list1 = token.split(":")
        value = list1[1].lower()
        if value[-1] == "\n":
            token_dict[value[:len(value)-1]] = list1[0].lower()
        else:
            token_dict[value[:len(value)]] = list1[0].lower()

    Rule_list = [["subject", "verb", "article", "adjective", "predicate", "."], ["subject", "verb", "article", "predicate", "."],
                 ["verb", "subject", "article", "adjective", "predicate", "?"], ["verb", "subject", "article", "predicate", "?"]]

    input_obj = open('inputs.txt', 'r')
    input_list = input_obj.readlines()
    input_obj.close()

    for input1 in input_list:
        output = False
        sentence_list = []
        list2 = input1.split(" ")
        # cheking for "?" and "." and also checking for new line character at the end.
        if list2[-1][-1] == '\n':
            if list2[-1][-2] == ".":
                list2[-1] = list2[-1][:len(list2[-1])-2]
                list2.append('.')
            elif list2[-1][-2] == "?":
                list2[-1] = list2[-1][:len(list2[-1])-2]
                list2.append('?')
        else:
            if list2[-1][-1] == ".":
                list2[-1] = list2[-1][:len(list2[-1])-1]
                list2.append('.')
            elif list2[-1][-2] == "?":
                list2[-1] = list2[-1][:len(list2[-1])-1]
                list2.append('?')

        for each_word in list2:
            if each_word == '.' or each_word == '?':
                sentence_list.append(each_word)
            elif each_word.lower() not in token_dict:
                output = False
                break
            else:
                sentence_list.append(token_dict[each_word.lower()])

        for pos in range(len(Rule_list)):
            if Rule_list[pos] == sentence_list:
                output = True
                break
            else:
                output = False

        output_file_obj = open("output_file.txt", "a+")
        if output == False:
            output_file_obj.write(" ".join(list2) + ' ( Invalid)'+'\n')
        else:
            output_file_obj.write(
                " ".join(list2) + '\n' + '(Valid . Supports Rule'+str(pos+1)+')'+'\n')
        print(list2, sentence_list, output)
    output_file_obj.close()
    global pop_up
    pop_up = Toplevel(master)
    pop_up.title("Successfullt created")
    pop_up.configure(bg='Blue')
    pop_up.geometry("250x200")
    Label(pop_up, text="Successfullt created('output_file.txt'):-)",
          fg='Blue').pack()
    Button(pop_up, text="Okay", command=created,
           fg='blue', bg='Blue', background='Red').pack()
    return


def created():
    pop_up.destroy()
    return

canvas = Canvas(master, width=98, height=95, bg='blue')
canvas.pack()
canvas.place(x=360, y=30)
img = PhotoImage(file="eng2.png")
canvas.create_image(10, 10, anchor=NW, image=img)

Readme_Button = Button(master, text="Readme",
                       command=Readme_content, font=10, bg='blue', fg='pink')
Readme_Button.place(x=373, y=140)

l1 = Label(master, text="Input File", fg='red')
l1.config(width=10, font=30)
l1.place(x=180, y=240)

Input_File = Entry(master, textvariable=input_file, font=35)
Input_File.place(x=320, y=240)

Input_Button = Button(master, text="Done",
                      command=Add_Input_File, font=10, bg='blue', fg='pink')
Input_Button.place(x=540, y=240)

Input_Button = Button(master, text="View Input File",
                      command=View_Input_File, font=10, bg='blue', fg='pink')
Input_Button.place(x=600, y=240)

l2 = Label(master, text="Token File", fg='red')
l2.config(width=10, font=30)
l2.place(x=180, y=290)

Token_File = Entry(master, textvariable=token_file, font=35)
Token_File.place(x=320, y=290)

Token_Button = Button(master, text="Done",
                      command=Add_Token_File, font=10, bg='blue', fg='pink')
Token_Button.place(x=540, y=290)

Token_Button = Button(master, text="View Token File",
                      command=View_Token_File, font=10, bg='blue', fg='pink')
Token_Button.place(x=600, y=290)

Result_Button = Button(master, text="Result",
                       command=Result, font=20, bg='blue', fg='pink')
Result_Button.place(x=385, y=350)

mainloop()
