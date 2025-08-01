import pandas as pd
import json
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox

class document():
    def xlwrite(self):
        # Create the application
        app = QApplication(sys.argv)
        # Create a temporary widget (needed for dialogs)
        widget = QWidget()
        widget.setWindowTitle("Input Example")
        # Show input dialog
        folder_path, ok = QInputDialog.getText(widget, 'Input Dialog', "Enter folder path: ")
        # Show message box based on input
        if ok and folder_path:
            pass
        else:
            QMessageBox.warning(widget, 'No Input', 'You didn\'t enter folder path')


        dict={}
        #jsonpath=folder_path
        jsonfile=os.listdir(folder_path)
        for j in range (0,len(jsonfile)):
            if jsonfile[j].endswith('.json'):
                path= fr"{folder_path}\{jsonfile[j]}"
                with open (path, "r") as file:
                    data=json.load(file)
                    if j==0:
                        dict["Job_ID"]=[data["CartItemOption"][0]["Job_ID"]]
                    else:
                        dict["Job_ID"].append(data["CartItemOption"][0]["Job_ID"])

                    for i in range(0, len(data["CartItemOption"])):
                        if j==0: 
                            dict[data["CartItemOption"][i]["CharacteristicName"]]=[data["CartItemOption"][i]["CharacteristicValue"]]
                        else:
                            dict[data["CartItemOption"][i]["CharacteristicName"]].append(data["CartItemOption"][i]["CharacteristicValue"])
                file.close()    
        df=pd.DataFrame(dict)    
        df.to_excel(rf"{folder_path}\Testcases.xlsx",index=0)
        # Exit the application
        sys.exit()