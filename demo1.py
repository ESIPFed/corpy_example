#!/usr/bin/env python

# Very basic example of retrieving existing information
# from COR (registered ontologies, organizations, terms).

if __name__ == "__main__":
    from pprint import pprint

    from swagger_client import ApiClient
    from swagger_client import OntologyApi
    from swagger_client import OrganizationApi
    from swagger_client import TermApi

    # explicitly indicate the API endpoint:
    host = 'http://cor.esipfed.org/ont/api/v0'
    print("Using endpoint " + host)

    # With not authentication:
    api_client = ApiClient(host=host)

    ont_api = OntologyApi(api_client)
    org_api = OrganizationApi(api_client)
    term_api = TermApi(api_client)

    print('\n' + '=' * 20)
    print('Ontologies:')
    pprint(ont_api.ont_get())

    print('\n' + '=' * 20)
    print('Organizations:')
    pprint(org_api.org_get())

    print('\n' + '=' * 20)
    print('Terms containing "temperature" in SPO:')
    pprint(term_api.term_get(containing='temperature', _in='spo'))
