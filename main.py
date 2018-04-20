import Tkinter as tk
from Tkinter import *
import graphlab
import tkMessageBox
class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x900')
        self.configure(background='#899FFA')
        self.title("House Selling Price Predictor")
        self.e1=tk.Label(self,text="House Selling Price Predictor",font="Verdana 10 bold",bg='#F5FA89  ').grid(row=0,column=3,padx = 130)
        self.e2=tk.Label(self, text="Bedrooms:",bg='#F5FA89  ').grid(row=1,column=2,padx=30,pady=10,sticky=W+E+N+S )
        self.entry1 = tk.Entry(self)
        #self.button1 = tk.Button(self, text="Get", command=self.on_button1)
        #self.button1.grid(row=1,column=4)
        self.entry1.grid(row=1,column=3,padx = 50,pady=10)
        self.e3=tk.Label(self, text="Bathrooms:",bg='#F5FA89').grid(row=2,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry2 = tk.Entry(self)
        #self.button2 = tk.Button(self, text="Get", command=self.on_button2)
        #self.button2.grid(row=2,column=4)
        self.entry2.grid(row=2,column=3)
        self.e4=tk.Label(self, text="sqft_living",bg='#F5FA89').grid(row=3,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry3 = tk.Entry(self)
        #self.button3 = tk.Button(self, text="Get", command=self.on_button3)
        #self.button3.grid(row=3,column=4)
        self.entry3.grid(row=3,column=3)
        self.e5=tk.Label(self, text="sqft_lot",bg='#F5FA89').grid(row=4,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry4 = tk.Entry(self)
        #self.button4 = tk.Button(self, text="Get", command=self.on_button4)
        #self.button4.grid(row=4,column=4)
        self.entry4.grid(row=4,column=3)
        self.e6=tk.Label(self, text="floors",bg='#F5FA89').grid(row=5,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry5 = tk.Entry(self)
        #self.button5 = tk.Button(self, text="Get", command=self.on_button5)
        #self.button5.grid(row=5,column=4)
        self.entry5.grid(row=5,column=3)
        self.e7=tk.Label(self, text="zipcode",bg='#F5FA89').grid(row=6,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry6 = tk.Entry(self)
        #self.button6 = tk.Button(self, text="Get", command=self.on_button6)
        #self.button6.grid(row=6,column=4)
        self.entry6.grid(row=6,column=3)
        self.e8=tk.Label(self, text="condition",bg='#F5FA89').grid(row=7,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry7 = tk.Entry(self)
        #self.button7 = tk.Button(self, text="Get", command=self.on_button7)
        #self.button7.grid(row=7,column=4)
        self.entry7.grid(row=7,column=3)
        self.e9=tk.Label(self, text="grade",bg='#F5FA89').grid(row=8,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry8 = tk.Entry(self)
        #self.button8 = tk.Button(self, text="Get", command=self.on_button8)
        #self.button8.grid(row=8,column=4)
        self.entry8.grid(row=8,column=3)
        self.e10=tk.Label(self, text="waterfront",bg='#F5FA89').grid(row=9,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry9 = tk.Entry(self)
        #self.button9 = tk.Button(self, text="Get", command=self.on_button9)
        #self.button9.grid(row=9,column=4)
        self.entry9.grid(row=9,column=3)
        self.e11=tk.Label(self, text="view",bg='#F5FA89').grid(row=10,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry10 = tk.Entry(self)
        #self.button10 = tk.Button(self, text="Get", command=self.on_button10)
        #self.button10.grid(row=10,column=4)
        self.entry10.grid(row=10,column=3)
        self.e12=tk.Label(self, text="sqft_above",bg='#F5FA89').grid(row=11,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry11 = tk.Entry(self)
        #self.button11 = tk.Button(self, text="Get", command=self.on_button11)
        #self.button11.grid(row=11,column=4)
        self.entry11.grid(row=11,column=3)
        self.e13=tk.Label(self, text="sqft_basement",bg='#F5FA89').grid(row=12,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry12 = tk.Entry(self)
        #self.button12 = tk.Button(self, text="Get", command=self.on_button12)
        #self.button12.grid(row=12,column=4)
        self.entry12.grid(row=12,column=3)
        self.e14=tk.Label(self, text="yr_built",bg='#F5FA89').grid(row=13,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry13 = tk.Entry(self)
        #self.button13 = tk.Button(self, text="Get", command=self.on_button13)
        #self.button13.grid(row=13,column=4)
        self.entry13.grid(row=13,column=3)
        self.e15=tk.Label(self, text="yr_renovated",bg='#F5FA89').grid(row=14,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry14 = tk.Entry(self)
        #self.button14 = tk.Button(self, text="Get", command=self.on_button14)
        #self.button14.grid(row=14,column=4)
        self.entry14.grid(row=14,column=3)
        self.e16=tk.Label(self, text="lat",bg='#F5FA89').grid(row=15,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry15 = tk.Entry(self)
        #self.button15 = tk.Button(self, text="Get", command=self.on_button15)
        #self.button15.grid(row=15,column=4)
        self.entry15.grid(row=15,column=3)
        self.e17=tk.Label(self, text="long",bg='#F5FA89').grid(row=16,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry16 = tk.Entry(self)
        #self.button16 = tk.Button(self, text="Get", command=self.on_button16)
        #self.button16.grid(row=16,column=4)
        self.entry16.grid(row=16,column=3)
        self.e18=tk.Label(self, text="sqft_living15",bg='#F5FA89').grid(row=17,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry17 = tk.Entry(self)
        #self.button17 = tk.Button(self, text="Get", command=self.on_button17)
        #self.button17.grid(row=17,column=4)
        self.entry17.grid(row=17,column=3)
        self.e19=tk.Label(self, text="sqft_lot15",bg='#F5FA89').grid(row=18,column=2,padx=30,pady=5,sticky=W+E+N+S)
        self.entry18 = tk.Entry(self)
        #self.button18 = tk.Button(self, text="Get", command=self.on_button18)
        #self.button18.grid(row=18,column=4)
        self.entry18.grid(row=18,column=3)
        self.img = tk.PhotoImage(file="C:/Users/utepsilon1/Desktop/enter-now-button_(1).gif",master = self)
        self.buttonk=tk.Button(self,text='Enter',command=self.callb, height = 41, width = 150,image = self.img)
        
        self.buttonk.grid(row=22,column=3,padx=50,pady=5)
        self.mainloop()
    def callb(self):
    	self.on_button1()
    	self.on_button2()
    	self.on_button3()
    	self.on_button4()
    	self.on_button5()
    	self.on_button6()
    	self.on_button7()
    	self.on_button8()
    	self.on_button9()
    	self.on_button10()
    	self.on_button11()
    	self.on_button12()
    	self.on_button13()
    	self.on_button14()
    	self.on_button15()
    	self.on_button16()
    	self.on_button17()
    	self.on_button18()
        self.linear_regg()
    def on_button1(self):
        k=self.entry1.get()
        tem=[]
        tem.append(int(k))
        list1.update({'bedrooms':tem})
    def on_button2(self):
    	k=self.entry2.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'bathrooms':tem})
    def on_button3(self):
    	k=self.entry3.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'sqft_living':tem})
    def on_button4(self):
    	k=self.entry4.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'sqft_lot':tem})
    def on_button5(self):
    	k=self.entry5.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'floors':tem})
    def on_button6(self):
    	k=self.entry6.get()
    	tem=[]
    	tem.append(k)
    	list1.update({'zipcode':tem})
    def on_button7(self):
    	k=self.entry7.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'condition':tem})
    def on_button8(self):
    	k=self.entry8.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'grade':tem})
    def on_button9(self):
    	k=self.entry9.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'waterfront':tem})
    def on_button10(self):
    	k=self.entry10.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'view':tem})
    def on_button11(self):
    	k=self.entry11.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'sqft_above':tem})
    def on_button12(self):
    	k=self.entry12.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'sqft_basement':tem})
    def on_button13(self):
    	k=self.entry13.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'yr_built':tem})
    def on_button14(self):
    	k=self.entry14.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'yr_renovated':tem})
    def on_button15(self):
    	k=self.entry15.get()
    	tem=[]
    	tem.append(float(k))
    	list1.update({'lat':tem})
    def on_button16(self):
    	k=self.entry16.get()
    	tem=[]
    	tem.append(float(k))
    	list1.update({'long':tem})
    def on_button17(self):
    	k=self.entry17.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'sqft_living15':tem})
    def on_button18(self):
    	k=self.entry18.get()
    	tem=[]
    	tem.append(int(k))
    	list1.update({'sqft_lot15':tem})
    def linear_regg(self):
        self.sales = graphlab.SFrame('home_data.gl/')
        #graphlab.canvas.set_target('ipynb')
        #sales.show(view="Scatter Plot", x="sqft_living", y="price")
        #trd,td = df.random_split(.8,seed=0)
        self.advanced_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode',
                            'condition', # condition of house				
                            'grade', # measure of quality of construction				
                            'waterfront', # waterfront property				
                            'view', # type of view				
                            'sqft_above', # square feet above ground				
                            'sqft_basement', # square feet in basement				
                            'yr_built', # the year built				
                            'yr_renovated', # the year renovated				
                            'lat', 'long', # the lat-long of the parcel				
                            'sqft_living15', # average sq.ft. of 15 nearest neighbors 				
                            'sqft_lot15', # average lot size of 15 nearest neighbors 
                            ]
        self.sqft_model = graphlab.linear_regression.create(self.sales,target='price',features=self.advanced_features)
        #print trd['price'].mean()
        #print sqft_model.evaluate(td)
        df1 =graphlab.SFrame(list1)
        self.a=self.sqft_model.predict(df1)
        self.b = 'Price = '+str(self.a)
        tk.Label(self,text =  self.b,bg='#F5FA89').grid(row =25,column =3)


list1 = {}
w = SampleApp()
w.mainloop()