//
// Created by Donat on 18/09/2023.
//
#include <gtest/gtest.h>
#include "../User.h"

TEST(Usertest, Constructor) {
    std::string name = "Donat";
    User u(name);


}

TEST(Usertest, Changename) {
    std::string name = "Donat";
    User u(name);
    std::string name2 = "Donat2";
    u.changeName(name2);

}

TEST(Usertest, AddList) {
    std::string name = "Donat";
    User u(name);
    std::string list1name = "List1";
    std::string list2name = "List2";

    List l(list2name);
    u.addList(list1name);
    u.addList(&l);

}

TEST(Usertest, RemoveList) {
    std::string name = "Donat";
    User u(name);
    std::string list1name = "List1";
    std::string list2name = "List2";
    List l(list2name);
    u.addList(list1name);
    u.addList(&l);
    u.removeList("List1");
    u.removeList("List2");

}

TEST(Usertest, PrintLists) {
    std::string name = "Donat";
    User u(name);
    std::string list1name = "List1";
    std::string list2name = "List2";
    List l(list2name);
    u.addList(list1name);
    u.addList(&l);


}

TEST(Usertest, GetLists) {
    std::string name = "Donat";
    User u(name);
    std::string list1name = "List1";
    std::string list2name = "List2";
    List l(list2name);
    u.addList(list1name);
    u.addList(&l);
    u.getLists();

}



