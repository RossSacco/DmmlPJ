import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import pickle
from ttkbootstrap import Style

# Carica la pipeline del modello (preprocessing + classificatore)
with open('diabetes_classifier.pkl', 'rb') as f:
    pipeline = pickle.load(f)

def predict():
    try:
        # Recupera i valori dai campi
        genhlth = genhlth_options[genhlth_var.get()]
        physhlth_raw = float(entry_phys_hlth.get()) 
        physhlth = physhlth_raw if (physhlth_raw <= 31 and physhlth_raw > 0) else pd.Nan  # Assicurati che sia >= 0
        persdoc2 = int(var_perdoc.get())
        medcost = int(var_medcost.get())
        checkup1 = checkup_var_options[checkup_var.get()]
        bphigh = int(var_bphigh.get())
        cholchk = cholchk_var_options[cholchk_var.get()]
        toldhi = int(var_toldhi.get())
        cvdinfr = int(var_cvdinfr4.get())
        cvdcrhda = int(var_cvdcrhda4.get())
        cvdstrk3 = int(var_cvdstrk3.get())
        asthma3 = int(var_asthma.get())
        chcscnr = int(var_skincancer.get())
        chocncr = int(var_cancer.get())
        chccopd1 = int(var_chcc.get())
        havart3 = int(var_havart3.get())
        addepev2 = int(var_addepev2.get())
        chckidny = int(var_chckidny.get())
        educa = educa_var_options[educa_var.get()]

        input_data = pd.DataFrame([{
            'GENHLTH': genhlth,
            'PHYSHLTH': physhlth,
            'PERSDOC2': persdoc2,
            'MEDCOST': medcost,
            'CHECKUP1': checkup1,
            'BPHIGH': bphigh,
            'CHOLCHK': cholchk,
            'TOLDHI': toldhi,
            'CVDINFR4': cvdinfr,
            'CVDCRHDA4': cvdcrhda,
            'CVDSTRK3': cvdstrk3,
            'ASTHMA3': asthma3,
            'CHCSCNCR': chcscnr,
            'CHCOCNCR': chocncr,
            'CHCCOPD1': chccopd1,
            'HAVARTH3': havart3,
            'ADDEPEV2': addepev2,
            'CHCKIDNY': chckidny,
            'EDUCA': educa,
            
            
        }])

        prediction = pipeline.predict(input_data)[0]
        classes = {0: "No Diabetes", 1: "Diabetes"}
        messagebox.showinfo("Risultato", f"Classificazione: {classes[prediction]}")

    except Exception as e:
        messagebox.showerror("Errore", f"Errore: {e}")

# Inizializza finestra
root = tk.Tk()
style = Style(theme='darkly')
root.title("🩺 Classificatore Rischio Diabete")
root.geometry("600x600")

frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

def add_input_field(parent, label, default=""):
    row = ttk.Frame(parent)
    row.pack(fill=tk.X, pady=5)
    ttk.Label(row, text=label, width=25, anchor='w').pack(side=tk.LEFT)
    entry = ttk.Entry(row)
    entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
    entry.insert(0, default)
    return entry

def add_dropdown(parent, label, var, options):
    row = ttk.Frame(parent)
    row.pack(fill=tk.X, pady=5)
    ttk.Label(row, text=label, width=25, anchor='w').pack(side=tk.LEFT)
    menu = ttk.Combobox(row, textvariable=var, values=options, state='readonly')
    menu.pack(side=tk.RIGHT, expand=True, fill=tk.X)
    menu.set(options[0])
    return menu

# Campi di input

entry_phys_hlth = add_input_field(frame, "Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?", "5")


# Campi con drop

genhlth_var = tk.StringVar()
genhlth_options = {
    "Excellent": 1,
    "Very good": 2,
    "Good": 3,
    "Fair": 4,
    "Poor": 5
}
add_dropdown(frame, "General Health:", genhlth_var, list(genhlth_options.keys()))
genhlth_var.set("Good")  # valore predefinito visibile

checkup_var = tk.StringVar()
checkup_var_options = {
    "Within past year": 1,
    "Within past 2 year": 2,
    "Within past 5 year": 3,
    "5 or more year ago": 4,
    "Never": 8
}
add_dropdown(frame, "About how long has it been since you last visited a doctor for a routine checkup? ", checkup_var, list(checkup_var_options.keys()))
checkup_var.set("Never")  # valore predefinito visibile

cholchk_var = tk.StringVar()
cholchk_var_options = {
    "Within past year": 1,
    "Within past 2 year": 2,
    "Within past 5 year": 3,
    "5 or more year ago": 4
}
add_dropdown(frame, "About how long has it been since you last had your blood cholesterol checked? ", cholchk_var, list(cholchk_var_options.keys()))
cholchk_var.set("Whitin past year")  # valore predefinito visibile

marital_var = tk.StringVar()
marital_var_options = {
    "Married": 1,
    "Divorced": 2,
    "Widowed": 3,
    "Other": 4,
    "Never Married": 5
    }
add_dropdown(frame, "Which is your marital status?", marital_var, list(marital_var_options.keys()))
marital_var.set("Whitin past year")  # valore predefinito visibile

educa_var = tk.StringVar()
educa_var_options = {
    "College graduate": 1,
    "Some College or technical school": 2,
    "high school graduate": 3,
    "Some high school": 4,
    "Elementary": 5,
    "Never attended school or only kindergarten": 6
    }
add_dropdown(frame, "What is the highest grade or year of school you completed?", educa_var, list(educa_var_options.keys()))
educa_var.set("Whitin past year")  # valore predefinito visibile


# Campi binari

var_perdoc = tk.IntVar()
ttk.Checkbutton(frame, text="Do you have a personal doctor?", variable=var_perdoc).pack(pady=5)

var_medcost = tk.IntVar()
ttk.Checkbutton(frame, text="Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?", variable=var_medcost).pack(pady=5)

var_bphigh = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have high blood pressure?", variable=var_bphigh).pack(pady=5)

var_toldhi = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have high cholesterol?", variable=var_toldhi).pack(pady=5)

var_cvdinfr4 = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you had a heart attack?", variable=var_cvdinfr4).pack(pady=5)

var_cvdcrhda4 = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you had coronary heart disease?", variable=var_cvdcrhda4).pack(pady=5)

var_cvdstrk3 = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you had a stroke?", variable=var_cvdstrk3).pack(pady=5)

var_asthma = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have asthma?", variable=var_asthma).pack(pady=5)

var_skincancer = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have skin cancer?", variable=var_skincancer).pack(pady=5)

var_cancer = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have any type of cancer?", variable=var_cancer).pack(pady=5)

var_chcc = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have chronic obstructive pulmonary disease (COPD)?", variable=var_chcc).pack(pady=5)

var_havart3 = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have arthritis?", variable=var_havart3).pack(pady=5)

var_addepev2 = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have depression?", variable=var_addepev2).pack(pady=5)

var_chckidny = tk.IntVar()
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have kidney disease?", variable=var_chckidny).pack(pady=5)

# Bottone di predizione
btn = ttk.Button(frame, text="Classifica", command=predict, style="success.Outline.TButton")
btn.pack(pady=20)

# Avvia l'app
root.mainloop()
