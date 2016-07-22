swagger_link = "http://ks-inf-geo1.t2.tenet:8080/swagger.json"

test_data_geo_service = [
    {
        "title": "test_Positive",
        "operationId": "findStateByName",
        "parameters": {
            "state": "Texas"
        },
        "er": {
            "status_code": 200,
            "body": '{"countryIsoCode":"US","shortName":"TX","fullName":"Texas",city:["name", ["Dallas", "fghf", "fhfhfh"]}'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "findStateByName",
        "parameters": {
            "state": "121213"
        },
        "er": {
            "status_code": 400,
            "body": '<html>\n<head>\n<meta http-equiv="Content-Type" '
                    'content="text/html;charset=utf-8"/>\n<title>Error'
                    ' 400 Bad Request</title>\n</head>\n<body><h2>HTTP'
                    ' ERROR 400</h2>\n<p>Problem accessing /country/state/ROMAN_121213.'
                    ' Reason:\n<pre>    '
                    'Bad Request</pre></p>\n</body>\n</html>\n'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "findCountryByName",
        "parameters": {
            "country": "UA"
        },
        "er": {
            "status_code": 200,
            "body": '{"short2Name":"UA","short3Name":"UKR","fullName":"Ukraine"}'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "getCountryComboView",
        "parameters": {
            "name": "foo",
            "country": "UA"
        },
        "er": {
            "status_code": 200,
            "body": "<select name='foo' class='bodyText' style='width:280px'><option value='AD'>Andorra<option value='AF'>Afghanistan<option value='AG'>Antigua and Barbuda<option value='AI'>Anguilla<option value='AL'>Albania<option value='AM'>Armenia<option value='AO'>Angola<option value='AQ'>Antarctica<option value='AR'>Argentina<option value='AS'>American Samoa<option value='AU'>Australia<option value='AW'>Aruba<option value='AX'>�land Islands<option value='AZ'>Azerbaijan<option value='AT'>Austria<option value='DZ'>Algeria<option value='BS'>Bahamas<option value='BH'>Bahrain<option value='BD'>Bangladesh<option value='BB'>Barbados<option value='BY'>Belarus<option value='BE'>Belgium<option value='BZ'>Belize<option value='BJ'>Benin<option value='BM'>Bermuda<option value='BT'>Bhutan<option value='BO'>Plurinational State of Bolivia<option value='BQ'>Sint Eustatius and Saba Bonaire<option value='BA'>Bosnia and Herzegowina<option value='BW'>Botswana<option value='BV'>Bouvet Island<option value='BR'>Brazil<option value='IO'>British Indian Ocean Territory<option value='BN'>Brunei Darussalam<option value='BG'>Bulgaria<option value='BF'>Burkina Faso<option value='BI'>Burundi<option value='KH'>Cambodia<option value='CM'>Cameroon<option value='CA'>Canada<option value='CV'>Cape Verde<option value='KY'>Cayman Islands<option value='CF'>Central African Republic<option value='TD'>Chad<option value='CL'>Chile<option value='CN'>China<option value='CX'>Christmas Island<option value='CC'>Cocos  Islands<option value='CO'>Colombia<option value='KM'>Comoros<option value='CG'>Congo<option value='CD'>The Democratic Republic of The Congo<option value='CK'>Cook Islands<option value='CR'>Costa Rica<option value='CI'>C�te d'Ivoire<option value='HR'>Croatia<option value='CU'>Cuba<option value='CW'>Cura�ao<option value='CY'>Cyprus<option value='CZ'>Czech Republic<option value='DK'>Denmark<option value='DJ'>Djibouti<option value='DM'>Dominica<option value='DO'>Dominican Republic<option value='EC'>Ecuador<option value='EG'>Egypt<option value='SV'>El Salvador<option value='GQ'>Equatorial Guinea<option value='ER'>Eritrea<option value='EE'>Estonia<option value='ET'>Ethiopia<option value='FK'>Falkland Islands<option value='FO'>Faroe Islands<option value='FJ'>Fiji<option value='FI'>Finland<option value='FR'>France<option value='GF'>French Guiana<option value='PF'>French Polynesia<option value='TF'>French Southern Territories<option value='GA'>Gabon<option value='GM'>Gambia<option value='GE'>Georgia<option value='DE'>Germany<option value='GH'>Ghana<option value='GI'>Gibraltar<option value='GR'>Greece<option value='GL'>Greenland<option value='GD'>Grenada<option value='GP'>Guadeloupe<option value='GU'>Guam<option value='GT'>Guatemala<option value='GG'>Guernsey<option value='GN'>Guinea<option value='GW'>Guinea-bissau<option value='GY'>Guyana<option value='HT'>Haiti<option value='HM'>Heard and McDonald Islands<option value='VA'>Holy See<option value='HN'>Honduras<option value='HK'>Hong Kong<option value='HU'>Hungary<option value='IS'>Iceland<option value='IN'>India<option value='ID'>Indonesia<option value='IR'>Iran<option value='IQ'>Iraq<option value='IE'>Ireland<option value='IM'>Isle of Man<option value='IL'>Israel<option value='IT'>Italy<option value='JM'>Jamaica<option value='JP'>Japan<option value='JE'>Jersey<option value='JO'>Jordan<option value='KZ'>Kazakhstan<option value='KE'>Kenya<option value='KI'>Kiribati<option value='KP'>Democratic People's Republic of Korea<option value='KR'>Republic of Korea<option value='KW'>Kuwait<option value='KG'>Kyrgyzstan<option value='LA'>Lao People's Democratic Republic<option value='LV'>Latvia<option value='LB'>Lebanon<option value='LS'>Lesotho<option value='LR'>Liberia<option value='LY'>Libya<option value='LI'>Liechtenstein<option value='LT'>Lithuania<option value='LU'>Luxembourg<option value='MO'>Macao<option value='MK'>The Former Yugoslav Republic of Macedonia<option value='MG'>Madagascar<option value='MW'>Malawi<option value='MY'>Malaysia<option value='MV'>Maldives<option value='ML'>Mali<option value='MT'>Malta<option value='MH'>Marshall Islands<option value='MQ'>Martinique<option value='MR'>Mauritania<option value='MU'>Mauritius<option value='YT'>Mayotte<option value='MX'>Mexico<option value='FM'>Federated States of Micronesia<option value='MD'>Republic of Moldova<option value='MC'>Monaco<option value='MN'>Mongolia<option value='ME'>Montenegro<option value='MS'>Montserrat<option value='MA'>Morocco<option value='MZ'>Mozambique<option value='MM'>Myanmar<option value='NA'>Namibia<option value='NR'>Nauru<option value='NP'>Nepal<option value='NL'>Netherlands<option value='NC'>New Caledonia<option value='NZ'>New Zealand<option value='NI'>Nicaragua<option value='NE'>Niger<option value='NG'>Nigeria<option value='NU'>Niue<option value='NF'>Norfolk Island<option value='MP'>Northern Mariana Islands<option value='NO'>Norway<option value='OM'>Oman<option value='PK'>Pakistan<option value='PW'>Palau<option value='PS'>State of Palestine<option value='PA'>Panama<option value='PG'>Papua New Guinea<option value='PY'>Paraguay<option value='PE'>Peru<option value='PH'>Philippines<option value='PN'>Pitcairn<option value='PL'>Poland<option value='PT'>Portugal<option value='PR'>Puerto Rico<option value='QA'>Qatar<option value='RE'>R�union<option value='RO'>Romania<option value='RU'>Russian Federation<option value='RW'>Rwanda<option value='SH'>Ascension and Tristan Da Cunha Saint Helena<option value='BL'>Saint Barth�lemy<option value='KN'>Saint Kitts and Nevis<option value='LC'>Saint Lucia<option value='PM'>Saint Pierre and Miquelon<option value='VC'>Saint Vincent and The Grenadines<option value='WS'>Samoa<option value='SM'>San Marino<option value='ST'>S�o Tome and Principe<option value='SA'>Saudi Arabia<option value='SN'>Senegal<option value='RS'>Serbia<option value='SC'>Seychelles<option value='SL'>Sierra Leone<option value='SG'>Singapore<option value='SX'>Sint Maarten<option value='SK'>Slovakia<option value='SI'>Slovenia<option value='SB'>Solomon Islands<option value='SO'>Somalia<option value='ZA'>South Africa<option value='GS'>South Georgia and The South Sandwich Islands<option value='SS'>South Sudan<option value='ES'>Spain<option value='LK'>Sri Lanka<option value='SD'>Sudan<option value='SR'>Suriname<option value='SJ'>Svalbard and Jan Mayen Islands<option value='SZ'>Swaziland<option value='SE'>Sweden<option value='CH'>Switzerland<option value='SY'>Syrian Arab Republic<option value='TW'>Province of China Taiwan<option value='TJ'>Tajikistan<option value='TZ'>United Republic of Tanzania<option value='TH'>Thailand<option value='TL'>Timor-leste<option value='TG'>Togo<option value='TK'>Tokelau<option value='TO'>Tonga<option value='TT'>Trinidad and Tobago<option value='TN'>Tunisia<option value='TR'>Turkey<option value='TM'>Turkmenistan<option value='TC'>Turks and Caicos Islands<option value='TV'>Tuvalu<option value='UG'>Uganda<option value='UA' selected>Ukraine<option value='AE'>United Arab Emirates<option value='GB'>United Kingdom<option value='US'>United States<option value='UM'>United States Minor Outlying Islands<option value='UY'>Uruguay<option value='UZ'>Uzbekistan<option value='VU'>Vanuatu<option value='VE'>Bolivarian Republic of Venezuela<option value='VN'>Vietnam<option value='VG'>Virgin Islands, British<option value='VI'>Virgin Islands, US<option value='WF'>Wallis and Futuna Islands<option value='EH'>Western Sahara<option value='YE'>Yemen<option value='ZM'>Zambia<option value='ZW'>Zimbabwe</select>"
        }
    },
    {
        "title": "test_Positive_findCountryStateByName",
        "operationId": "findCountryStateByName",
        "parameters": {
            "country": "AU",
            "state": "NSW"
        },
        "er": {
            "status_code": 200,
            "body": '{"countryIsoCode":"AU","shortName":"NSW","fullName":"New South Wales"}'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "findCountryCityLocations",
        "parameters": {
            "country": "US",
            "city": "La Fayette"
        },
        "er": {
            "status_code": 200,
            "body": '[{"id":13290,"countryIsoCode":"US","region":"Georgia","city":"La Fayette","postalCode":"30728","dmaCode":"575","areaCode":"706","coordinates":{"geoHash":"dn5mkk29bb2u"}},{"id":116770,"countryIsoCode":"US","region":"New York","city":"La Fayette","postalCode":"13084","dmaCode":"555","areaCode":"315","coordinates":{"geoHash":"dr9u59hvpsqs"}},{"id":120477,"countryIsoCode":"US","region":"Illinois","city":"La Fayette","postalCode":"61449","dmaCode":"675","areaCode":"309","coordinates":{"geoHash":"dp218xpgndh1"}},{"id":122687,"countryIsoCode":"US","region":"Georgia","city":"La Fayette","postalCode":"30728","dmaCode":"575","areaCode":"706","coordinates":{"geoHash":"dn5mkk29bb2u"}},{"id":169548,"countryIsoCode":"US","region":"Kentucky","city":"La Fayette","postalCode":"42254","dmaCode":"659","areaCode":"931","coordinates":{"geoHash":"dn98su5p1w83"}},{"id":650717,"countryIsoCode":"US","region":"New York","city":"La Fayette","postalCode":"42254","dmaCode":"659","areaCode":"931","coordinates":{"geoHash":"dn98t33ntt41"}}]'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "findLocationByIP",
        "parameters": {
            "ip": "8.8.8.8",
        },
        "er": {
            "status_code": 200,
            "body": '{"id":2720,"countryIsoCode":"US","region":"California","city":"Mountain View","postalCode":"94040","dmaCode":"807","areaCode":"650","coordinates":{"geoHash":"9q9htvdhmpfk"}}'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "findStateCityLocations",
        "parameters": {
            "state": "New York",
            "city": "La Fayette"
        },
        "er": {
            "status_code": 200,
            "body": '<html>\n<head>\n<meta http-equiv="Content-Type" '
                    'content="text/html;charset=utf-8"/>\n<title>Error'
                    ' 400 Bad Request</title>\n</head>\n<body><h2>HTTP'
                    ' ERROR 400</h2>\n<p>Problem accessing /country/state/132.'
                    ' Reason:\n<pre>    '
                    'Bad Request</pre></p>\n</body>\n</html>\n'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "findZipLocations",
        "parameters": {
            "zip": "42254"
        },
        "er": {
            "status_code": 200,
            "body": '<html>\n<head>\n<meta http-equiv="Content-Type" '
                    'content="text/html;charset=utf-8"/>\n<title>Error'
                    ' 400 Bad Request</title>\n</head>\n<body><h2>HTTP'
                    ' ERROR 400</h2>\n<p>Problem accessing /country/state/MISHA132.'
                    ' Reason:\n<pre>    '
                    'Bad Request</pre></p>\n</body>\n</html>\n'
        }
    },
    {
        "title": "test_Positive",
        "operationId": "findGeoPhoneLocationByCountryCity",
        "parameters": {
            "country": "US",
            "city": "Boston",
        },
        "er": {
            "status_code": 200,
            "body": '{"countryIsoCode":"US","shortName":"TX","fullName":"Texas"}'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "findGeoPhoneLocationByCountryPhoneNumber",
        "parameters": {
            "country": "US",
            "phoneNumber": "7818498118"
        },
        "er": {
            "status_code": 200,
            "body": '<html>\n<head>\n<meta http-equiv="Content-Type" '
                    'content="text/html;charset=utf-8"/>\n<title>Error'
                    ' 400 Bad Request</title>\n</head>\n<body><h2>HTTP'
                    ' ERROR 400</h2>\n<p>Problem accessing /country/state/132.'
                    ' Reason:\n<pre>    '
                    'Bad Request</pre></p>\n</body>\n</html>\n'
        }
    },
    {
        "title": "test_Validator",
        "operationId": "findGeoPhoneLocationByPhoneNumber",
        "parameters": {
            "phoneNumber": "+17818498118"
        },
        "er": {
            "status_code": 200,
            "body": '<html>\n<head>\n<meta http-equiv="Content-Type" '
                    'content="text/html;charset=utf-8"/>\n<title>Error'
                    ' 400 Bad Request</title>\n</head>\n<body><h2>HTTP'
                    ' ERROR 400</h2>\n<p>Problem accessing /country/state/132.'
                    ' Reason:\n<pre>    '
                    'Bad Request</pre></p>\n</body>\n</html>\n'
        }
    },
]
