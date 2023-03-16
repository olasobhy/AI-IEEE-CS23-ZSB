class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #emails = [e for e in emails.split(',')]
        lst =[]
        for e in emails :
            l = e.split('@')
            local_name= l[0]
            if '+' in local_name:
                 i = local_name.index('+')
                 local_name = local_name.replace(local_name[i::],"")  
            domain_name =l[1]
            local_name =local_name.replace(".","")
            email =local_name +"@"+ domain_name
            if email not in lst:
                 lst.append(email)
        return(len(lst))