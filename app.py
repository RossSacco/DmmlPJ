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
        physhlth = physhlth_raw if (physhlth_raw <= 31 and physhlth_raw > 0) else pd.NA  # Assicurati che sia >= 0
        hlthpln1 = int(var_hlthpln1.get())
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
        marital = marital_var_options[marital_var.get()]
        educa = educa_var_options[educa_var.get()]
        veteran = int(var_veteran.get())
        employ = emply_var_options[emply_var.get()]
        children = int(entry_children.get())
        income2 = income2_options[income2_var.get()]
        internet = int(var_internet.get())
        qlactlm2 = int(var_qlactlm2.get())
        useequip = int(var_useequip.get())
        blind = int(var_blind.get())
        decide = int(var_decide.get())
        diffwalk = int(var_diffwalk.get())
        diffdress = int(var_diffdress.get())
        diffalon = int(var_diffalon.get())
        smoke100 = int(var_smoke100.get())
        alcday5 = float(entry_alcday_week.get())
        fruitju1 = float(entry_fruitju1.get())
        fruit1 = float(entry_fruit.get())
        beans = float(entry_beans.get())
        fvgreen = float(entry_fvgreen.get())
        fvorang = float(entry_fvorang.get())
        vegetab1 = float(entry_vegetab1.get())
        exerany2 = int(var_exerany2.get())
        strength = float(entry_stregth.get())
        flushot6 = int(var_flushot6.get())
        pneuvac3 = int(var_pneuvac3.get())
        hivtst6 = int(var_hivtst6.get())
        race = race_var_options[race_var.get()]
        age = age_options[age_var.get()]
        bmi5cat = bmi5cat_options[bmi5cat_var.get()]
        pacat = pacat_options[pacat_var.get()]

        input_data = pd.DataFrame([{
            'GENHLTH': genhlth,
            'PHYSHLTH': physhlth,
            'HLTHPLN1': hlthpln1,
            'PERSDOC2': persdoc2,
            'MEDCOST': medcost,
            'CHECKUP1': checkup1,
            'BPHIGH4': bphigh,
            'CHOLCHK': cholchk,
            'TOLDHI2': toldhi,
            'CVDINFR4': cvdinfr,
            'CVDCRHD4': cvdcrhda,
            'CVDSTRK3': cvdstrk3,
            'ASTHMA3': asthma3,
            'CHCSCNCR': chcscnr,
            'CHCOCNCR': chocncr,
            'CHCCOPD1': chccopd1,
            'HAVARTH3': havart3,
            'ADDEPEV2': addepev2,
            'CHCKIDNY': chckidny,
            'MARITAL': marital,
            'EDUCA': educa,
            'VETERAN3': veteran,
            'EMPLOY1': employ,
            'CHILDREN': children,
            'INCOME2': income2,
            'INTERNET': internet,
            'QLACTLM2': qlactlm2,
            'USEEQUIP': useequip,
            'BLIND': blind,
            'DECIDE': decide,
            'DIFFWALK': diffwalk,
            'DIFFDRES': diffdress,
            'DIFFALON': diffalon,
            'SMOKE100': smoke100,
            'ALCDAY5': alcday5,
            'FRUITJU1': fruitju1,
            'FRUIT1': fruit1,
            'FVBEANS': beans,
            'FVGREEN': fvgreen,
            'FVORANG': fvorang,
            'VEGETAB1': vegetab1,
            'EXERANY2': exerany2,
            'STRENGTH': strength,
            'FLUSHOT6': flushot6,
            'PNEUVAC3': pneuvac3,
            'HIVTST6': hivtst6,
            '_RACE': race, 
            '_AGE_G': age,
            '_BMI5CAT': bmi5cat,
            '_PACAT1': pacat
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
root.geometry("1200x700")

# Frame con scrollbar
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

frame = scrollable_frame

def add_input_field(parent, label, default=""):
    row = ttk.Frame(parent)
    row.pack(fill=tk.X, pady=5)
    ttk.Label(row, text=label, anchor='w', wraplength=690, justify='center').pack(fill=tk.X)
    entry = ttk.Entry(row)
    entry.pack(fill=tk.X)
    entry.insert(0, default)
    return entry

def add_dropdown(parent, label, var, options):
    row = ttk.Frame(parent)
    row.pack(fill=tk.X, pady=5)
    ttk.Label(row, text=label, anchor='w', wraplength=690, justify='center').pack(fill=tk.X)
    menu = ttk.Combobox(row, textvariable=var, values=options, state='readonly')
    menu.pack(fill=tk.X)
    menu.configure(font=("Helvetica", 10))
    return menu


# Campi di input

entry_phys_hlth = add_input_field(frame, "- Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?", "5")
entry_children = add_input_field(frame, "- How many children less than 18 years of age live in your household?", "0")
entry_alcday_week = add_input_field(frame, "- On how many days in a week did you have at least one drink of any alcoholic beverage?", "0")
entry_fruitju1 = add_input_field(frame, "- How many times per month do you drink fruit juice?", "0")
entry_fruit = add_input_field(frame, "- How many times per month, not counting juice, do you eat fruit?", "0")
entry_beans = add_input_field(frame, "- How many times per month do you eat beans?", "0")
entry_fvgreen = add_input_field(frame, "- How many times per month do you eat green vegetables?", "0")
entry_fvorang = add_input_field(frame, "- How many times per month do you eat orange vegetables?", "0")
entry_vegetab1 = add_input_field(frame, "- How many times per month do you eat other vegetables?", "0")
entry_stregth = add_input_field(frame, "- How many times per month do you do strength training?", "0")

# Campi con drop

genhlth_var = tk.StringVar()
genhlth_options = {
    "Excellent": 1,
    "Very good": 2,
    "Good": 3,
    "Fair": 4,
    "Poor": 5
}
add_dropdown(frame, "- General Health:", genhlth_var, list(genhlth_options.keys()))
genhlth_var.set("Good")  # valore predefinito visibile

checkup_var = tk.StringVar()
checkup_var_options = {
    "Within past year": 1,
    "Within past 2 year": 2,
    "Within past 5 year": 3,
    "5 or more year ago": 4,
    "Never": 8
}
add_dropdown(frame, "- About how long has it been since you last visited a doctor for a routine checkup? ", checkup_var, list(checkup_var_options.keys()))
checkup_var.set("Never")  # valore predefinito visibile

cholchk_var = tk.StringVar()
cholchk_var_options = {
    "Within past year": 1,
    "Within past 2 year": 2,
    "Within past 5 year": 3,
    "5 or more year ago": 4
}
add_dropdown(frame, "- About how long has it been since you last had your blood cholesterol checked? ", cholchk_var, list(cholchk_var_options.keys()))
cholchk_var.set("Within past year")  # valore predefinito visibile

marital_var = tk.StringVar()
marital_var_options = {
    "Married": 1,
    "Divorced": 2,
    "Widowed": 3,
    "Other": 4,
    "Never Married": 5
    }
add_dropdown(frame, "- Which is your marital status?", marital_var, list(marital_var_options.keys()))
marital_var.set("Married")  # valore predefinito visibile

educa_var = tk.StringVar()
educa_var_options = {
    "College graduate": 1,
    "Some College or technical school": 2,
    "high school graduate": 3,
    "Some high school": 4,
    "Elementary": 5,
    "Never attended school or only kindergarten": 6
    }
add_dropdown(frame, "- What is the highest grade or year of school you completed?", educa_var, list(educa_var_options.keys()))
educa_var.set("Elementary")  # valore predefinito visibile

emply_var = tk.StringVar()
emply_var_options = {
    "Employed for wages": 1,
    "Self-employed": 2,
    "Other": 3,
    "Homemaker": 5,
    "Retired": 7,
    "Unable to work": 8
}
add_dropdown(frame, "- Which of the following best describes you?", emply_var, list(emply_var_options.keys()))
emply_var.set("Employed for wages")  # valore predefinito visibile

income2_var = tk.StringVar()
income2_options = {
    "Less than $10,000": 1,
    "Less than $15,000": 2,
    "Less than $20,000": 3,
    "Less than $25,000": 4,
    "Less than $35,000": 5,
    "Less than $50,000": 6,
    "Less than $75,000": 7,
    "$75,000 or more": 8
}   
add_dropdown(frame, "- What is your annual household income?", income2_var, list(income2_options.keys()))
income2_var.set("Less than $10,000")  # valore predefinito visibile

race_var = tk.StringVar()
race_var_options = {
    "White": 1,
    "Black or African American": 2,
    "other": 3,
    "Hispanic": 4
}
add_dropdown(frame, "- What is your ethnicity?", race_var, list(race_var_options.keys()))
race_var.set("White")  # valore predefinito visibile


age_var = tk.StringVar()
age_options = {
    "18-24": 1,
    "25-34": 2,
    "35-44": 3,
    "45-54": 4,
    "55-64": 5,
    "65 or older": 6
}
add_dropdown(frame, "- What is your age?", age_var, list(age_options.keys()))
age_var.set("18-24")  # valore predefinito visibile

bmi5cat_var = tk.StringVar()
bmi5cat_options = {
    "Underweight": 1,
    "Normal weight": 2,
    "Overweight": 3,
    "Obese": 4
}
add_dropdown(frame, "- What is your BMI category?", bmi5cat_var, list(bmi5cat_options.keys()))
bmi5cat_var.set("Normal weight")  # valore predefinito visibile

pacat_var = tk.StringVar()
pacat_options = {
    "Highly active": 1,
    "active": 2,
    "insufficiently active": 3,
    "inactive": 4
}
add_dropdown(frame, "- How would you describe your physical activity level?", pacat_var, list(pacat_options.keys()))
pacat_var.set("Highly active")  # valore predefinito visibile

# Campi binari

var_hlthpln1 = tk.IntVar()
row_hlthpln1 = ttk.Frame(frame)
row_hlthpln1.pack(fill=tk.X, pady=5)
ttk.Checkbutton(frame, text="Do you have any kind of health care coverage, including health insurance, prepaid plans such as Health Maintenance Organizations (HMOs), or government plans such as Medicare?", variable=var_hlthpln1).pack(pady=5)

var_perdoc = tk.IntVar()
row_perdoc = ttk.Frame(frame)
row_perdoc.pack(fill=tk.X, pady=5)
ttk.Checkbutton(frame, text="Do you have a personal doctor?", variable=var_perdoc).pack(pady=5)

var_medcost = tk.IntVar()
row_medcost = ttk.Frame(frame)
row_medcost.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?", variable=var_medcost).pack(pady=5)

var_bphigh = tk.IntVar()
row_bphigh = ttk.Frame(frame)
row_bphigh.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have high blood pressure?", variable=var_bphigh).pack(pady=5)

var_toldhi = tk.IntVar()
row_toldhi = ttk.Frame(frame)
row_toldhi.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have high cholesterol?", variable=var_toldhi).pack(pady=5)

var_cvdinfr4 = tk.IntVar()
row_cvdinfr4 = ttk.Frame(frame)
row_cvdinfr4.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you had a heart attack?", variable=var_cvdinfr4).pack(pady=5)

var_cvdcrhda4 = tk.IntVar()
row_cvdcrhda4 = ttk.Frame(frame)
row_cvdcrhda4.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you had coronary heart disease?", variable=var_cvdcrhda4).pack(pady=5)

var_cvdstrk3 = tk.IntVar()
row_cvdstrk3 = ttk.Frame(frame)
row_cvdstrk3.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you had a stroke?", variable=var_cvdstrk3).pack(pady=5)

var_asthma = tk.IntVar()
row_asthma = ttk.Frame(frame)
row_asthma.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have asthma?", variable=var_asthma).pack(pady=5)

var_skincancer = tk.IntVar()
row_skincancer = ttk.Frame(frame)
row_skincancer.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have skin cancer?", variable=var_skincancer).pack(pady=5)

var_cancer = tk.IntVar()
row_cancer = ttk.Frame(frame)
row_cancer.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have any type of cancer?", variable=var_cancer).pack(pady=5)

var_chcc = tk.IntVar()
row_chcc = ttk.Frame(frame)
row_chcc.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have chronic obstructive pulmonary disease (COPD)?", variable=var_chcc).pack(pady=5)

var_havart3 = tk.IntVar()
row_havart3 = ttk.Frame(frame)
row_havart3.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have arthritis?", variable=var_havart3).pack(pady=5)

var_addepev2 = tk.IntVar()
row_addepev2 = ttk.Frame(frame)
row_addepev2.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have depression?", variable=var_addepev2).pack(pady=5)

var_chckidny = tk.IntVar()
row_chckidny = ttk.Frame(frame)
row_chckidny.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been told by a doctor that you have kidney disease?", variable=var_chckidny).pack(pady=5)

var_veteran = tk.IntVar()
row_veteran = ttk.Frame(frame)
row_veteran.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Are you a veteran?", variable=var_veteran).pack(pady=5)

var_internet = tk.IntVar()
row_internet = ttk.Frame(frame)
row_internet.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Do you have access to the internet?", variable=var_internet).pack(pady=5)

var_qlactlm2 = tk.IntVar()
row_qlactlm2 = ttk.Frame(frame)
row_qlactlm2.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Are you limited in any way in any activities because of physical, mental, or emotional problems?", variable=var_qlactlm2).pack(pady=5)

var_useequip = tk.IntVar()
row_useequip = ttk.Frame(frame)
row_useequip.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Do you use any special equipment to help you with daily activities?", variable=var_useequip).pack(pady=5)

var_blind = tk.IntVar()
row_blind = ttk.Frame(frame)
row_blind.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Are you blind or do you have serious difficulty seeing, even when wearing glasses?", variable=var_blind).pack(pady=5)

var_decide = tk.IntVar()
row_decide = ttk.Frame(frame)
row_decide.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions?", variable=var_decide).pack(pady=5)

var_diffwalk = tk.IntVar()
row_diffwalk = ttk.Frame(frame)
row_diffwalk.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Do you have serious difficulty walking or climbing stairs?", variable=var_diffwalk).pack(pady=5)

var_diffdress = tk.IntVar()
row_diffdress = ttk.Frame(frame)
row_diffdress.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Do you have difficulty dressing or bathing?", variable=var_diffdress).pack(pady=5)

var_diffalon = tk.IntVar()
row_diffalon = ttk.Frame(frame)
row_diffalon.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Do you have difficulty doing errands alone such as visiting a doctor's office or shopping?", variable=var_diffalon).pack(pady=5)

var_smoke100 = tk.IntVar()
row_smoke100 = ttk.Frame(frame)
row_smoke100.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you smoked at least 100 cigarettes in your entire life?", variable=var_smoke100).pack(pady=5)

var_exerany2 = tk.IntVar()
row_exerany2 = ttk.Frame(frame)
row_exerany2.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="During the past month, other than your regular job, did you participate in any physical activities or exercises ", variable=var_exerany2).pack(pady=5)

var_flushot6 = tk.IntVar()
row_flushot6 = ttk.Frame(frame)
row_flushot6.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you had a flu shot or a flu vaccine in the past 12 months?", variable=var_flushot6).pack(pady=5)

var_pneuvac3 = tk.IntVar()
row_pneuvac3 = ttk.Frame(frame)
row_pneuvac3.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever had a pneumonia vaccine?", variable=var_pneuvac3).pack(pady=5)

var_hivtst6 = tk.IntVar()
row_hivtst6 = ttk.Frame(frame)
row_hivtst6.pack(fill=tk.X, pady=5, padx = 20)
ttk.Checkbutton(frame, text="Have you ever been tested for HIV?", variable=var_hivtst6).pack(pady=5)

# Bottone di predizione
btn = ttk.Button(frame, text="Classifica", command=predict, style="success.Outline.TButton")
btn.pack(pady=20)

# Avvia l'app
root.mainloop()
