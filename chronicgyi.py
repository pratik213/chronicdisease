from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import tkinter.messagebox as tmsg
import tkinter.filedialog as fldg
import tkinter.font as tkFont

class ChronicKidneyGui(Tk):

    def __init__(self):
        super().__init__()
        # logo_image1 = ImageTk.open('300Logo.png')
        # self.myimage = ImageTk.PhotoImage(Image.open('300Logo.png'))
        # self.iconphoto(False,self.myimage)

        # Window Geometry
        self.geometry('795x500')

        # Window Title
        self.title('Chronic Kidney Disease Prediction')

        # Root Color
        self.configure(bg='#2C3539')

        # Fonst Style
        self.fontStyle = tkFont.Font(family="comic sans ms", size=15)

        # Menu Bar
        self.mainmenue = Menu(self,font=self.fontStyle)
        self.filemenue = Menu(self.mainmenue, tearoff =False)
        self.filemenue.add_command(label="Open", command= lambda :print('Its Working'))
        self.filemenue.add_command(label='Save As',command=lambda  : print('Its woring'))
        self.filemenue.add_command(label='Exit',command=self.quit)
        self.config(menu=self.mainmenue)
        self.mainmenue.add_cascade(label='File', menu = self.filemenue)

        self.Edit_menu = Menu(self.mainmenue, tearoff=False)
        self.Edit_menu.add_command(label="Clear All", command=lambda :print('Its Working'))
        self.Edit_menu.add_command(label="Find Number of text", command=lambda :print('Its Working'))
        self.Edit_menu.add_command(label="Replace text", command=lambda :print('Its Working'))
        self.config(menu=self.mainmenue)
        self.mainmenue.add_cascade(label="Edit", menu=self.Edit_menu)

        self.view_menu = Menu(self.mainmenue, tearoff=False)
        self.zoom_menu = Menu(self.view_menu, tearoff=False)
        self.zoom_menu.add_command(label="Increase font", command=lambda :print("Its woring"))
        self.zoom_menu.add_command(label="Decrease Font", command=lambda :print("Its woring"))
        self.zoom_menu.add_command(label="Restore To Default", command=lambda :print("Its woring"))
        self.view_menu.add_cascade(label="Change Font Size", menu=self.zoom_menu)
        self.config(menu=self.mainmenue)
        self.mainmenue.add_cascade(label="View", menu=self.view_menu)

        self.Format_menu = Menu(self.mainmenue, tearoff=False)
        self.Format_menu.add_command(label="Default Theme", command=lambda :print("Its woring"))
        self.Format_menu.add_command(label="Dark Theme", command=lambda :print("Its woring"))
        self.config(menu=self.mainmenue)
        self.mainmenue.add_cascade(label="Format", menu=self.Format_menu)

        # configuring Menue Items


        #

        # Widgets Inside The main Window

        self.frame_1 = Frame(self, borderwidth=4, relief='groove',bg='#98AFC7')
        # self.frame_1.grid(row=0, column=0,padx=5)
        self.frame_1.place(relx=0.001,rely=0)


        self.label_First_info = Label(self.frame_1, text="Fill The Data On The Fields", font=("comic sans ms", 15, "italic",'underline'),borderwidth=2,relief='groove')
        self.label_First_info.grid(row=0,column=0,padx=10,pady=10,columnspan=6)

        self.label_sg = Label(self.frame_1, text="Sg :", font=("comic sans ms", 10, "italic"))
        self.label_sg.grid(row=1,column=0,padx=1,pady=10)

        self.entry_wid_sg = Entry(self.frame_1,width=15,borderwidth=3)
        self.entry_wid_sg.grid(row=1, column=1)

        self.label_al = Label(self.frame_1, text="Al :", font=("comic sans ms", 10, "italic"))
        self.label_al.grid(row=2, column=0, padx=1, pady=10)

        self.entry_wid_al = Entry(self.frame_1, width=15,borderwidth=3)
        self.entry_wid_al.grid(row=2, column=1)

        self.label_sc = Label(self.frame_1, text="Sc :", font=("comic sans ms", 10, "italic"))
        self.label_sc.grid(row=3, column=0, padx=1, pady=10)

        self.entry_wid_sc = Entry(self.frame_1, width=15,borderwidth=3)
        self.entry_wid_sc.grid(row=3, column=1)

        self.label_hemo = Label(self.frame_1, text=" Hemo :", font=("comic sans ms", 10, "italic"))
        self.label_hemo.grid(row=4, column=0, padx=1, pady=10)

        self.entry_wid_hemo = Entry(self.frame_1, width=15,borderwidth=3)
        self.entry_wid_hemo.grid(row=4, column=1)

        self.label_pcv = Label(self.frame_1, text="Pcv :", font=("comic sans ms", 10, "italic"))
        self.label_pcv.grid(row=5, column=0, padx=1, pady=10)

        self.entry_wid_pcv = Entry(self.frame_1, width=15,borderwidth=3)
        self.entry_wid_pcv.grid(row=5, column=1)

        self.label_wbcc = Label(self.frame_1, text="Wbcc :", font=("comic sans ms", 10, "italic"))
        self.label_wbcc.grid(row=6, column=0, padx=1, pady=10)

        self.entry_wid_wbcc = Entry(self.frame_1, width=15,borderwidth=3)
        self.entry_wid_wbcc.grid(row=6, column=1)

        self.label_rbcc = Label(self.frame_1, text="Rbcc :", font=("comic sans ms", 10, "italic"))
        self.label_rbcc.grid(row=7, column=0, padx=1, pady=10)

        self.entry_wid_rbcc = Entry(self.frame_1, width=15,borderwidth=3)
        self.entry_wid_rbcc.grid(row=7, column=1)

        self.label_htn = Label(self.frame_1, text="Htn :", font=("comic sans ms", 10, "italic"))
        self.label_htn.grid(row=8, column=0, padx=1, pady=10)

        self.entry_wid_htn = Entry(self.frame_1, width=15,borderwidth=3)
        self.entry_wid_htn.grid(row=8, column=1)

        self.submit_btn = Button(self.frame_1, text = 'Run Diagnostics',font=("comic sans ms", 10, "italic"))
        self.submit_btn.grid(row=9,column=1,pady=10)



    # Second Frame On The Right Side

        self.frame_2 = Frame(self, borderwidth=4, relief='groove', bg='#437C17')
        # self.frame_2.grid(row=0, column=1,sticky=N)
        self.frame_2.place(relx=0.363,rely=0)

        self.label_result = Label(self.frame_2, text="Results On Console",
                                      font=("comic sans ms", 15, "italic", 'underline'), borderwidth=2, relief='groove')
        self.label_result.grid(row=0, column=1)


        self.text_wid_output = Text(self.frame_2,borderwidth=4,relief='groove',height=18,width=60)
        self.text_wid_output.grid(row=1,column=1)


    # # Final Frame For Showing Prediction
    #
        self.frame_3 = Frame(self, borderwidth=4, relief='groove', bg='#4088C7')
        # self.frame_3.grid(row=1, column=1,sticky=NW)
        self.frame_3.place(x=290,y=343)

        self.label_result = Label(self.frame_3, text="Final Classification",
                                  font=("comic sans ms", 15, "italic", 'underline'), borderwidth=2, relief='groove')
        self.label_result.grid(row=0, column=0)

        self.label_final_output = Label(self.frame_3, text="Your Are ==> ", borderwidth=3,relief='groove', font=("comic sans ms", 12, "italic"))
        self.label_final_output.grid(row=1,column=0)

        self.text_wid_final_classification_output=Text(self.frame_3,height=5,width=38,borderwidth=4,relief='groove')
        self.text_wid_final_classification_output.grid(row=1, column=1)

        # Some Extra Features
        self.frame_4 = Frame(self, borderwidth=4, relief='groove', bg='#98AFC7')
        self.frame_4.place(x=290, y=300)

        # self.label_extra_featues = Label(self.frame_4, text="Extra Features", borderwidth=3, relief='groove',
        #                                 font=("comic sans ms", 12, "italic"))
        # self.label_extra_featues.grid(row=0, column=0)

        self.extra_btn_plot_output = Button(self.frame_4,text='Plot The Output',font=("comic sans ms", 10, "italic"))
        self.extra_btn_plot_output.grid(row=0,column=0)

        self.extra_btn_plot_models_efficiency = Button(self.frame_4, text="Plot Model's Efficiency", font=("comic sans ms", 10, "italic"))
        self.extra_btn_plot_models_efficiency.grid(row=0, column=1)


if __name__ == '__main__':
    mainwin = ChronicKidneyGui()

    mainwin.mainloop()