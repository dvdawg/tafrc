#for GUI
import tkinter as tk
#for plotting
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

from trajectory import Trajectory

# plot constant
xlabel = ["x(m)", "x(m)", "y- height(m)"]
ylabel = ["y- height(m)", "z(m)", "z(m)"]
plot_title = ["x-y", "x-z","y-z"]

#UI class for control parameters, calculate button and plot
class shooterGUI():
    def __init__(self):
        #class for calculation that provides data for plotting
        self.main_tech = Trajectory()

        # the main window object
        self.main_wnd = tk.Tk() 
        self.main_wnd.title(self.main_tech.title)
        
        def exit_function():
            # Put any cleanup here.  
            self.main_wnd.quit()

        self.main_wnd.protocol('WM_DELETE_WINDOW', exit_function)


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
        self.fig = plt.figure(figsize = (5,6), dpi = 100)
        self.fig.subplots_adjust(hspace=.5)

        #label and values for variables
        self.label2 = [] * 10 #TODO: macro instead of 10
        self.label  = [] * self.numparam 
        self.e1     = [] * self.numparam 

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

        #   place example values for the variables
        for i, val in enumerate(self.main_tech.default_val):
            self.e1[i].insert(tk.END, val)

        # Create a RESULT Button & attached to calculation function
        self.button_result = tk.Button(self.control_frame, text = "RESULT", bg = "red", fg = "black", width=15, command = self.calculate)    
        self.button_result.grid(row = self.numparam+2, column = 1)
        
        var = tk.StringVar()
        var.set("========= Usage =========\n\
                Input the values in the boxes to simulate the \n\
                path of your field element relative to your target.\n\
                All units are in SI units - \n\
                distance and height - meters\n\
                velocity - meters/second \n\
                angle - degrees relative to coordinate axes\n\n\
                1. input shooter height, target height, and target x/z\n\
                2. input initial velocity and the shooter orientation(angles)\n\
                3. set time to interval (in seconds)\n\
                4. press result to view the trajectory with these conditions\n\
                5. adjust shooter angles to hit the target, repeat until the path of the projectile hits the target.")  
        self.label2.append(tk.Label( self.control_frame, textvariable=var).grid(row=self.numparam))

    def _init_right_frame(self):
        ##### plotting
        # Plotting the graph inside the Figure - add subplot
        
        self.subplot = [self.fig.add_subplot(311), self.fig.add_subplot(312),self.fig.add_subplot(313)]

        # Creating Canvas that connect tkinter and matplot
        self.canv = FigureCanvasTkAgg(self.fig, master = self.plot_frame)
        get_widz = self.canv.get_tk_widget()
        get_widz.pack()
        #TODO: add reset button for resetting all the values ?      

    #bottom frame for now only has close button. 
    def _init_bottom_frame(self):
        #add widgets
        self.button1 = tk.Button(self.bottomframe, text='Close', width=25, command=self.main_wnd.quit)
        self.button1.pack()

    
    def calculate(self):
        # get parameter values from GUI
        for i in range(self.numparam):
            self.main_tech.setparameters(i,self.e1[i].get())

        # do calculation with the parameters 
        x, y, z = self.main_tech.calculateTrajct()
  
        
        # after calculation, it is ready to plot
        self.updateplot(x,y,z)
    
    def updateplot(self, x, y, z):
        self.fig.clf()
        self.subplot = [self.fig.add_subplot(311), self.fig.add_subplot(312),self.fig.add_subplot(313)]
        for i, subplot in enumerate(self.subplot):
            
            if i==0:
                plot_x = x
                plot_y = y
                #plot the target location
                
                markerline, stemlines, baseline = subplot.stem(float(self.main_tech.paramlist['target_x(m)']),float(self.main_tech.paramlist['target_y_height']), markerfmt='o',label='target',basefmt="m")       
                plt.setp(stemlines, 'linewidth', 0)
            elif i==1:
                plot_x = x
                plot_y = z
                #plot the target location
                markerline, stemlines, baseline = subplot.stem(float(self.main_tech.paramlist['target_x(m)']),float(self.main_tech.paramlist['target_z']), markerfmt='o',label='target',basefmt="m")       
                plt.setp(stemlines, 'linewidth', 0)
            elif i==2:
                plot_x = y
                plot_y = z
                #plot the target location
                markerline, stemlines, baseline = subplot.stem(float(self.main_tech.paramlist['target_y_height']),float(self.main_tech.paramlist['target_z']), markerfmt='o',label='target',basefmt="m")       
                plt.setp(stemlines, 'linewidth', 0)
            
            #plot trajectory
            self.setplotvals(subplot,plot_x,plot_y, xlabel[i], ylabel[i], plot_title[i])

            
        
        self.canv.draw()


    def setplotvals(self, subplot,x,y,xlabel, ylabel, title):

        #subplot.stem(self.main_tech.paramlist['target_x(m)'],self.main_tech.paramlist['target_y_height'], markerfmt='o',label='target')


        subplot.plot(x,y, marker = "o", label = "Trajectory")
        
        subplot.set_xlabel(xlabel,  loc='right')
        subplot.set_ylabel(ylabel)
        subplot.set_title(title)
        subplot.legend()
        subplot.grid()

        

        

def main():
    sh_gui = shooterGUI()
    sh_gui.run_gui_loop()


if __name__ == "__main__":
    main()


