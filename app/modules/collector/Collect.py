from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

class Colletor : 
    '''
        Class to collect and return data submitted to a form
    '''

    def __init__(self, url, list, mail, password) :
        self.site_url = url
        self.sp_list = list
        self.ctx = ClientContext(self.site_url).with_credentials(UserCredential(mail, password))
    
    def collect(self) :
        sp_lists = self.ctx.web.lists
        s_list = sp_lists.get_by_title(self.sp_list)
        l_items = s_list.get_items()
        self.ctx.load(l_items)
        self.ctx.execute_query()

        # Remove junk entries 
        ls=['FileSystemObjectType','ServerRedirectedEmbedUri','ServerRedirectedEmbedUrl','ID','ContentTypeId','Modified','Created','AuthorId','EditorId','OData__UIVersionString','Attachments','GUID', 'ComplianceAssetId']
        l=[]
        DATA=[]
        for item in l_items:
            l.append(item.properties)
        for dic in l:
            DATADIC={}
            for ele in dic:
                if ele not in ls:
                    dat=dic.get(ele)
                    DATADIC[ele]=dat
            DATA.append(DATADIC)

        return DATA