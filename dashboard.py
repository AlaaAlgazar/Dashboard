import customtkinter as ctk
from matplotlib import pyplot,figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ************************************
# some data to show

sales_data={
    "product A":100,
    "product B":200,
    "product C":300,
    "product D":400,
    "product E":500,
}

inventory_data={
    "product A":150,
    "product B":75,
    "product C":100,
    "product D":125,
    "product E":150,
}

product_data={
    "A":10,
    "B":40,
    "C":30,
    "D":20,
    "E":50,
}
inventory_month_data={
    "jan":200,
    "feb":300,
    "mar":800,
    "apr":1300,
    "may":350,
    "jun":600,
    "jul":900,
    "agu":700,
    "sep":900,
    "oct":1000,
    "nov":300,
    "dec":450,

}

sales_year_data={
    2018:5000,
    2019:17500,
    2020:10000,
    2021:7500,
    2022:15000
}

# **********************************

pyplot.rcParams['axes.prop_cycle']=pyplot.cycler(color=["#125","#298","#152","#175","#179"])


# first chart
chart1,axes = pyplot.subplots()
axes.set_title("Sales by product")
axes.bar(sales_data.keys(),sales_data.values())
axes.set_xlabel("Product")
axes.set_ylabel("Sales")
# pyplot.show()





chart2,axes2=pyplot.subplots()
axes2.set_title("Inventory by product")
axes2.barh(list(inventory_data.keys()),list(inventory_data.values()))
axes2.set_xlabel("Inventory")
axes2.set_ylabel("product")
# pyplot.show()


chart3 ,axes3=pyplot.subplots()
axes3.set_title("Product breakdown")
axes3.pie(product_data.values(),labels=product_data.keys(),autopct="%1.3f%%")
# pyplot.show()

chart4, axes4=pyplot.subplots()
axes4.set_title("Sales by year")
axes4.plot(list(sales_year_data.keys()),list(sales_year_data.values()))
axes4.set_xlabel("Year")
axes4.set_ylabel("Sales")
# pyplot.show()


chart5, axes5=pyplot.subplots()
axes5.fill_between(inventory_month_data.keys(),inventory_month_data.values())
axes5.set_title("Inventory by month")
axes5.set_xlabel("Month")
axes5.set_ylabel("Inventory")
pyplot.show()

window=ctk.CTk()
window.title("Dashboards")
window.state("zoomed")
window.state("withdraw")
main_frame=ctk.CTkFrame(window,width=window.winfo_screenwidth())
main_frame.grid(row=0,column=0)
top_frame=ctk.CTkFrame(main_frame,width=window.winfo_screenwidth())
top_frame.grid(row=0,column=0,sticky="new")

bottom_frame=ctk.CTkFrame(main_frame,width=window.winfo_screenwidth())
bottom_frame.grid(row=1,column=0,sticky="new")

canvas1=FigureCanvasTkAgg(chart1,top_frame)
canvas1.draw()
canvas1.get_tk_widget().grid(row=0,column=1)


canvas2=FigureCanvasTkAgg(chart2,top_frame)
canvas2.draw()
canvas2.get_tk_widget().grid(row=0,column=2)


canvas3=FigureCanvasTkAgg(chart3,top_frame)
canvas3.draw()
canvas3.get_tk_widget().grid(row=0,column=3)


canvas4=FigureCanvasTkAgg(chart4,bottom_frame)
canvas4.draw()
canvas4.get_tk_widget().grid(row=0,column=0)


canvas5=FigureCanvasTkAgg(chart5,bottom_frame)
canvas5.draw()
canvas5.get_tk_widget().grid(row=0,column=1)



fig=pyplot.figure()
fig.set_figwidth(1)
fig.set_figheight(2)





















window.mainloop()