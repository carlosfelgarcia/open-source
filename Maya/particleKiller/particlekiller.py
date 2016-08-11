'''
Created on Apr 19, 2015

@author: Carlos Garcia
@url: www.vfxcarlosgarcia.com
email: carlos@vfxcarlosgarcia.com
'''


import random as rand
import maya.cmds as cmds
import sys

Psel = cmds.ls( selection=True )
listIds = []
funtionDic = {'------------': None, 'Pairs (Only works once)': 1, 'Odds (Only works once)': 2, 'Half': 3, 'Number': 4 }
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#Main Functions
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------    
def main(*args):
    particlesIds = cmds.getAttr(Psel[0] + '.particleId')
    if particlesIds != None:
        lifespanMode = cmds.getAttr(Psel[0] + '.lifespanMode')
        selFuntion = cmds.optionMenuGrp('opitions', q = True, v = True)
        numToKill = cmds.intField('particleNumber', q = True, v = True)
        fn = funtionDic[selFuntion]
        print particlesIds
        if fn != None:
            if fn == 1:
                particleList = pair(particlesIds)
            elif fn == 2:
                particleList = odds(particlesIds)
            elif fn == 3:
                particleList = half(particlesIds)
            elif fn == 4:
                particleList = number(particlesIds, numToKill)
            
            print particleList
            killer(particleList, particlesIds, lifespanMode)
            cmds.deleteUI(window)
    else:
        result = cmds.confirmDialog(
                title='No particles',
                message="There are no particles to kill",
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

        if result == 'OK' or result == 'Cancel':
            cmds.deleteUI(window)
                
def killer(listIds, particlesIds, lifespanMode):
    print "Killing ", len(listIds) , " particles."
    if listIds:
        if lifespanMode != 3:
            cmds.setAttr(Psel[0] + '.lifespanMode', 3)
            print "lifespanMode changed to 'lifespanPP only'"
        for particleId in listIds:
            try:
                if particleId in particlesIds:
                    cmds.nParticle( Psel[0], e=True, attribute='lifespanPP', id = particleId, fv=0 )
            except:
                print "The selected method can't kill more particles please select another."
        #if lifespanMode != 3:
         #   cmds.setAttr(Psel[0] + '.lifespanMode', lifespanMode)
        print "Particles killed: ", listIds
    
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#Base Funtions
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
def check(*args):
    Psel = cmds.ls( selection=True )
    print Psel
    if len(Psel) > 1:
        result = cmds.confirmDialog(
                title='More than one selection',
                message="Please select just the particle system",
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

        if result == 'OK':
            cmds.select( clear=True )
            cmds.deleteUI(window)

    elif len(Psel) == 0:
        result = cmds.confirmDialog(
                title='Nothing is selected',
                message="Nothing is selected.",
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

        if result == 'OK':
            cmds.select( clear=True )
            cmds.deleteUI(window)

    else:
        shapesList = cmds.listRelatives(Psel[0])
        objType = cmds.objectType(shapesList[0])
        if(objType !=  'nParticle'):
            result = cmds.confirmDialog(
                    title='Particles are not selected',
                    message="The selection is not a particle system.",
                    button=['OK', 'Cancel'],
                    defaultButton='OK',
                    cancelButton='Cancel',
                    dismissString='Cancel')

            if result == 'OK':
                cmds.select( clear=True )
                cmds.deleteUI(window)
                
        else:
            option = cmds.optionMenuGrp('opitions', q = True, v = True)
            if option == 'Number':
                cmds.intField('particleNumber', enable = True, edit = True)
            else:
                cmds.intField('particleNumber', enable = False, edit = True)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#Search Funtions
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

def pair(particlesIds, listIds = []):
    listIds = [particleId for particleId in particlesIds if particleId % 2 == 0]
    return listIds
    
def odds(particlesIds, listIds = []):
    listIds = [particleId for particleId in particlesIds if particleId % 2 == 1]
    return listIds

def half(particlesIds, listIds = []):
    counter = 0
    for particleId in particlesIds:
        if counter % 2 == 0:
            listIds.append(particleId)
        counter += 1
    return listIds

def number(particlesIds, numToKill, listIds = []):
    counter = 0
    while counter < numToKill:
        randNum = rand.randint(0, len(particlesIds))
        if randNum in listIds and randNum in particlesIds:
            while randNum not in listIds and randNum in particlesIds:
                randNum = rand.randint(0, len(particlesIds))
            listIds.append(randNum)
        else:
            listIds.append(randNum)
        counter += 1
    return listIds
    
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#window creation
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

if (cmds.window('Particle Killer', exists=True)):
    cmds.deleteUI('Particle Killer')

window = cmds.window('Particle Killer')
cmds.rowColumnLayout( numberOfColumns=1)

#gMainProgressBar = cmds.progressBar(maxValue=rangeF,isInterruptable=True,width=400)

cmds.text( label='\n1.Please select the particle system,\n\n2.Choose the fuction to kill the particles,\n\n3.Run it ...', fn = "boldLabelFont", al='left')
cmds.separator( height=20, style='doubleDash', w = 350)
cmds.text( label='Note: Some functions only works once due to that the particles Ids are unique', fn = "boldLabelFont", al='left')
cmds.separator( height=10, style='none', w = 350)
options = cmds.optionMenuGrp('opitions', label='Funtions', w = 350, cc = check)
cmds.menuItem( label='------------' )
cmds.menuItem( label='Pairs (Only works once)' )
cmds.menuItem( label='Odds (Only works once)' )
cmds.menuItem( label='Half' )
cmds.menuItem( label='Number' )
particleNumber = cmds.intField('particleNumber', enable = False)
cmds.button( label='Kill them, ALL!!!', c = main, w = 100)


cmds.showWindow( window )