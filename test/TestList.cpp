//
// Created by Donat on 18/09/2023.
//

#include <gtest/gtest.h>
#include "../list.h"
#include "../Item.h"


TEST(ListTest, Constructor) {
    std::string list1name = "List1";
    List l(list1name);
}

TEST(ListTest, AddObject) {
    std::string list1name = "List1";
    List l(list1name);
    std::string uom = "Kg";
    std::string categ = "milk";
    std::string name = "icecream";
    l.addItem(uom, 2, categ, name, false);
}

TEST(ListTest, RemoveObject) {
    std::string list1name = "List1";
    List l(list1name);
    std::string uom = "Kg";
    std::string categ = "milk";
    std::string name = "yogurt";
    l.addItem(uom, 2, categ, name, false);
    l.removeItem("yogurt");
}

TEST(ListTest, ChangeBought) {
    std::string list1name = "List1";
    List l(list1name);
    std::string uom = "Kg";
    std::string categ = "milk";
    std::string name = "yogurt";
    Item i(uom, 2, categ, name, false);
    l.addItem(i);
    l.changeBought(i.getName(), true);
}

TEST(ListTest, totelementseist) {
    std::string list1name = "List1";
    List l(list1name);
    std::string uom = "Kg";
    std::string categ = "milk";
    std::string name = "milk";
    l.addItem(uom, 2, categ, name, false);
    l.totElementsList();
}


