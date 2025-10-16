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




_print("=========== FUTURE DEATH SYSTEM ===========")    slow
_print("-------------------------------------------")    name
 = input(">> Input your name: ").strip()    slow
_print("-------------------------------------------")    slow
_print(">> ERR . . . Name cannot be empty.")    slow
_print("-------------------------------------------")    name
 = input(">> Input your name: ").strip()



birth_input = input(">> Input birth date (MM.DD.YYYY): ").strip()       