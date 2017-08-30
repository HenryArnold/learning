import web
import aService
import sys
  
urls = ("/Service/A","hello")
app = web.application(urls,globals())
  
class hello:
    def GET(self):
        mservice = aService.AService()
        result = mservice.getA(1)
        json = ""
        json +="{"
        json +="'id':"+str(result[0])+","
        json +="'code':'"+result[1]+"',"
        json +="'title':'"+result[2]+"'"
        json +="}"
        return json;
if __name__=="__main__":
    app.run()