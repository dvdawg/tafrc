#for GUI
import tkinter as tk
#for plotting
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
#replace trajectory with your class
from trajectory import Trajectory

#UI class for control parameters, calculate button and plot
class shooterGUI():
    def __init__(self):
        #class for calculation that provides data for plotting
        self.main_tech = Trajectory()

        # the main window object
        self.main_wnd = tk.Tk() 
        self.main_wnd.title(self.main_tech.title)
        
        # number of variables, list is defined in the main tech (trajectory class)
        self.numparam = len(self.main_tech.paramlist)

        #initialize GUI
        self._init_GUI()

    def _init_GUI(self):
        #bottom frame for text and misc, not necessarily required...
        self.bottomframe = tk.Frame(self.main_wnd)
        self.bottomframe.pack( side = tk.BOTTOM )

        #frame for control parameters
        self.control_frame = tk.Frame(self.main_wnd)
        self.control_frame.pack(side = tk.LEFT, padx = "10")

        #frame for plotting
        self.plot_frame = tk.Frame(self.main_wnd)
        self.plot_frame.pack( side = tk.RIGHT )

        # Creating a figure for plotting
        self.fig = Figure(figsize = (5,5), dpi = 100)

        #label and values for variables
        self.label  = []*self.numparam 
        self.e1     = []*self.numparam 

        # init frames and plot
        self._init_left_frame() 
        self._init_right_frame()
        self._init_bottom_frame()

    #GUI loop => runs GUI    
    def run_gui_loop(self):
        self.main_wnd.mainloop()

     # *** parameter (left) window
    def _init_left_frame(self):
        for i in range(self.numparam):
            #take pamameter name from the list for display
            self.label.append(tk.Label(self.control_frame, text=self.main_tech.param_str[i]).grid(row=i,ipadx ="10",ipady ="10"))
            #el = text boxes to get parameter values
            self.e1.append(tk.Entry(self.control_frame))
            self.e1[i].insert(tk.END, '0')
            self.e1[i].grid(row=i, column=1)

        # Create a RESULT Button & attached to calculation function
        self.button_result = tk.Button(self.control_frame, text = "RESULT", bg = "red", fg = "black", width=15, command = self.calculate)    
        self.button_result.grid(row = self.numparam+2, column = 1)
    
    def _init_right_frame(self):
        ##### plotting

        # Plotting the graph inside the Figure - add subplot
        self.subplot = self.fig.add_subplot(111)

        # Creating Canvas that connect tkinter and matplot
        self.canv = FigureCanvasTkAgg(self.fig, master = self.plot_frame)
        get_widz = self.canv.get_tk_widget()
        get_widz.pack()
        #TODO: add reset button for resetting all the values ?
    
    #bottom frame for now only has close button. 
    def _init_bottom_frame(self):
        #add widgets
        self.button1 = tk.Button(self.bottomframe, text='Close', width=25, command=self.main_wnd.destroy)
        self.button1.pack()
    
    def calculate(self):
        # get parameter values from GUI
        for i in range(self.numparam):
            self.main_tech.setparameters(i,self.e1[i].get())

        # do calculation with the parameters 
        traj_x, traj_y = self.main_tech.calculateTrajct()

        # after calculation, it is ready to plot
        self.updateplot(traj_x, traj_y)
    
    def updateplot(self, x, y):
        subplot = self.subplot
        subplot.plot(x,y, marker = "o", label = "Trajectory")
        subplot.set_xlabel("height (m)")
        subplot.set_ylabel("x (m)")
        subplot.set_title("Graph_Tk")
        subplot.legend()
        subplot.grid()
        self.canv.draw()


def main():
    sh_gui = shooterGUI()
    sh_gui.run_gui_loop()


if __name__ == "__main__":
    main()



# # ----== init window ==-------------------------------

# # the main window object
# main_wnd = tk.Tk()
# main_wnd.title('Your title')

# #bottom frame for text and misc, not necessarily required...
# bottomframe = tk.Frame(main_wnd)
# bottomframe.pack( side = tk.BOTTOM )

# #frame for control parameters
# control_frame = tk.Frame(main_wnd)
# control_frame.pack(side = tk.LEFT, padx = "10")

# #frame for plotting
# plot_frame = tk.Frame(main_wnd)
# plot_frame.pack( side = tk.RIGHT )

# # ----== init figure for plotting ==-------------------------------

# # Creating Figure.
# fig = Figure(figsize = (5,5), dpi = 100)


# # ----== init constant and GUI variables ==-------------------------------
# #init constant
# NUMPARAM = 10
# label = []*NUMPARAM
# e1= []*NUMPARAM

# #TODO: make a class containing canv, subplot, x, y

# # ----== functions for GUI ==-------------------------------
# def calculate(paramlist, canv, subplot):
#     # do calculation here
#     x=[ 1, 2, 3 ,4 ,5 ,6 ,7]
#     y=[ 1, 2, 3, 4, 5, 6, 7]
#     # call update plot 
#     updateplot(canv, subplot, x, y)

# def updateplot(canv, subplot, x, y):
    
#     subplot.plot(x,y, marker = "o", label = "Trajectory")
#     subplot.set_xlabel("height (m)")
#     subplot.set_ylabel("x (m)")
#     subplot.set_title("Graph_Tk")
#     subplot.legend()
#     subplot.grid()
#     canv.draw()

# # ----== build GUI ==-------------------------------

# # *** parameter (left) window

# for i in range(NUMPARAM):
#     label.append(tk.Label(control_frame, text='Param'+str(i)).grid(row=i,ipadx ="10",ipady ="10"))
#     e1.append(tk.Entry(control_frame))
#     e1[i].grid(row=i, column=1)

# # Create a RESULT Button & attached to calculation function
# button_result = tk.Button(control_frame, text = "RESULT", bg = "red", fg = "black", width=15, command = calculate)    
# button_result.grid(row = NUMPARAM+2, column = 1)



# ##### plotting

# x = []
# y = []

# # Plotting the graph inside the Figure
# subplot = fig.add_subplot(111)


# # Creating Canvas
# canv = FigureCanvasTkAgg(fig, master = plot_frame)

# updateplot(canv, subplot, x, y)

# get_widz = canv.get_tk_widget()
# get_widz.pack()

# #add widgets
# button1 = tk.Button(bottomframe, text='Close', width=25, command=main_wnd.destroy)
# button1.pack()

# main_wnd.mainloop()

