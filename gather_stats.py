from lib import lib

lib = lib({'token': 'tok_dev_zazBhSNjh7ivLcF65CCQQ2fvr2vMCuwmjW4gxPmw4mNF9USz6WPD992rdfVsHr3n'})

comp_ranks = {}



def calc_ranks(gamertag):
    # Query ranks
    ranked_stats = lib.halo.infinite['@0.3.8'].stats.csrs({
    'gamertag': gamertag,
    'season': 1
     })

    rank_open = ranked_stats['data'][0]['response']['current']['value']
    rank_controller_soloduo = ranked_stats['data'][1]['response']['current']['value']
    rank_kbm_soloduo = ranked_stats['data'][2]['response']['current']['value']

    return [rank_open, rank_controller_soloduo, rank_kbm_soloduo]

def parse_service_record_data(gamertag):
    service_record = lib.halo.infinite['@0.3.8'].stats['service-record'].multiplayer({
    'gamertag': gamertag,
    'filter': 'matchmade:pvp'
    })
  
    # service_record data pulls 
    kda = f"{service_record['data']['core']['kda']:.2f}"
    win_rate = f"{service_record['data']['win_rate']:.2f}"

    return [kda, win_rate]

def gather_all_stats(gamertag):
    kda_win_rate = parse_service_record_data(gamertag)
    kda = kda_win_rate[0]
    win_rate = kda_win_rate[1]
    ranked = calc_ranks(gamertag)
    ranked_open = ranked[0]
    kbm_sd = ranked[1]
    con_sd = ranked[2]
    return [kda, win_rate, ranked_open, kbm_sd, con_sd]
    # temp code for API
    #return [1111, 111, 1111, -1111, 1111]


