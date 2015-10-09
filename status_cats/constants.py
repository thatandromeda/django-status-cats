"""
A handy place to stash a dict of http status codes and cat pic URLs.

This includes all the cat pics found at
https://www.flickr.com/photos/girliemac/sets/72157628409467125/. There
are some RFC 7231 status codes not represented in here, and some
nonstandard codes (e.g. from WebDAV or Microsoft IIS) that are.

Yes, we could do http.cat for this, and get easier URLs, but Flickr is
more likely to stick around.
"""

CAT_URLS = {
    # HTTP_100_CONTINUE
    100: 'https://c2.staticflickr.com/8/7162/6512768893_a821929823_b.jpg',

    # HTTP_101_SWITCHING_PROTOCOLS
    101: 'https://c2.staticflickr.com/8/7022/6540479029_730c095b63_b.jpg',

    # HTTP_200_OK
    200: 'https://c2.staticflickr.com/8/7153/6512628175_6a4e8ab6ba_b.jpg',

    # HTTP_201_CREATED
    201: 'https://c2.staticflickr.com/8/7149/6540221577_ed29955a01_b.jpg',

    # HTTP_202_ACCEPTED
    202: 'https://c2.staticflickr.com/8/7167/6540479079_16e97a624a_b.jpg',

    # HTTP_204_NO_CONTENT
    204: 'https://c2.staticflickr.com/8/7154/6547319943_442c6509bb_b.jpg',

    # HTTP_206_PARTIAL_CONTENT
    206: 'https://c2.staticflickr.com/8/7021/6514473163_4e2a681cbd_b.jpg',

    # HTTP_207_MULTI_STATUS
    207: 'https://c2.staticflickr.com/8/7141/6514472979_c44518c4ce_b.jpg',

    # HTTP_300_MULTIPLE_CHOICES
    300: 'https://c2.staticflickr.com/8/7019/6519540181_d4eae6ee7a_b.jpg',

    # HTTP_301_MOVED_PERMANENTLY
    301: 'https://c2.staticflickr.com/8/7022/6519540231_73756bac6c_b.jpg',

    # HTTP_302_FOUND
    302: 'https://c2.staticflickr.com/8/7019/6508023829_3d44c4ac16_b.jpg',

    # HTTP_303_SEE_OTHER
    303: 'https://c2.staticflickr.com/8/7007/6513125065_ef7cfa6256_b.jpg',

    # HTTP_304_NOT_MODIFIED
    304: 'https://c2.staticflickr.com/8/7166/6540551929_eeee6bf3dd_b.jpg',

    # HTTP_305_USE_PROXY
    305: 'https://c2.staticflickr.com/8/7002/6540365403_01e93b44a3_b.jpg',

    # HTTP_307_TEMPORARY_REDIRECT
    307: 'https://c2.staticflickr.com/8/7161/6513001269_edff1f0079_b.jpg',

    # HTTP_400_BAD_REQUEST
    400: 'https://c2.staticflickr.com/8/7161/6513001269_edff1f0079_b.jpg',

    # HTTP_401_UNAUTHORIZED
    401: 'https://c2.staticflickr.com/8/7148/6508023065_8dae48a30b_b.jpg',

    # HTTP_402_PAYMENT_REQUIRED
    402: 'https://c2.staticflickr.com/8/7165/6513001321_8ecc400e0a_b.jpg',

    # HTTP_403_FORBIDDEN
    403: 'https://c2.staticflickr.com/8/7173/6508023617_f3ffc34e17_b.jpg',

    # HTTP_404_NOT_FOUND
    404: 'https://c2.staticflickr.com/8/7172/6508022985_b22200ced0_b.jpg',

    # HTTP_405_METHOD_NOT_ALLOWED
    405: 'https://c2.staticflickr.com/8/7175/6508023523_996188af86_b.jpg',

    # HTTP_406_NOT_ACCEPTABLE
    406: 'https://c2.staticflickr.com/8/7143/6508023119_b681209a58_b.jpg',

    # HTTP_408_REQUEST_TIMEOUT
    408: 'https://c2.staticflickr.com/8/7018/6508023179_bab3eebce8_b.jpg',

    # HTTP_409_CONFLICT
    409: 'https://c2.staticflickr.com/8/7010/6508023259_b1c6f5a353_b.jpg',

    # HTTP_410_GONE
    410: 'https://c2.staticflickr.com/8/7145/6514567755_1c5b7f575f_b.jpg',

    # HTTP_411_LENGTH_REQUIRED
    411: 'https://c2.staticflickr.com/8/7159/6540724141_7d78eae062_b.jpg',

    # HTTP_412_PRECONDITION_FAILED
    412: 'https://c2.staticflickr.com/6/5724/20403154863_8734524a4c_b.jpg',

    # HTTP_413_REQUEST_ENTITY_TOO_LARGE
    413: 'https://c2.staticflickr.com/8/7161/6508023747_1d60889626_b.jpg',

    # HTTP_414_REQUEST_URI_TOO_LONG
    414: 'https://c2.staticflickr.com/8/7152/6508023351_6732ed2f58_b.jpg',

    # HTTP_415_UNSUPPORTED_MEDIA_TYPE
    415: 'https://c2.staticflickr.com/6/5775/21031835411_802f2b5c75_b.jpg',

    # HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
    416: 'https://c2.staticflickr.com/8/7151/6513196851_10ef1d190e_b.jpg',

    # HTTP_417_EXPECTATION_FAILED
    417: 'https://c2.staticflickr.com/8/7009/6508023679_cb3e88fa92_b.jpg',

    # HTTP_418_I'M_A_TEAPOT
    # you didn't think I'd leave this one out did you
    418: 'https://c2.staticflickr.com/8/7006/6508102407_a4de65687b_b.jpg',

    # HTTP_422_UNPROCESSABLE_ENTITY
    422: 'https://c2.staticflickr.com/8/7004/6514473085_3c996d9594_b.jpg',

    # HTTP_423_LOCKED
    423: 'https://c2.staticflickr.com/8/7150/6514510235_8c2ee4965e_b.jpg',

    # HTTP_424_FAILED_DEPENDENCY
    424: 'https://c2.staticflickr.com/8/7165/6514584423_a9b13d6b70_b.jpg',

    # HTTP_425_UNORDERED_COLLECTION
    # Only used by Microsoft IIS
    425: 'https://c2.staticflickr.com/8/7013/6540586787_c7182a2bc1_b.jpg',

    # HTTP_426_UPGRADE_REQUIRED
    426: 'https://c2.staticflickr.com/8/7167/6509400771_33a1f59890_b.jpg',

    # HTTP_429_TOO_MANY_REQUESTS
    429: 'https://c2.staticflickr.com/8/7152/6509400997_25bb1bb4fb_b.jpg',

    # HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
    431: 'https://c2.staticflickr.com/8/7144/6509400689_a67d026d0a_b.jpg',

    # HTTP_444_NO_RESPONSE
    444: 'https://c2.staticflickr.com/8/7152/6509400599_52ca022f98_b.jpg',

    # HTTP_450_BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS
    450: 'https://c2.staticflickr.com/8/7151/6513125123_dd582f5c2a_b.jpg',

    # HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
    451: 'https://c2.staticflickr.com/6/5527/9113233540_cb36fb659c_b.jpg',

    # HTTP_500_INTERNAL_SERVER_ERROR
    500: 'https://c2.staticflickr.com/8/7001/6509400855_aaaf915871_b.jpg',

    # HTTP_502_BAD_GATEWAY
    502: 'https://c2.staticflickr.com/8/7158/6508023429_735b433a36_b.jpg',

    # HTTP_503_SERVICE_UNAVAILABLE
    503: 'https://c2.staticflickr.com/8/7157/6540643319_7945715c3a_b.jpg',

    # HTTP_506_VARIANT_ALSO_NEGOTIATES
    506: 'https://c2.staticflickr.com/8/7155/6540643279_d5126cd8f6_b.jpg',

    # HTTP_507_INSUFFICIENT_STORAGE
    507: 'https://c2.staticflickr.com/8/7160/6509400503_648dc8a2e5_b.jpg',

    # HTTP_508_LOOP_DETECTED
    508: 'https://c2.staticflickr.com/8/7025/6509400445_5fd9c7a9c3_b.jpg',

    # HTTP_509_BANDWIDTH_LIMIT_EXCEEDED
    509: 'https://c2.staticflickr.com/8/7154/6540399865_7bb98e69d2_b.jpg',

    # HTTP_599_NETWORK_CONNECT_TIMEOUT_ERROR
    599: 'https://c2.staticflickr.com/8/7033/6509400929_57ec73af05_b.jpg',
}

"""
The following codes are part of RFC 7231, but have no cat pics:
    HTTP_203_NON_AUTHORITATIVE_INFORMATION
    HTTP_205_RESET_CONTENT
    HTTP_306_RESERVED (reserved, but unused)
    HTTP_501_NOT_IMPLEMENTED
    HTTP_504_GATEWAY_TIMEOUT
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED

The following codes are part of other RFCs, but have no cat pics:
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED (RFC 7235)
    HTTP_428_PRECONDITION_REQUIRED (RFC 6585)
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED (RFC 6585)

"""
