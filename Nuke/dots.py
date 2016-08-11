'''
Created on 29/01/2013

@author: carlosfelgarcia
'''
import nuke

dots = 0
realdots=0
attach = False
Minput = False
select = False
        
#Create a panel
p = nuke.Panel('Dots organizer')
op = ["Selection "]
for node in nuke.allNodes():
    if node.Class() == "Dot":
        if node.inputs() == 1:
                cl = node.input(0).Class()
                if cl not in op:
                    op.append(cl)
lis = ""
for i in range(0, len(op)):
    lis += op[i] + " "
p.addEnumerationPulldown('Choose which dots inputs you want to Hide or Label', lis)
p.addBooleanCheckBox('Hide', False)
p.addBooleanCheckBox('Unhide', False)
p.addBooleanCheckBox('Label', True)
p.addBooleanCheckBox('Unlabel', False)
p.addBooleanCheckBox('Rename', False)

p.show()
inputNode = p.value('Choose which dots inputs you want to Hide or Label')
label = p.value('Label')
hide = p.value('Hide')
unhide = p.value('Unhide')
unlabel = p.value('Unlabel')
rename = p.value('Rename')


if inputNode != None:
    if inputNode != "Selection":   
    #Loop into each node and ask for the dots
        if inputNode == 'Dot':
            nuke.allNodes().sort()
        for node in nuke.allNodes():
            if node.Class() == 'Dot':
                dots += 1
                if node.inputs() == 1:
                    if node.input(0).Class() == inputNode:
                        realdots+=1
                        attach = True
                        name = node.input(0).knob('label').getValue()
                        if node.knob('label').getValue() !="":
                            if rename:
                                if label and unlabel == False:
                                    if name == "":
                                        name = node.input(0).name()
                                    node.knob('label').setValue(name)
                            else:
                                if hide == False and unhide == False and unlabel == False:
                                    realdots = realdots - 1
                        else:
                            if label and unlabel == False:
                                if name == "":
                                    name = node.input(0).name()
                                node.knob('label').setValue(name)
                        if hide and unhide == False:
                            node.knob('hide_input').setValue(True)
                            
                        if unhide and hide == False:
                            node.knob('hide_input').setValue(False)
                        
#                        if unhide and hide:
#                            hide_un=True
#                            node.knob('hide_input').setValue(False)
                            
                        if unlabel and label == False:
                            node.knob('label').setValue("")
                else:
                    Minput = True

    else:
        try: 
            select = True
            selNodes = nuke.selectedNodes()
            assert len(selNodes)>0

        except:
            attach = True
            Minput = False
            dots = 1
            nuke.message("You don't have any node selected")


        if len(selNodes)>0:
            selNodes.sort()
            for n in selNodes:
                if n.Class() == 'Dot':
                    dots += 1
                    if n.inputs() == 1:
                        realdots+=1
                        name = n.input(0).knob('label').getValue()
                        if n.knob('label').getValue() !="":
                            if rename:
                                if label and unlabel == False:
                                    if name == "":
                                        name = n.input(0).name()
                                    n.knob('label').setValue(name)
                                
                            else:
                                if  hide == False and unhide == False and unlabel == False:
                                    realdots = realdots - 1
                        else:
                            if label and unlabel == False:
                                if name == "":
                                    name = n.input(0).name()
                                n.knob('label').setValue(name)
                        if hide and unhide == False:
                            n.knob('hide_input').setValue(True)
                            
                        if unhide and hide == False:
                            n.knob('hide_input').setValue(False)
                        
#                        if unhide and hide:
#                            hide_un=True
#                            n.knob('hide_input').setValue(False)

                        if unlabel and label == False:
                            n.knob('label').setValue("")
                               
                    else:
                        Minput = True

        if attach == False and select == False:
            nuke.message("You don't have any dot attach to the input node")
        if Minput:
            nuke.message("Some of your dots don't have any input")
        if dots == 0 and select == False:
            nuke.message("You don't have any dots in your script")
        if dots == 0 and select:
            nuke.message("You don't have any dots Selected")
        if unhide and hide:
            realdots = 0
            nuke.message("You check hide and unhide, please just select one")
        if label and unlabel:
            realdots = 0
            nuke.message("You check label and unlabel, please just select one")
            
if realdots != 0:
    mes = "You have modify " + str(realdots) + " dots in your script"
    nuke.message(str(mes))