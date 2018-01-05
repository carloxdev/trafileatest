# -*- coding: utf-8 -*-

# Python's Libraries
import hashlib
import random


class UserBusiness(object):

    @staticmethod
    def get_token():
        """Obtengo un token random para el usuario."""
        return hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()
