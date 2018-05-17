from auth import api

DUB_WOE_ID = 560743
LON_WOE_ID = 44418    
GLA_WOE_ID = 21125   


def get_trending_by_woe(WOE_ID):
    trending = api.trends_place(WOE_ID)
    set_of_trends = set()
    for trend in trending[0]['trends']:
        set_of_trends.add(trend['name'])
    return set_of_trends
        
trending_in_dublin = get_trending_by_woe(560743)
trending_in_london = get_trending_by_woe(44418)
trending_in_glasgow = get_trending_by_woe(21125)
trending_in_both = trending_in_glasgow.intersection(trending_in_dublin)
trending_in_all = trending_in_both.intersection(trending_in_london)

print(trending_in_both)

