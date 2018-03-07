#!/usr/bin/python

import xml.etree.ElementTree
from LiquibaseData import LiquibaseChangeLog, LiquibaseChangeSet
from io import BytesIO

def writeChangeLogFile(liquibaseData):
    liquibaseTree = xml.etree.ElementTree.Element('databaseChangeLog');
    for changeSet in liquibaseData.changeSets:
        if isinstance(changeSet, LiquibaseChangeLog):
            writeChangeLogFile(changeSet)
            attrib = {
                id: changeSet.id,
                context: changeSet.context,
                author: changeSet.author
            }
            xml.etree.ElementTree.SubElement(liquibaseTree, "include", attrib)
        else:
            xml.etree.ElementTree.SubElement(liquibaseTree, "changeSet", {})

    et = xml.etree.ElementTree.ElementTree(liquibaseTree)
    et.write(liquibaseData.name, encoding='utf-8', xml_declaration=True)