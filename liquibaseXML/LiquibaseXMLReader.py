#!/usr/bin/python

import xml.etree.ElementTree
from LiquibaseData import LiquibaseChangeLog, LiquibaseChangeSet

def readChangeLogFile(file):
    changeLog = LiquibaseChangeLog()
    changeLog.name = file
    changeLogXML = xml.etree.ElementTree.parse(file).getroot()

    for child in changeLogXML:
        if "include" in child.tag:
            changeLog.changeSets.append(readChangeLogFile(child.attrib.value))
        elif "changeSet" in child.tag:
            changeLog.changeSets.append(readChangeSet(child))
    return changeLog


def readChangeSet(element):
    changeSet = LiquibaseChangeSet()
    if element.attrib["id"]:
        changeSet.id = element.get("id")
    if element.get("context"):
        changeSet.context = element.get("context")
    if element.get("author"):
        changeSet.author = element.get("author")
    return changeSet


