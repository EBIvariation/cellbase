import pycellbase.cbrestclients as fts
from pycellbase.cbconfig import ConfigClient
from pycellbase.commons import get


class CellBaseClient(object):
    """Creates different query clients and allows direct queries to the RESTful
     service"""
    def __init__(self, config_client=None):
        # Client storage; If a client is already created, then it is returned
        self._clients = {}

        # Setting up config params
        if config_client is not None:
            try:
                assert isinstance(config_client, ConfigClient)
            except:
                msg = ('CellBaseClient configuration not properly set.' +
                       ' "pycellbase.config.ConfigClient" object is needed as' +
                       ' parameter')
                raise IOError(msg)
            self._configuration = config_client
        else:
            self._configuration = ConfigClient()

    def get_config(self):
        """Returns current configuration parameters"""
        return self._configuration.configuration

    def get(self, category, subcategory, resource, query_id=None, **options):
        """Creates the URL for querying the REST service"""
        response = get(host=self._configuration.host,
                       version=self._configuration.version,
                       species=self._configuration.species,
                       category=category,
                       subcategory=subcategory,
                       query_id=query_id,
                       resource=resource,
                       options=options)

        return response

    def get_gene_client(self):
        """Creates the gene client"""
        if 'GENE' not in self._clients:
            self._clients['GENE'] = fts.GeneClient(self._configuration)
        return self._clients['GENE']

    def get_transcript_client(self):
        """Creates the protein client"""
        if 'TRANSCRIPT' not in self._clients:
            self._clients['TRANSCRIPT'] =\
                fts.TranscriptClient(self._configuration)
        return self._clients['TRANSCRIPT']

    def get_protein_client(self):
        """Creates the protein client"""
        if 'PROTEIN' not in self._clients:
            self._clients['PROTEIN'] = fts.ProteinClient(self._configuration)
        return self._clients['PROTEIN']

    def get_variation_client(self):
        """Creates the variation client"""
        if 'VARIATION' not in self._clients:
            self._clients['VARIATION'] =\
                fts.VariationClient(self._configuration)
        return self._clients['VARIATION']

    def get_genomic_region_client(self):
        """Creates the genomic region client"""
        if 'GENOMIC_REGION' not in self._clients:
            self._clients['GENOMIC_REGION'] = \
                fts.GenomicRegionClient(self._configuration)
        return self._clients['GENOMIC_REGION']

    def get_variant_client(self):
        """Creates the variant client"""
        if 'VARIANT' not in self._clients:
            self._clients['VARIANT'] = fts.VariantClient(self._configuration)
        return self._clients['VARIANT']
