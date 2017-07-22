
from idna.core import InvalidCodepoint
import pytest

# test content inspired by https://github.com/jcranmer/idna-uts46/blob/master/test/test-uts46.js

def test_nameprep_basic_unicode(ens):
    assert ens.nameprep("öbb.at") == "öbb.at"
    assert ens.nameprep("Öbb.at") == "öbb.at"
    assert ens.nameprep("O\u0308bb.at") == "öbb.at"
    assert ens.nameprep("xn--bb-eka.at") == "öbb.at"
    assert ens.nameprep("faß.de") == "faß.de"
    assert ens.nameprep("fass.de") == "fass.de"
    assert ens.nameprep("xn--fa-hia.de") == "faß.de"

def test_nameprep_std3_rules(ens):
    with pytest.raises(InvalidCodepoint):
        ens.nameprep("not=std3")
