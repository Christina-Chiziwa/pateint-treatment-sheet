
import psycopg2

# Connect to the database
conn = psycopg2.connect(database="patient_treatment_sheet", user="postgres", password="christina@53", host="localhost", port="5432")
cur = conn.cursor()

# Create the table to store the user's data
cur.execute("CREATE TABLE IF NOT EXISTS patient_sheets (id serial PRIMARY KEY, name varchar(50),Age integer,sex varchar(50), email varchar(50),address varchar(50),phone_number integer,past_illness varchar(50),past_surgery varchar(50),hospitilisation varchar(50),Chronic_conditions varchar(50),respiratory_rate integer,heartrate integer,oxygen_saturation integer,systolic_bp integer, diastolic_bp integer, temperature float,current_medication varchar(50),current_procedures varchar(50),dosage varchar(50),frequencies integer,medication_allergies varchar(50),food_allergies varchar(50),other_allergies varchar(50),blood_test varchar(50),imaging_studies varchar(50));")

# Retrieve data from the form and insert it into the database
name = input("Enter your name: ")
Age=input("enter your age:")
sex=input("enter your sex:")
email = input("Enter your email: ")
address=input("enter your location:")
phone_number=input("enter your phone_number:")
past_illness=input("enter your past_illness:")
past_surgery=input("enter your past_surgery:")
hospitilisation=input("enter your hospitilisation :")
chronic_conditions=input("enter your chronic_conditions :")
respiratory_rate =input("enter your respiratory_rate :")
heatrate=input("enter your heatrate :")
oxygen_saturation=input("enter your oxygen_saturation:")
systolic_bp=input("enter your Systolic_bp:")
diastolic_bp=input("enter your diastolic_bp:")
temperature=input("enter your temperature:")
current_medication=input("enter your current_medication:")
current_procedures=input("enter your current_procedures:")
dosage=input("enter your dosage:")
frequencies=input("enter your frequencies:")
medication_allergies=input("enter your medication_allergies:")
food_allergies=input("enter your food_allergies:")
other_allergies=input("enter your Other_allergies:")
blood_test=input("enter your blood_test:")
imaging_studies=input("enter your imaging_studies:")

cur.execute("INSERT INTO patient_sheets (name,Age,sex, email,address,phone_number,past_illness,past_surgery,hospitilisation,chronic_conditions,respiratory_rate,heatrate,oxygen_saturation,systolic_bp,diastolic_bp,temperature,current_medication,current_procedures,dosage,frequencies,medication_allergies,food_allergies,other_allergies,blood_test,imaging_studies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (name,Age,sex, email,address,phone_number,past_illness,past_surgery,hospitilisation,chronic_conditions,respiratory_rate,heatrate,oxygen_saturation,systolic_bp,diastolic_bp,temperature,current_medication,current_procedures,dosage,frequencies,medication_allergies,food_allergies,other_allergies,blood_test,imaging_studies))
conn.commit()

# Close the database connection
cur.close()
conn.close()