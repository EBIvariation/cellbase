import unittest

import pycellbase.cbfeatures as cbfts
from pycellbase.cbconfig import ConfigClient


class GeneClientTest(unittest.TestCase):
    """Tests the GeneClient class"""
    def setUp(self):
        """Initializes the gene client"""
        self._gc = cbfts.GeneClient(ConfigClient())

    def test_get_biotypes(self):
        """Checks retrieval of gene biotypes"""
        res = self._gc.get_biotypes()
        assert len(res[0]['result']) == 29
        assert 'protein_coding' in res[0]['result']

    def test_get_clinical(self):
        """Checks retrieval of gene clinical info"""
        res = self._gc.get_clinical('BRCA1')
        assert len(res[0]['result']) == 6412
        assert res[0]['result'][0]['source'] == 'clinvar'

    def test_get_protein(self):
        """Checks retrieval of protein"""
        res = self._gc.get_protein('BRCA1')
        assert len(res[0]['result']) == 1
        assert res[0]['result'][0]['name'][0] == 'BRCA1_HUMAN'

    def test_get_transcript(self):
        """Checks retrieval of protein"""
        res = self._gc.get_transcript('BRCA1')
        assert len(res[0]['result']) == 27
        assert res[0]['result'][0]['name'] == 'BRCA1-001'

    def test_get_tfbs(self):
        """Checks retrieval of protein"""
        res = self._gc.get_tfbs('BRCA1')
        assert len(res[0]['result']) == 175
        assert res[0]['result'][0]['tfName'] == 'E2F4'

    def test_get_snp(self):
        """Checks retrieval of snp"""
        res = self._gc.get_snp('LDLR')
        assert len(res[0]['result']) == 4113
        assert res[0]['result'][0]['id'] == 'rs191244119'

    def test_get_info(self):
        """Checks retrieval of gene info"""
        res = self._gc.get_info('BRCA1')
        assert len(res[0]['result']) == 1
        assert res[0]['id'] == 'BRCA1'


class ProteinClientTest(unittest.TestCase):
    """Tests the ProteinClient class"""
    def setUp(self):
        """Initializes the protein client"""
        self._pc = cbfts.ProteinClient(ConfigClient())

    def test_get_substitution_scores(self):
        """Checks retrieval of protein substitution scores"""
        res = self._pc.get_substitution_scores('BRCA1_HUMAN')
        assert len(res[0]['result']) == 1
        assert (res[0]['result'][0]['1']['W'] ==
                {'pe': 0, 'ps': 0.995, 'ss': 0, 'se': 1})

    def test_get_sequence(self):
        """Checks retrieval of protein sequence"""
        res = self._pc.get_sequence('Q9UL59')
        assert len(res[0]['result']) == 1
        assert len(res[0]['result'][0]) == 606


class TrancriptClientTest(unittest.TestCase):
    """Tests the TrancriptClient class"""
    def setUp(self):
        """Initializes the transcript client"""
        self._tc = cbfts.TranscriptClient(ConfigClient())

    def test_get_function_prediction(self):
        """Checks retrieval of function predictions"""
        res = self._tc.get_function_prediction('ENST00000536068')
        assert len(res[0]['result']) == 1
        assert (res[0]['result'][0]['10']['E'] ==
                {'pe': 1, 'se': 1, 'ps': 0.497, 'ss': 0})

    def test_get_gene(self):
        """Checks retrieval of genes which codify the transcript"""
        res = self._tc.get_gene('ENST00000536068')
        assert len(res[0]['result']) == 1
        assert res[0]['result'][0]['name'] == 'ZNF214'

    def test_get_protein(self):
        """Checks retrieval of codified proteins"""
        res = self._tc.get_protein('ENST00000536068')
        assert len(res[0]['result']) == 1
        assert res[0]['result'][0]['name'][0] == 'ZN214_HUMAN'

    def test_get_sequence(self):
        """Checks retrieval of the transcript sequence"""
        res = self._tc.get_sequence('ENST00000536068')
        assert len(res[0]['result']) == 1
        assert len(res[0]['result'][0]) == 2562


class VariationClientTest(unittest.TestCase):
    """Tests the VariationClient class"""
    def setUp(self):
        """Initializes the variation client"""
        self._vc = cbfts.VariationClient(ConfigClient())

    def test_get_consequence_types(self):
        """Checks retrieval of consequence types with and without specific ID"""
        # Without ID
        res = self._vc.get_consequence_types()
        assert len(res[0]['result']) == 38
        assert 'coding_sequence_variant' in res[0]['result']

        # With ID # TODO Currently not working. Is this deprecated?
        res = self._vc.get_consequence_types('rs6025')
        assert len(res[0]['result']) == 0
        assert res[0]['result'] == []


class GenomicRegionTest(unittest.TestCase):
    """Tests the GenomicRegion class"""
    def setUp(self):
        """Initializes the variation client"""
        self._gr = cbfts.GenomicRegionClient(ConfigClient())

    def test_get_clinical(self):
        """Checks retrieval of clinical data"""
        res = self._gr.get_clinical('3:100000-900000')
        assert len(res[0]['result']) == 469
        assert res[0]['result'][0]['mutationCDS'] == 'c.4G>A'

    def test_get_conservation(self):
        """Checks retrieval of conservation data"""
        res = self._gr.get_conservation('3:100000-900000')
        assert len(res[0]['result']) == 3
        assert res[0]['result'][0]['source'] == 'gerp'

    def test_get_gene(self):
        """Checks retrieval of genes"""
        res = self._gr.get_gene('3:100000-900000')
        assert len(res[0]['result']) == 8
        assert res[0]['result'][0]['name'] == 'AC090044.1'

    def test_get_regulatory(self):
        """Checks retrieval of regulatory elements"""
        res = self._gr.get_regulatory('3:100000-900000')
        assert len(res[0]['result']) == 677
        assert res[0]['result'][0]['name'] == 'H3K27me3'

    def test_get_sequence(self):
        """Checks retrieval of sequence"""
        res = self._gr.get_sequence('3:100-200')
        assert len(res[0]['result']) == 1
        assert len(res[0]['result'][0]['sequence']) == 101

    def test_get_tfbs(self):
        """Checks retrieval of transcription factor binding sites (TFBSs)"""
        res = self._gr.get_tfbs('3:100000-900000')
        assert len(res[0]['result']) == 239
        assert res[0]['result'][0]['name'] == 'CTCF'

    def test_get_transcript(self):
        """Checks retrieval of transcripts"""
        res = self._gr.get_transcript('3:1000-100000')
        assert len(res[0]['result']) == 2
        assert res[0]['result'][0]['id'] == 'ENST00000440867'

    def test_get_variation(self):
        """Checks retrieval of variations"""
        res = self._gr.get_variation('3:10000-100000')
        assert len(res[0]['result']) == 2937
        assert res[0]['result'][0]['id'] == 'rs192023809'


if __name__ == '__main__':
    unittest.main()
