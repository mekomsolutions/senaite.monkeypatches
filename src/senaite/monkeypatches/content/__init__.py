# -*- coding: utf-8 -*-

from bika.lims import bikaMessageFactory as _
from bika.lims.browser.widgets.recordswidget import RecordsWidget
from senaite.core.browser.fields.records import RecordsField
from senaite.core import logger

import bika.lims.content.abstractbaseanalysis as abstractbaseanalysisToPatch


# Results can be selected from a dropdown list.  This prevents the analyst
# from entering arbitrary values.  Each result must have a ResultValue, which
# must be a number - it is this number which is interpreted as the actual
# "Result" when applying calculations.
patchedResultOptions = RecordsField(
    'ResultOptions',
    schemata="Result Options",
    type='resultsoptions',
    subfields=('ResultValue', 'ResultText'),
    required_subfields=('ResultValue', 'ResultText'),
    subfield_labels={'ResultValue': _('Result Value'),
                     'ResultText': _('Display Value'), },
    subfield_validators={'ResultValue': 'result_options_value_validator',
                         'ResultText': 'result_options_text_validator'},
    subfield_sizes={'ResultValue': 20,
                    'ResultText': 25,},
    subfield_maxlength={'ResultValue': 40,
                        'ResultText': 255,},
    widget=RecordsWidget(
        label=_("Predefined results"),
        description=_(
            "List of possible final results. When set, no custom result is "
            "allowed on results entry and user has to choose from these values"
        ),
    )
)

abstractbaseanalysisToPatch.ResultOptions = patchedResultOptions
abstractbaseanalysisToPatch.schema.addField(patchedResultOptions)