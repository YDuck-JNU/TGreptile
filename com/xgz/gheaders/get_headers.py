def tg_header(url):
    """
    用于骗过TG的请求头
    :param url: 需要传递https://t.me/后面的内容
    :return: 返回需要的请求头
    """
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 't.me',
        'Origin': 'https://t.me',
        'Referer': f'https://t.me/s/{url}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
    }
    return headers


def jd_header():
    """
    京东的请求头
    :return:
    """
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,or;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': '__jdu=16355948253331234440236; shshshfpa=e28592e6-0d6c-3127-167b-6865734f705c-1635594906; jcap_dvzw_fp=KJ5cszK4VlmduRhufXHB2FWh79Q1CVibncV39cxvfi5diPSOluJbJlg2tOI1V-r406tVGg==; TrackID=1SVkqbEDtHM4GWu-YwoF6FN4i84J6Vg-gkSuD4Zq8eTzHSbdtBZ7B8Hu_CAxWO03D9vK4G6jIoWPsGjamtQa9AeD6_ZydKj-pNymXCvk3k5A; mba_muid=16355948253331234440236; webp=1; visitkey=4891548280498072; qd_uid=L52DKFF7-BGA5YEL24KL4AFSDJ8A0; qd_fs=1656675078154; _gia_s_local_fingerprint=addfdffef1c609a58e2adb6de6fa9075; _gia_s_e_joint={"eid":"K7B7C5S47A7CI7PH3DLJF3W4MSMZIIESYUTRWNOF6E4DC7DMRCHB4XYU4S3MGAUR7NBIX32P365T4ZZ53L3OYCKXRU","ma":"","im":"","os":"Windows 10","ip":"173.82.226.17","ia":"","uu":"","at":"5"}; joyya=1656675113.1656675119.40.1rlrmuz; shshshfpb=ghDl7Dkw1akzUHMZt8zp%2FAA%3D%3D; buy_uin=200001099673961356; jdpin=wdXGOCPuRZOLOR; mcossmd=00379972eb8abb7a6f8b47d775dc4d4a; nickname=%E7%BE%BD; openid1=EABE483D41C1CF8E2CE810A62D670057682B3626ACACF60A54A42809B63173549228D2B71099710EBEBE908AD7CC58B7; picture_url=http%3A%2F%2Fthirdqq.qlogo.cn%2Fg%3Fb%3Doidb%26k%3Dg3y34Yfvh3eNfBB8PibHIiaA%26s%3D40%26t%3D1640702560; pin=wdXGOCPuRZOLOR; pinId=01xu8YZmNAypKZxb9yRrrg; pinStatus=1; pinsign=5df40d765484fca331b60d436bd1f6b1; sfstoken=tk01wa8041b41a8sMSsyKzMrMVZjb%2BEbq15TMPpnTxBI8O1bvZ2BLPehLM1gVLFCT0d1LzKDD2idbaG%2BddWd4f%2BrQ61Z; sq_open_id=000000000000000000000000AF0C9693; sq_sex=%u7537; wq_skey=zq7C6E57D11B3A4EF7C2D45596BD63816C10067BA959C4AAFEF5AC343645EA801C3097D7B342A00E86AF703B0B3D7CAE3B99212EA36C137BEEB825BD8A07B2B374; wq_uin=200001099673961356; wq_unionid=UID_0B118DBC06353F4303E2310B592DCFDB; rurl=%2F%2Fwq.jd.com%2Fpinbind%2FpinTokenRedirect%3Ftype%3D1%26biz%3Djm-business-center%26rurl%3Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fcommon%252FsaveWqToken%253Furl%253Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fwx%252FcompleteInfoActivity%252Fview%252Factivity%253FactivityId%253D65129c60660a4c5c8dde0e8be8664834%2526venderId%253D107615%26scope%3D0%26sceneid%3D9001%26btnTips%3D%26hideApp%3D0; qd_ad=sendbeans.jd.com%7C-%7Cjd%7C-%7C0; qd_ls=1657299705501; qd_ts=1658797888971; qd_sq=3; 3AB9D23F7A4B3C9B=K7B7C5S47A7CI7PH3DLJF3W4MSMZIIESYUTRWNOF6E4DC7DMRCHB4XYU4S3MGAUR7NBIX32P365T4ZZ53L3OYCKXRU; wxa_level=1; cid=9; jxsid=16588052773835470775; PPRD_P=UUID.16355948253331234440236; sc_width=1536; autoOpenApp_downCloseDate_auto=1658807620441_1800000; jxsid_s_u=https%3A//shop.m.jd.com/; RT="z=1&dm=jd.com&si=6liwbf38oww&ss=l61no5dq&sl=1&tt=0&obo=1&ld=16mk&r=ab6b1799d0c5dc31023804089362d978&ul=16mo&hd=188y"; shshshfp=c0212080262300201e5a1c67f7a5e7ea; retina=0; CCC_SE=ADC_LqbNNy19DMlT4XwvKiHgbrlKbpTTStit7Ax7PaNGlR8IoRj%2foM6etWLweH3cVWJAyjPlNz3EuxEhE6tT7GMgHaGKgpyjbYJr1vcAG0reZdFPx3xjtUmUtD33h7raarj5ikIUlaJXI4m8ynvljgzGE%2floC3L5IgVJqbatSozyiTk3dq9Xf12O729mVXINkEIOIOsDakevgLTC3nIhYfWDWyuWRMTsLhiFFUhPgB0ESgKLuDmtBIvEzPJ1Jwigys0Tku9enN1%2fMtj%2bGqjlDmrWVYWhl0w9aZl6iyWMb%2fK6QD61ohEWfjCwS1ZjOxaVhOV5Kv3R6G2dYEqRMSa0YTVyO%2bCFbIdC7PZHLJP%2boiYKpjferK5qbh9x1reBy0saPV%2bZyChwmracdcck8JCkfcvvcdT0IKjUvMhH%2bX7ynbe6jLbu1JwDPkd7RlfSYKggg5mPjI6sJ7z0UctmlFaFbPFaEwbC%2ftuJWMy7OANMiFwR7Wrf%2fMFlzp4XIjCl55a1TEq8; unpl=JF8EAKRnNSttWU4HBhJRGUUTT1oEW10LSh4GOjAFBlgPTVcCSwIdFEJ7XlVdXhRKER9sYBRUXlNJUw4eBisSEHteVV5cAE4fAW9nNWRVUCVIBVYCdRF-SBAZE20LSycCX2cCVllcQ1EMGAYZEBJLXlZbWA1KFAFoVzVUW2h7ZAQrAysTIAozVFdYCU4QTm9gB1BZUE5dBh8AGRAQSF9RW1gJSBUEX2Y1Vw; wqmnx1=MDEyNjM2MXQvbW9vN2FzY2VzPXVkaSZhbjExbT1iYTRmNzQ4OHo1aSAubjZwSzdLIEcgZTBTLzZGMm4tM1FVTyomSA%3D%3D; appCode=ms0ca95114; __jdb=122270672.11.16355948253331234440236|30.1658807960; __jdc=122270672; mba_sid=16588052827044705268607334503.13; __jd_ref_cls=MDownLoadFloat_TopOldExpo; __wga=1658810211092.1658805286801.1657188673007.1655394902615.11.8; __jdv=122270672%7Ckong%7Ct_2010949311_%7Cjingfen%7C04b28b3f256a412084df1c4f726a177c%7C1658810211095; __jda=122270672.16355948253331234440236.1635594825.1658807960.1658810211.31; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; _tj_rvurl=https%3A//wq.jd.com/mshop/homeindex%3FshopId%3D177256%26ad_od%3Dshare%26cu%3Dtrue%26utm_source%3Dkong%26utm_medium%3Djingfen%26utm_campaign%3Dt_2010949311_%26utm_term%3D04b28b3f256a412084df1c4f726a177c; jxsid_s_t=1658810211214; shshshsID=299e8da5e5da27288b21bdce73f33d94_11_1658810211835',
        'referer': 'https://u.jd.com/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'

    }
    return headers
