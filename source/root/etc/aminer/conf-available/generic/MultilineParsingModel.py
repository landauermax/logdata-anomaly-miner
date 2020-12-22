"""This module defines a parser for multiline logs."""

from aminer.parsing import DecimalIntegerValueModelElement
from aminer.parsing import DelimitedDataModelElement
from aminer.parsing import FirstMatchModelElement
from aminer.parsing import FixedDataModelElement
from aminer.parsing import SequenceModelElement


def get_model():
    """Return the model."""
    model = SequenceModelElement('multiline', [
        FixedDataModelElement('length_str', b'LENGTH: "'),
        DecimalIntegerValueModelElement('length'),
        FixedDataModelElement('sessionid_str', b'"\nSESSIONID:['),
        DecimalIntegerValueModelElement('sessionid_id'),
        FixedDataModelElement('sessionid_str2', b'] "'),
        DecimalIntegerValueModelElement('sessionid'),
        FixedDataModelElement('entryid_str', b'"\nENTRYID:['),
        DecimalIntegerValueModelElement('entryid_id'),
        FixedDataModelElement('entryid_str2', b'] "'),
        DecimalIntegerValueModelElement('entryd'),
        FixedDataModelElement('statement_str', b'"\nSTATEMENT:['),
        DecimalIntegerValueModelElement('statement_id'),
        FixedDataModelElement('statement_str2', b'] "'),
        DecimalIntegerValueModelElement('statement'),
        FixedDataModelElement('userid_str', b'"\nUSERID:['),
        DecimalIntegerValueModelElement('userid_id'),
        FixedDataModelElement('userid_str2', b'] "'),
        DelimitedDataModelElement('userid', b'"'),
        FixedDataModelElement('userhost_str', b'"\nUSERHOST:['),
        DecimalIntegerValueModelElement('userhost_id'),
        FixedDataModelElement('userhost_str2', b'] "'),
        DelimitedDataModelElement('userhost', b'"'),
        FixedDataModelElement('terminal_str', b'"\nTERMINAL:['),
        DecimalIntegerValueModelElement('terminal_id'),
        FixedDataModelElement('terminal_str2', b'] "'),
        DelimitedDataModelElement('terminal', b'"'),
        FixedDataModelElement('action_str', b'"\nACTION:['),
        DecimalIntegerValueModelElement('action_id'),
        FixedDataModelElement('action_str2', b'] "'),
        DecimalIntegerValueModelElement('action'),
        FixedDataModelElement('returncode_str', b'"\nRETURNCODE:['),
        DecimalIntegerValueModelElement('returncode_id'),
        FixedDataModelElement('returncode_str2', b'] "'),
        DecimalIntegerValueModelElement('returncode'),
        FixedDataModelElement('remainder', b'"')
    ])
    return model

