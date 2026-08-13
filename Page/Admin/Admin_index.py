from Base.Base import PageBase
class AdminINdex(PageBase):
    def open_index_page(self):
        url=self.base_url+'/admin'
        self.open_url(url)