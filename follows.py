params = {
    'count': '100',
    'search_surface': 'follow_list_page',
}

params_xx = {
    'count': '100',
    'max_id': '200',
    'search_surface': 'follow_list_page',
}

response = requests.get('https://i.instagram.com/api/v1/friendships/468542719/followers/', params=params, cookies=cookies, headers=headers)
response100 = requests.get('https://i.instagram.com/api/v1/friendships/468542719/followers/', params=params_xx, cookies=cookies, headers=headers)

seguidores_name = response.json()
i=0
for s in seguidores_name['users']:
    #print(s['full_name'])
    i=i+1
    #print(i)
print('ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ')
seguidores_name100 = response100.json()
i=0
for s in seguidores_name100['users']:
    #print(s['full_name'])
    i=i+1
    #print(i)


#r = requests.get('https://www.instagram.com/graphql/query/?query_hash=56a7068fea504063273cc2120ffd54f3&variables=%7B%22id%22%3A%221476919210%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFBdzl5NGZscTZzUzh0R21jbGJENUJRYVkya0N5dTYxZmNMd0I1bUhSUkZkYUplZjVZZmZnTHp5TGNjSDJXSWM4N2M1Nk5tYTFzeVg2RXBCZWNhaFN1Uw%3D%3D%22%7D')
#r = requests.get('https://www.instagram.com/graphql/query/?query_id=17842794232208280&id=468542719&first=12&after='+ str(paging))

#print(a['data']['user']['edge_owner_to_timeline_media']['edges'])

# https://www.instagram.com/graphql/query/?query_hash=d4d88dc1500312af6f937f7b804c68c3&
# variables=%7B%22user_id%22%3A%22468542719%22%2C%22include_chaining%22%3Atrue%2C%22include_reel%22%3Atrue%2C%22
# include_suggested_users%22%3Afalse%2C%22include_logged_out_extras%22%3Afalse%2C%22
# include_highlight_reels%22%3Atrue%2C%22include_live_status%22%3Atrue%7D

# https://www.instagram.com/graphql/query/?query_id=17842794232208280&
# variables=%7B%22id%22%3A%22468542719%22%2C%22first%22%3A+12%2C%22
# after%22%3A+%22QVFDazFHYkFZZUQ4NndfYVFwbnZnZUl2clRQa1J2MGRucEhDYWpjcmxacE5jenFWckVPamVGX0x5cEJnQVlyM09PTmxHTFlMRW5BVDM5ZVlkdTVTc0daRg%3D%3D%22%7D


#https://gist.github.com/nownabe/202854eefce253d8eda0c4f79f1a645f
#https://carloshenriquereis-17318.medium.com/how-to-get-data-from-a-public-instagram-profile-edc6704c9b45
#https://curlconverter.com/

#https://levelup.gitconnected.com/automating-instagram-posts-with-python-and-instagram-graph-api-374f084b9f2b


#https://webscraping.ai/blog/instagram-scraping-in-2021
#https://instagram-private-api.readthedocs.io/en/latest/_modules/instagram_web_api/client.html
#https://scrapingfish.com/blog/scraping-instagram#pagination-with-instagram-graphql-api

#QVFBLXFqQUR1SVNKTDRhZ1lIVkJNWUlKY3prUU9ZWGR6N1NYbmp5aHgxaDZWWkM2U1hHS2VmMU1QLXpWU2xMcG1xOUtJLTZVQklHNmdBcTg1MTBhYmRaQQ==
#QVFBLXFqQUR1SVNKTDRhZ1lIVkJNWUlKY3prUU9ZWGR6N1NYbmp5aHgxaDZWWkM2U1hHS2VmMU1QLXpWU2xMcG1xOUtJLTZVQklHNmdBcTg1MTBhYmRaQQ==

