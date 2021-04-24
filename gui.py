from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from main import CsvDavinciConverter as dr

class TkinterSettings:

    def __init__(self, root):
        self.mainframe = ttk.Frame(root, padding="5 5 12 12")

        root.title('Davinci CSV Converter')
        root.iconbitmap('davinci-resolve.ico')

        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.label = ttk.Label(self.mainframe, text="Select a Davinci Resolve CSV File").grid(column=1, row=1, sticky=W)
        ttk.Label(self.mainframe, text="Save Converted CSV File To").grid(column=1, row=2, sticky=W)
        ttk.Button(self.mainframe, text="Browse", command=self.open_file).grid(column=3, row= 1, sticky="W")
        ttk.Button(self.mainframe, text='Browse', command=self.where_save).grid(column=3, row=2, sticky="W")
        ttk.Button(self.mainframe, text='Start', command=lambda: self.start_conversion(self.filename, self.output_file)).grid(column=3, row=4, sticky=(N, W, E, S))

        self.status_of_program()

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        super().__init__()

    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir=".", title="Select a file",
                                                   filetypes=[("Csv Files", "*.csv"), ("EDL Files", "*.edl")])
        self.status_of_program("csv_selected")

    def where_save(self):
        self.output_file = filedialog.asksaveasfilename(initialdir=".", title="Save the exported CSV file in",
                                                   filetypes=[("csv files", "*.csv"), ("all files", "*.*")])
        self.status_of_program("save_to_selected")

    def start_conversion(self, input, output):
        converter = dr()
        converter.convert(input, output)
        self.status_of_program("conversion_finalized")

    def status_of_program(self, status=None):
        if status == "csv_selected":
            output = str(self.filename).split("/")
            self.label = ttk.Label(self.mainframe, text="{} was selected.".format(output[-1])).grid(row=5, column=1, columnspan=5,
                                                                                       sticky=W)
        elif status == "save_to_selected":
            output = str(self.output_file).split("/")
            self.label = ttk.Label(self.mainframe, text="{} will be created.".format(output[-1])).grid(row=5, column=1, columnspan=5,
                                                                                       sticky=W)
        elif status == "conversion_finalized":
            output = str(self.output_file).split("/")
            self.label = ttk.Label(self.mainframe, text="{} successful created.".format(output[-1])).grid(row=5, column=1, columnspan=5,
                                                                                       sticky=W)
        else:
            self.label = ttk.Label(self.mainframe, text="Ready for convert.").grid(row=5, column=1, columnspan=5,
                                                                                       sticky=W)


root = Tk()
TkinterSettings(root)
root.mainloop()

