#!/usr/bin/env python

# Very basic example of retrieving existing information
# from COR (registered ontologies, organizations, terms).

if __name__ == "__main__":
    from pprint import pprint
    import swagger_client

    configuration = swagger_client.Configuration()
    # Note: no authenticated operations in this simple demo.
    api_client = swagger_client.ApiClient(configuration)

    # ontologies
    ont_api = swagger_client.OntologyApi(api_client)
    print('\n\nOntologies' + '=' * 50 + '\n')
    pprint(ont_api.ont_get())

    iri = 'http://sweetontology.net/realmBiolBiome'
    format = 'ttl'
    print('\n\nOntology by iri=%s format=%s' % (iri, format) + '=' * 50 + '\n')
    response = ont_api.ont_get(iri=iri, format=format)
    pprint(response)

    # organizations
    org_api = swagger_client.OrganizationApi(api_client)
    print('\n\nOrganizations' + '=' * 50 + '\n')
    print('Organizations:')
    pprint(org_api.org_get())

    # terms
    term_api = swagger_client.TermApi(api_client)
    containing = 'temperature'
    print('\n\nTerms containing "%s" in SPO' % containing + '=' * 50 + '\n')
    pprint(term_api.term_get(containing=containing, _in='spo'))
