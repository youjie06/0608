from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser
from PIL import Image, ImageTk

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.fontSize = 12
        self.fontStyle = 'Arial'
        
        # Colors
        self.white="#ffffff"
        self.black="#000000"
        self.darkBG1="#2d2f32"
        self.darkBG2="#3f4145"
        self.darkBG3="#5c5f64"
        self.brightBG1 ="#e3e5e8"
        self.brightBG2 ="#f7f6f7"
      
        # Text frame
        self.text_frame = Frame(self.root, border=0)
        self.text_frame.pack(padx=10, pady=10)
        
        # Label frame for title
        self.labelframe = LabelFrame(self.text_frame, width=400, height=50, text='標題', border=0)
        self.labelframe.pack(padx=10, pady=2)
        self.input_font = ("Helvetica", 20)

        # Text area for title
        self.text_area = Text(self.labelframe, width=400, height=1, wrap='none', font=self.input_font, bg=self.darkBG3, fg=self.white)
        self.text_area.pack()

        # Tool bar
        self.tool_bar = Label(self.text_frame)
        self.tool_bar.pack(side=TOP, padx=10, pady=0, fill=X)
        self.font_families = font.families()
        self.font_family_variable = StringVar()
        self.fontfamily_Combobox = Combobox(self.tool_bar, width=30, value=self.font_families, state='readonly',
                                       textvariable=self.font_family_variable)
        self.fontfamily_Combobox.current(self.font_families.index('Arial'))
        self.fontfamily_Combobox.grid(row=0, column=0, padx=13)
        self.size_variable = IntVar()
        self.font_size_Combobox = Combobox(self.tool_bar, width=14, textvariable=self.size_variable, state='readonly',
                                      values=tuple(range(8, 81)))
        self.font_size_Combobox.current(4)
        self.font_size_Combobox.grid(row=0, column=1, padx=5)

        self.fontfamily_Combobox.bind('<<ComboboxSelected>>', self.font_style)
        self.font_size_Combobox.bind('<<ComboboxSelected>>', self.font_size)

        # Buttons for formatting
        self.bold_image = Image.open('icon/bold.png')
        self.bold_icon = ImageTk.PhotoImage(self.bold_image)
        self.boldButton = Button(self.tool_bar, image=self.bold_icon, command=self.bold_text)
        self.boldButton.grid(row=0, column=3, padx=5)

        self.italic_image = Image.open('icon/italic.png')
        self.italic_icon = ImageTk.PhotoImage(self.italic_image)
        self.italicButton = Button(self.tool_bar, image=self.italic_icon, command=self.italic_text)
        self.italicButton.grid(row=0, column=4, padx=5)

        self.underline_image = Image.open('icon/underline.png')
        self.underline_icon = ImageTk.PhotoImage(self.underline_image)
        self.underlineButton = Button(self.tool_bar, image=self.underline_icon, command=self.underline_text)
        self.underlineButton.grid(row=0, column=5, padx=5)

        self.font_color_image = Image.open('icon/font_Color.png')
        self.font_color_icon = ImageTk.PhotoImage(self.font_color_image)
        self.fontColorButton = Button(self.tool_bar, image=self.font_color_icon, command=self.color_select)
        self.fontColorButton.grid(row=0, column=6, padx=5)

        self.left_align_image = Image.open('icon/left.png')
        self.left_align_icon = ImageTk.PhotoImage(self.left_align_image)
        self.leftAlignButton = Button(self.tool_bar, image=self.left_align_icon, command=self.align_left)
        self.leftAlignButton.grid(row=0, column=7, padx=5)

        self.center_align_image = Image.open('icon/center.png')
        self.center_align_icon = ImageTk.PhotoImage(self.center_align_image) 
        self.centerAlignButton = Button(self.tool_bar, image=self.center_align_icon, command=self.align_center)
        self.centerAlignButton.grid(row=0, column=8, padx=5)

        self.right_align_image = Image.open('icon/right.png')
        self.right_align_icon = ImageTk.PhotoImage(self.right_align_image)
        self.rightAlignButton = Button(self.tool_bar, image=self.right_align_icon, command=self.align_right)
        self.rightAlignButton.grid(row=0, column=9, padx=5)

        # Label frame for content
        self.contentframe = LabelFrame(self.text_frame, width=400, height=150, text='內容', border=0)
        self.contentframe.pack(padx=10, pady=4)

        # Text input for content
        self.text_input = Text(self.contentframe, width=400, height=150, wrap='word', font=(16), bg=self.darkBG3, fg=self.white)
        self.text_input.pack(fill=BOTH, expand=True)

        self.root.mainloop()
    
    # Function to change font style
    def font_style(self,event=None):
        self.fontStyle = 'Arial'
        self.fontStyle = self.font_family_variable.get()
        self.text_input.config(font=(self.fontStyle, self.fontSize))

    # Function to change font size
    def font_size(self,event=None):
        self.fontSize = 12
        self.fontSize = self.size_variable.get()
        self.text_input.config(font=(self.fontStyle, self.fontSize))

    # Function to make text bold
    def bold_text(self):
        text_property = font.Font(font=self.text_input['font']).actual()
        if text_property['weight'] == 'normal':
            self.text_input.config(font=(self.fontStyle, self.fontSize, 'bold'))
        elif text_property['weight'] == 'bold':
            self.text_input.config(font=(self.fontStyle, self.fontSize, 'normal'))

    # Function to make text italic
    def italic_text(self):
        text_property = font.Font(font=self.text_input['font']).actual()
        if text_property['slant'] == 'roman':
                self.text_input.config(font=(self.fontStyle, self.fontSize, 'italic'))
        elif text_property['slant'] == 'italic':
            self.text_input.config(font=(self.fontStyle, self.fontSize, 'roman'))

    # Function to underline text
    def underline_text(self):
        text_property = font.Font(font=self.text_input['font']).actual()
        if text_property['underline'] == 0:
            self.text_input.config(font=(self.fontStyle, self.fontSize, 'underline'))
        elif text_property['underline'] == 1:
            self.text_input.config(font=(self.fontStyle, self.fontSize, 'normal'))

    # Function to select font color
    def color_select(self):
        color = colorchooser.askcolor()
        self.text_input.config(fg=color[1])

    # Function to align text right
    def align_right(self):
        self.text_input.tag_config('right', justify=RIGHT)
        self.text_input.tag_add('right', '1.0', END)

    # Function to align text left
    def align_left(self):
        self.text_input.tag_config('left', justify=LEFT)
        self.text_input.tag_add('left', '1.0', END)

    # Function to align text center
    def align_center(self):
        self.text_input.tag_config('center', justify=CENTER)
        self.text_input.tag_add('center', '1.0', END)
                
    def toggle_mode(self, mode_day):
        # change color
        self.mode_day = mode_day
        if self.mode_day:
            self.currentbg_color = self.darkBG2   
            self.currentfg_color = self.white
        else:
            self.currentbg_color = self.brightBG2
            self.currentfg_color = self.black

        # Update colors
        self.text_area.config(bg=self.currentbg_color, fg=self.currentfg_color)
        self.text_input.config(bg=self.currentbg_color, fg=self.currentfg_color)



