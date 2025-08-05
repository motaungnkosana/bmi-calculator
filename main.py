from tkinter import *
from tkinter import messagebox

# Root window setup
root = Tk()
root.title('BMI Calculator')
root.geometry('300x220')
root.config(bg='#686e70')

# Main frame
frame = Frame(root, padx=10, pady=10, bg='#686e70')
frame.pack(expand=True)

# Height
Label(frame, text="Enter your height (cm):", bg='#686e70', fg='white').grid(row=0, column=0, sticky=W, pady=5)
txtHeight = Entry(frame)
txtHeight.grid(row=0, column=1, pady=5)

# Weight
Label(frame, text="Enter your weight (kg):", bg='#686e70', fg='white').grid(row=1, column=0, sticky=W, pady=5)
txtWeight = Entry(frame)
txtWeight.grid(row=1, column=1, pady=5)

# Functions
def calcBMI():
    try:
        weight = float(txtWeight.get())
        height = float(txtHeight.get())
        if height <= 0 or weight <= 0:
            raise ValueError
        height /= 100  # convert cm to meters
        bmi = round(weight / (height * height), 1)
        showBMIResult(bmi)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for height and weight.")

def showBMIResult(bmi):
    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        category = 'Normal Weight'
    elif 25.0 <= bmi <= 29.9:
        category = 'Overweight'
    else:
        category = 'Obese'

    messagebox.showinfo('BMI Result', f'Your BMI is {bmi}\nCategory: {category}')

def reset():
    txtHeight.delete(0, END)
    txtWeight.delete(0, END)

def exitApp():
    root.destroy()

# Buttons
buttonFrame = Frame(frame, bg='#686e70')
buttonFrame.grid(row=2, columnspan=2, pady=15)

Button(buttonFrame, text='Calculate', command=calcBMI, width=10).grid(row=0, column=0, padx=5)
Button(buttonFrame, text='Clear', command=reset, width=10).grid(row=0, column=1, padx=5)
Button(buttonFrame, text='Exit', command=exitApp, width=10).grid(row=0, column=2, padx=5)

# Start the app
root.mainloop()
