from datetime import datetime,timedelta
import random
def generator() :
    try :
        initial_range = 1
        
        final_number = 100
        random_number = random.randint(initial_range,final_number)
        
        final_spin = 25
        random_spin = random.randint(initial_range, final_spin)
        
        final_hours = 3
        random_hours = random.randint(initial_range, final_hours)
        
        current_date = datetime.now()
        date_hours = current_date.strftime("%d/%m/%Y %H:%M")
        
        final_hours = timedelta(hours=random_hours)
        final_date = current_date + final_hours
        format_final_hours = final_date.strftime("%d/%m/%Y %H:%M")
        
        large_text = (
                    f"🐯 tigrinho! 🐯\n\n"
                    "maior sinal do mundo! 🌟\n\n"
                    f"⏰Entrada:⏰ {date_hours}\n"
                    f"💸valor:💸 🔥 R${random_number},00\n"
                    f"1. roletadas {random_spin}.\n"
                    f"2. Aposta válida até {format_final_hours}.\n"
                    "Vamos tornar isso épico! 🚀")
    
        return large_text
    except TypeError:
        return "error message"