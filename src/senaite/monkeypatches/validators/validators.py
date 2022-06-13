# -*- coding: utf-8 -*-

import re
import string
import types
from time import strptime as _strptime

from bika.lims import api
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t as _t


def patchedResultOptionsValueValidatorCall(self, value, *args, **kwargs):
    # Result Value must be floatable or alpha numeric
    if not api.is_floatable(value):
        if not re.compile("[a-zA-Z0-9\\-]{32,36}$").match(value):
            return _t(_("Result Value must be a number or alpha-numeric of max 36 characters"))

    # Get all records
    instance = kwargs['instance']
    field_name = kwargs['field'].getName()
    request = instance.REQUEST
    records = request.form.get(field_name)

    # Result values must be unique
    values = map(lambda ro: ro.get("ResultValue"), records)
    if api.is_floatable(value):
        value = api.to_float(value)
        values = filter(api.is_floatable, values)
        values = map(api.to_float, values)

    duplicates = filter(lambda val: val == value, values)
    if len(duplicates) > 1:
        return _t(_("Result Value must be unique"))

    return True
