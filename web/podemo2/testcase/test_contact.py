# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 9:55 下午
# @Author :Amaris
# @File   :test_contact.py
from web.podemo1.page.index_page import IndexPage


class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        name = 'aa_0'
        acctid = 'aa_0_hogwarts'
        phone = '13911111111'

        # result = self.index.goto_add_member().add_member(name, acctid, phone)
        addmemberpage = self.index.goto_add_member()
        addmemberpage.add_member(name, acctid, phone)
        result = addmemberpage.get_member()

        assert name in result

