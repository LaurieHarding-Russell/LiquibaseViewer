#!/usr/bin/python

import sys
from Tkinter import *
import LiquibaseXMLReader
from LiquibaseData import LiquibaseChangeLog, LiquibaseChangeSet

def createCommitLabel(commitsFrame):
    for changeSet in liquibaseData.changeSets:
        if isinstance(changeSet, LiquibaseChangeSet):
            lineText = changeSet.id + " " + changeSet.context + " " + changeSet.author
            left = Label(commitsFrame, text=lineText)
            left.pack()
        else:
            createCommitLabel(commitsFrame)

xmlFile = ""
if len(sys.argv) > 1:
    xmlFile = sys.argv[1]
else:
    exit(1)

liquibaseData = LiquibaseXMLReader.readChangeLogFile(xmlFile)
root = Tk()
root.title('Liquibase Viewer')

commitsFrame = LabelFrame(root, text=liquibaseData.name, width= 300)
commitsFrame.pack(side = LEFT, fill="y")
createCommitLabel(commitsFrame)


data = Canvas(root, bg="blue", height=250)
data.pack(side = LEFT, fill="both")

root.mainloop()