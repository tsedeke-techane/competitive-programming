class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = Counter()
      
        for cpdomain in cpdomains:
            visit_num = int(cpdomain.split(' ')[0])
            domain = cpdomain.split(' ')[1]
            subdomains = domain.split('.')
            # print(subdomains)
          
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                # print(subdomain)
                domain_count[subdomain] += visit_num
                # print(domain_count)
      
        ans = [f"{count} {domain}" for domain, count in domain_count.items()]

        return ans