"""
Floating IP DNS interface.
"""
from urllib import quote
from ops_client.manager.nova import NovaBaseManager

def _quote_domain(domain):
    """Special quoting rule for placing domain names on a url line.

    Domain names tend to have .'s in them.  Urllib doesn't quote dots,
    but Routes tends to choke on them, so we need an extra level of
    by-hand quoting here.
    """
    return quote(domain.replace('.', '%2E'))

class FloatingIPDNSDomainManager(NovaBaseManager):

    def domains(self, response_key = True, **kwargs):
        """Return the list of available dns domains."""
        key = None
        if response_key : 
            key = 'domain_entries'
        return self._get("/os-floating-ip-dns", key, **kwargs)

    def create_private(self, fqdomain, availability_zone, 
                       response_key = True, **kwargs):
        """Add or modify a private DNS domain."""
        body = {'domain_entry':
                 {'scope': 'private',
                  'availability_zone': availability_zone}}
        key = None
        if response_key : 
            key = 'domain_entry'
        return self._update('/os-floating-ip-dns/%s' % _quote_domain(fqdomain),
                            body, key, **kwargs)
            

    def create_public(self, fqdomain, project, response_key = True, **kwargs):
        """Add or modify a public DNS domain."""
        body = {'domain_entry':
                 {'scope': 'public',
                  'project': project}}
        key = None
        if response_key : 
            key = 'domain_entry'
        return self._update('/os-floating-ip-dns/%s' % _quote_domain(fqdomain),
                            body, key, **kwargs)

    def delete(self, fqdomain, **kwargs):
        """Delete the specified domain."""
        self._delete("/os-floating-ip-dns/%s" % _quote_domain(fqdomain), 
                     **kwargs)



class FloatingIPDNSEntryManager(NovaBaseManager):

    def get(self, domain, name, response_key = True, **kwargs):
        """Return a list of entries for the given domain and ip or name."""
        key = None
        if response_key : 
            key = "dns_entry"
        return self._get("/os-floating-ip-dns/%s/entries/%s" %
                              (_quote_domain(domain), name),
                          "dns_entry", **kwargs)

    def get_for_ip(self, domain, params = None, response_key = True, **kwargs):
        """Return a list of entries for the given domain and ip or name."""
        key = None
        if response_key : 
            key = "dns_entries"

        return self._list("/os-floating-ip-dns/%s/entries" %
                              _quote_domain(domain),
                          key, params=params, **kwargs)

    def create(self, domain, name, ip, dns_type, response_key = True, **kwargs):
        """Add a new DNS entry."""
        body = {'dns_entry':
                 {'ip': ip,
                  'dns_type': dns_type}}
        key = None
        if response_key : 
            key = "dns_entry"
        return self._update("/os-floating-ip-dns/%s/entries/%s" %
                            (_quote_domain(domain), name),
                            body, key, **kwargs)

    def modify_ip(self, domain, name, ip, response_key = True, **kwargs):
        """Add a new DNS entry."""
        body = {'dns_entry':
                 {'ip': ip,
                  'dns_type': 'A'}}
        key = None
        if response_key : 
            key = "dns_entry"
        return self._update("/os-floating-ip-dns/%s/entries/%s" %
                            (_quote_domain(domain), name),
                            body, key, **kwargs)

    def delete(self, domain, name, **kwargs):
        """Delete entry specified by name and domain."""
        self._delete("/os-floating-ip-dns/%s/entries/%s" %
                                (_quote_domain(domain), name), **kwargs)
