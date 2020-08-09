######################################################
###  All inventory storage will be placed here     ###
######################################################

init python:
    class Inventory:
        __items_massive = []

        def getItems(self):
            return self.__items_massive

        def storeItem(self):
            self.__items_massive

        def storeNewItem(self, item):
            self.__items_massive.append(item)
