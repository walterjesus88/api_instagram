import sys
import os
import requests, json, datetime, csv, time
from pandas import json_normalize
import pandas as pd
from datetime import datetime
from cookies import HEADERS,COOKIES
cookies=COOKIES
headers=HEADERS
data=[]

class api_instagram:
    def __init__(self,cuenta,id):
        self.cuenta = cuenta
        self.id = id

    def user_profile(self):
        # response = requests.get('https://i.instagram.com/api/v1/feed/user/468542719/', params=params, cookies=cookies, headers=headers)
        print('estoy n profile')
        print(self.cuenta)
        print('estoy n profile')
    
        params = {
            'username': self.cuenta,
        }
        comentarios =[]

        try:
            response = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, cookies=cookies, headers=headers)
            res = response.json()
            nodes = res['data']['user']['edge_owner_to_timeline_media']['edges']
            paging = res['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            biography = res['data']['user']['biography']
            seguidos = res['data']['user']['edge_follow']['count']
            seguidores = res['data']['user']['edge_followed_by']['count']
            publicaciones= res['data']['user']['edge_owner_to_timeline_media']['count']
            fbid=res['data']['user']['fbid']
            self.id=res['data']['user']['id']
            cantidad_reels=res['data']['user']['highlight_reel_count']
            full_name=res['data']['user']['full_name']
            username=res['data']['user']['username']
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            #raise SystemExit(e)
            print(e)

        params = {
            "query_hash": "69cba40317214236af40e7efa697781d",
            "variables": '{"id":"'+self.id+'", "first":12,"after":"" }'
        }

        self.params=params      
        #return params


    # def detalle_carrousel(self,carrousel):
    #     for car in carrousel:
    #         print(car['id'])
    #         print(car['image_versions2']['candidates'][0]['url'])
    #         #comentarios.append({"carousel_id":car['id'], "url_carrousel":car['image_versions2']['candidates'][0]['url']})

    def detalle_comentario(self,items):
        
        for comment in items:     
            #print(ccc['comments']) 
            url = 'https://www.instagram.com/p/'+comment['code']+'/'
            #ts = df_comments['created'].apply(int)            
            if 'caption' in comment:               
                #print(comment)
                if not comment['caption'] == None:
                    if 'created_at' in comment['caption']:
                        created= datetime.utcfromtimestamp(comment['caption']['created_at']).strftime('%Y-%m-%d %H:%M:%S')
                                      
                    if 'created_at_utc' in comment['caption']:
                        created_at_utc= datetime.utcfromtimestamp(comment['caption']['created_at_utc']).strftime('%Y-%m-%d %H:%M:%S')

                    if 'text' in comment['caption']:
                        text = comment['caption']['text']

                    if  'content_type' in comment['caption']:
                        content_type = comment['caption']['content_type']
                else:
                    created=0
                    created_at_utc=0
                    text=''
                    content_type=''                
        
            if 'carousel_media_count' in comment:
                carousel_media_count=comment['carousel_media_count']
            else:
                carousel_media_count=0

            if 'view_count' in comment:    
                view_count=comment['view_count']
                video_duration=comment['video_duration']
            else:
                view_count=0
                video_duration=0
                
            #if 'carousel_media' in comment:
            #    detalle_carrousel(comment['carousel_media'])

            if 'comment_count' in comment:
                comment_count=comment['comment_count']
            else:
                comment_count=0

            comments = {"pk_comment":comment['pk'],
            "text": text,
            "created":created,
            "created_at_utc":created_at_utc,
            "content_type":content_type,
            "codex":url,"code_id":comment['id'],"like_count":comment['like_count'],
            "comment_count":comment_count,"carousel_media_count":carousel_media_count,
            "view_count":view_count,"video_duration":video_duration
            }           

        return comments

    def detalle_post(self,node_id):
        print(node_id)

        #snode_id=self.node_id
        try:
            comment_detail = requests.get('https://i.instagram.com/api/v1/media/'+node_id+'/info/', cookies=cookies, headers=headers)
            #r.raise_for_status()
            print(comment_detail)
            c = comment_detail.json()
            items= c['items']
            if items:
                #self.items=cc
                detalle = self.detalle_comentario(items)
            data.append(detalle)#,"edge_media_to_caption":n['node']['edge_media_to_caption']})
        except requests.exceptions.RequestException as e:
            print(e)
            print('Estas limitado por instagram')

    def nodes(self,a):    
        nodes = a['data']['user']['edge_owner_to_timeline_media']['edges']
        for n in nodes:        
            self.detalle_post(n['node']['id'])

    def data_extract(self):
        p=0
        params=self.params
        print('paramssssss')
        print(params)
        while(True):
            try:
                r = requests.get('https://www.instagram.com/graphql/query/', params=params, cookies=cookies, headers=headers)
                r.raise_for_status()
                p=p+1
                a=r.json()
                self.nodes(a)
                after = a['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
                params = {"query_hash": "69cba40317214236af40e7efa697781d", "variables": '{"id":"'+self.id+'", "first":12,"after":"'+after+'"}',}
                
                if after=="":
                    break
                if p == 3:
                    break            
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                print(e)
                break



if __name__ == "__main__":
    print("File one executed when ran directly")
    cuenta = str(input("Ingrese el nombre de la cuenta:  "))

    dat =api_instagram(cuenta,12)
    dat.user_profile()
    dat.data_extract()  

    df_comments = pd.DataFrame(data)
    df_comments.to_excel(cuenta+'.xlsx', index=False, encoding="ISO-8859-1")



 
