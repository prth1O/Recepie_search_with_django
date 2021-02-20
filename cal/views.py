from django.shortcuts import render
from django.http import request,HttpResponse


from py_edamam import Edamam
# Create your views here.






def home(request):

    e = Edamam(nutrition_appid='33e2b843',
           nutrition_appkey='19cabd42f85ab1dd7a2c5075f2148bf7',
           recipes_appid='d2b39e3b',
           recipes_appkey='003a3b450bee5ae5c3977c81be5423bf',
           food_appid='b9689b5b',
           food_appkey='d7d6a5e7d612f7d7395df93d82008e79')


    query=request.POST.get('search_q',None)




    s=e.search_recipe(str(query))

    res=return_list(s)

    return  render(request,'temp1.html',{'res':res})
def return_values(path):
            dic_res={}
            for key,val in path.items():
                if key=='calories':
                    dic_res['cal']=round(val,2)

                if key== 'image':
                    dic_res['img']=val


                if key=='ingredientLines':
                    dic_res['ingr']=val
                if key=='label':
                    dic_res['label']=val
                if key=='url':
                    dic_res['url']=val
                if key=='totalWeight':
                    dic_res['totalWeight']=round(val,2)

            return dic_res

def CFP(path2):
    neut={}
    for i in path2:
        for key,val in i.items():
            if key=='label' and val=='Fat':
                neut['Fat']=round(i['total'],2)

            if key=='label' and val=='Carbs':
                neut['Carbs']=round(i['total'],2)

            if key=='label' and val=='Protein':
                neut['Protein']=round(i['total'],2)

    return neut


def return_list(json_dict):
    res_L=[]
    for i in range(len(json_dict)):
        path=json_dict['hits'][i]['recipe']
        path2=json_dict['hits'][i]['recipe']['digest']
        res_dict1=return_values(path)
        res_dict2=CFP(path2)
        res_dict1['Neut']=res_dict2
        res_L.append(res_dict1)
    return res_L
