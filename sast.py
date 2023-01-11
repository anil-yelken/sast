#Python Source Code Analysis:https://github.com/anil-yelken/python-source-code-analysis
#PHP Source Code Analysis:https://github.com/anil-yelken/php-source-code-analysis
filename="zafiyetli.php"
with open(filename,"r",encoding='utf-8') as file:
    lines=file.readlines()
line_number=1
linelist=[]
datalist=[]
variablelist=[]
variableCounter=0
for line in lines:
    try:
        if "=" in line:
            charCounter=line.find("=")
            variable = line[:charCounter]
            data = line[charCounter+1:]
            if len(datalist)==0:
                linelist.append(line_number)
                datalist.append(data)
                variablelist.append(variable.replace(" ",""))
                variableCounter+=1
            elif str(variablelist[variableCounter-1].replace(" ","")) in data or (str(variablelist[variableCounter-2].replace(" ","")) in data):
                linelist.append(line_number)
                datalist.append(data)
                variablelist.append(variable)
                variableCounter+=1
    except:
        pass
    line_number+=1
print(linelist)
print(datalist)
print(variablelist)
for index in range(0,line_number+1):
    if filename.endswith("php"):
        try:
            print(linelist[index],"-",datalist[index])
            if ("mysql_query" in datalist[index]) or ("query" in datalist[index]):
                print("Possible SQL Injection")
            elif "move_uploaded_file" in datalist[index]:
                print("Possible File Upload")
            elif "xml_parse" in datalist[index]:
                print("Possible XML Injection")
            elif ("exec" in datalist[index]) or ("shell_exec" in datalist[index]):
                print("Possible Command injection")
            elif ("echo" in datalist[index]) or ("var_dump" in datalist[index]):
                print("Possible XSS")
            elif ("include" in datalist[index]):
                print("Possible File Inclusion")
            elif ("eval" in datalist[index]):
                print("Possible Code Injection")
            elif ("!--#echo var" in datalist[index]):
                print("Possible SSI")
            elif ("unserialize" in datalist[index]):
                print("Possible Deserilization")
            elif ("Twig_Autoloader" in datalist[index]) or ("Twig_Loader_String" in datalist[index]) or ("Twig_Environment" in datalist[index]):
                print("Possible SSTI")
        except:
            pass
    elif filename.endswith("py"):
        try:
            print(linelist[index],"-",datalist[index])
            if (".execute" in datalist[index]):
                print("Possible SQL Injection")
            elif "render_template_string" in datalist[index]:
                print("Possible SSTI")
            elif "subprocess.check_output" in datalist[index]:
                print("Possible Command Injection")
            elif ("pickle.loads" in datalist[index]):
                print("Possible Deserilization")
            elif ("secure_filename" in datalist[index]) or (".save(os.path.join" in datalist[index]):
                print("Possible File Upload")
        except:
            pass
