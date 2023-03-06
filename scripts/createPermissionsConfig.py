from cgi import print_arguments
import yaml
from yaml.loader import SafeLoader

newLine = '\n'

pSets = 'permission_sets = [' +newLine
with open('permissionsets.yml') as f:
    data = list(yaml.load_all(f, Loader=SafeLoader))
    strPermissionSets = ''

    for fTeam in data:
        if fTeam is None:
            continue

        for permission in fTeam['permissionsets']:
            pset = '  {' + newLine
            pset = pset + '    name               = "'+ permission['permission-name'] + '"' + newLine
            pset = pset + '    description        = "Update later : ' + permission['permission-name']  +'",'+ newLine
            pset = pset + '    relay_state        = "",' + newLine
            pset = pset + '    session_duration   = "",' + newLine
            pset = pset + '    tags               = {},' + newLine
            pset = pset + '    inline_policy      = "",' + newLine

            pset = pset + '    policy_attachments = [' +newLine
            hasPolicy = False
            for policy in permission['policies']:
                if policy.find('iam::aws:policy') > 0 :
                    pset=pset + '      "' + policy + '",' + newLine
                    hasPolicy = True
            
            if hasPolicy:
                pset = pset[:-2] + newLine + '    ],' +newLine
            else:
                pset = pset[:-1] + newLine + '],' +newLine

            pset = pset + '    customer_managed_policy_attachments = [' + newLine
            hasPolicy = False
            for policy in permission['policies']:
                if not policy.find('iam::aws:policy') > 0 :
                    hasPolicy = True
                    custPolicy = policy.split(':policy',1)[1]
                    custPolicyParts = custPolicy.split('/')
                    policyName = custPolicyParts[len(custPolicyParts)-1]
                    policyPath = custPolicy[:-len(policyName)]
                    pset=pset + '      {'+ newLine
                    pset=pset + '        name = "'+ policyName +'"'+ newLine
                    pset=pset + '        path = "'+ policyPath +'"'+ newLine
                    pset=pset + '      },'+ newLine
            
            if hasPolicy:
                pset = pset[:-2] + newLine + '    ]' +newLine
            else:
                pset = pset[:-1] + newLine + '],' +newLine    

            pset = pset + '  },' + newLine
            pSets = pSets + pset
print(pSets[:-2] + newLine + ']')
