return ">> You will die today . . ."        
return ">> You will die tomorrow . . ."        
return ">> You will die the day after tomorrow . . ."        
return ">> ERR . . . Unexpected error in prediction.\n------------------------------------------"        
return f">> Your death date: {death.strftime('%m.%d.%Y')}"        



f.write("============== FUTURE DEATH ==============\n")        
f.write("------------------------------------------\n")        
f.write(f">> Name: {name}\n")        
f.write(f">> Birth: {birth_str}\n")        
f.write("------------------------------------------\n")        
f.write(result + "\n")        
f.write("------------------------------------------\n")        
f.write(f">> Record created at {datetime.now().strftime('%H:%M:%S %d.%m.%Y')}\n")        
f.write("------------------------------------------\n")        
f.write("==========================================\n")




_print("=========== FUTURE DEATH SYSTEM ===========")
slow_print("-------------------------------------------")
name = input(">> Input your name: ").strip()
slow_print("-------------------------------------------")
slow_print(">> ERR . . . Name cannot be empty.")
slow_print("-------------------------------------------")
name = input(">> Input your name: ").strip()



birth_input = input(">> Input birth date (MM.DD.YYYY): ").strip()



slow_print("-------------------------------------------")
slow_print(">> ERR . . . Invalid date or wrong format.\n>> Example: 4.13.1997 . . .")
slow_print("------------------------------------------")
slow_print(">> ERR . . . Birth date cannot be in the future.")
slow_print("------------------------------------------")




slow_print("-------------------------------------------")
slow_print(">> Processing . . .")
slow_print("-------------------------------------------")
slow_print(f">> Name: {name}")
slow_print("-------------------------------------------")
slow_print(f">> Record saved to '{saved}'")
slow_print("-------------------------------------------")
slow_print("             --- DEAD END ---              ")
slow_print("-------------------------------------------")
slow_print("===========================================")