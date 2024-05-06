SHA_IN_PARAMETERS = (
    # https://shared.ecom-psp.com/v2/docs/guides/e-Commerce/SHA-IN_params_24092019.txt
    "ACCEPTANCE",
    "ACCEPTURL",
    "ADDMATCH",
    "ADDRMATCH",
    "AIACTIONNUMBER",
    "AIAGIATA",
    "AIAIRNAME",
    "AIAIRTAX",
    "AIBOOKIND*XX*",
    "AICARRIER*XX*",
    "AICHDET",
    "AICLASS*XX*",
    "AICONJTI",
    "AIDEPTCODE",
    "AIDESTCITY*XX*",
    "AIDESTCITYL*XX*",
    "AIEXTRAPASNAME*XX*",
    "AIEYCD",
    "AIFLDATE*XX*",
    "AIFLNUM*XX*",
    "AIGLNUM",
    "AIINVOICE",
    "AIIRST",
    "AIORCITY*XX*",
    "AIORCITYL*XX*",
    "AIPASNAME",
    "AIPROJNUM",
    "AISTOPOV*XX*",
    "AITIDATE",
    "AITINUM",
    "AITINUML*XX*",
    "AITYPCH",
    "AIVATAMNT",
    "AIVATAPPL",
    "ALIAS",
    "ALIASOPERATION",
    "ALIASPERSISTEDAFTERUSE",
    "ALIASUSAGE",
    "ALLOWCORRECTION",
    "AMOUNT",
    "AMOUNT*XX*",
    "AMOUNTHTVA",
    "AMOUNTTVA",
    "ARP_TRN",
    "BACKURL",
    "BATCHID",
    "BGCOLOR",
    "BLVERNUM",
    "BIC",
    "BIN",
    "BRAND",
    "BRANDVISUAL",
    "BROWSERACCEPTHEADER",
    "BROWSERCOLORDEPTH",
    "BROWSERJAVAENABLED",
    "BROWSERJAVASCRIPTENABLED",
    "BROWSERLANGUAGE",
    "BROWSERSCREENHEIGHT",
    "BROWSERSCREENWIDTH",
    "BROWSERTIMEZONE",
    "BROWSERUSERAGENT",
    "BUTTONBGCOLOR",
    "BUTTONTXTCOLOR",
    "CANCELURL",
    "CARDNO",
    "CATALOGURL",
    "CAVV_3D",
    "CAVVALGORITHM_3D",
    "CERTID",
    "CHECK_AAV",
    "CIVILITY",
    "CN",
    "COF_INITIATOR",
    "COF_RECURRING_EXPIRY",
    "COF_RECURRING_FREQUENCY",
    "COF_SCHEDULE",
    "COF_TRANSACTION",
    "COM",
    "COMPLUS",
    "CONVCCY",
    "COSTCENTER",
    "COSTCODE",
    "CREDITCODE",
    "CREDITDEBIT",
    "CUID",
    "CURRENCY",
    "CVC",
    "CVCFLAG",
    "DATA",
    "DATATYPE",
    "DATEIN",
    "DATEOUT",
    "DBXML",
    "DCC_COMMPERC",
    "DCC_CONVAMOUNT",
    "DCC_CONVCCY",
    "DCC_EXCHRATE",
    "DCC_EXCHRATETS",
    "DCC_INDICATOR",
    "DCC_MARGINPERC",
    "DCC_REF",
    "DCC_SOURCE",
    "DCC_VALID",
    "DECLINEURL",
    "DELIVERYDATE",
    "DEVICE",
    "DISCOUNTRATE",
    "DISPLAYMODE",
    "ECI",
    "ECI_3D",
    "ECOM_BILLTO_COMPANY",
    "ECOM_BILLTO_POSTAL_CITY",
    "ECOM_BILLTO_POSTAL_COUNTRYCODE",
    "ECOM_BILLTO_POSTAL_COUNTY",
    "ECOM_BILLTO_POSTAL_NAME_FIRST",
    "ECOM_BILLTO_POSTAL_NAME_LAST",
    "ECOM_BILLTO_POSTAL_NAME_PREFIX",
    "ECOM_BILLTO_POSTAL_POSTALCODE",
    "ECOM_BILLTO_POSTAL_STREET_LINE1",
    "ECOM_BILLTO_POSTAL_STREET_LINE2",
    "ECOM_BILLTO_POSTAL_STREET_LINE3",
    "ECOM_BILLTO_POSTAL_STREET_NUMBER",
    "ECOM_BILLTO_TELECOM_MOBILE_NUMBER",
    "ECOM_BILLTO_TELECOM_PHONE_NUMBER",
    "ECOM_CONSUMERID",
    "ECOM_CONSUMER_GENDER",
    "ECOM_CONSUMEROGID",
    "ECOM_CONSUMERORDERID",
    "ECOM_CONSUMERUSERALIAS",
    "ECOM_CONSUMERUSERPWD",
    "ECOM_CONSUMERUSERID",
    "ECOM_ESTIMATEDDELIVERYDATE",
    "ECOM_ESTIMATEDELIVERYDATE",
    "ECOM_PAYMENT_CARD_EXPDATE_MONTH",
    "ECOM_PAYMENT_CARD_EXPDATE_YEAR",
    "ECOM_PAYMENT_CARD_NAME",
    "ECOM_PAYMENT_CARD_VERIFICATION",
    "ECOM_SHIPMETHOD",
    "ECOM_SHIPMETHODDETAILS",
    "ECOM_SHIPMETHODSPEED",
    "ECOM_SHIPMETHODTYPE",
    "ECOM_SHIPTO_COMPANY",
    "ECOM_SHIPTO_DOB",
    "ECOM_SHIPTO_ONLINE_EMAIL",
    "ECOM_SHIPTO_POSTAL_CITY",
    "ECOM_SHIPTO_POSTAL_COUNTRYCODE",
    "ECOM_SHIPTO_POSTAL_COUNTY",
    "ECOM_SHIPTO_POSTAL_NAME_FIRST",
    "ECOM_SHIPTO_POSTAL_NAME_LAST",
    "ECOM_SHIPTO_POSTAL_NAME_PREFIX",
    "ECOM_SHIPTO_POSTAL_POSTALCODE",
    "ECOM_SHIPTO_POSTAL_STATE",
    "ECOM_SHIPTO_POSTAL_STREET_LINE1",
    "ECOM_SHIPTO_POSTAL_STREET_LINE2",
    "ECOM_SHIPTO_POSTAL_STREET_NUMBER",
    "ECOM_SHIPTO_TELECOM_FAX_NUMBER",
    "ECOM_SHIPTO_TELECOM_MOBILE_NUMBER",
    "ECOM_SHIPTO_TELECOM_PHONE_NUMBER",
    "ECOM_SHIPTO_TVA",
    "ED",
    "EMAIL",
    "EXCEPTIONURL",
    "EXCLPMLIST",
    "EXECUTIONDATE*XX*",
    "FACEXCL*XX*",
    "FACTOTAL*XX*",
    "FIRSTCALL",
    "FLAG3D",
    "FONTTYPE",
    "FORCECODE1",
    "FORCECODE2",
    "FORCECODEHASH",
    "FORCEPROCESS",
    "FORCETP",
    "FP_ACTIV",
    "GENERIC_BL",
    "GIROPAY_ACCOUNT_NUMBER",
    "GIROPAY_BLZ",
    "GIROPAY_OWNER_NAME",
    "GLOBORDERID",
    "GUID",
    "HDFONTTYPE",
    "HDTBLBGCOLOR",
    "HDTBLTXTCOLOR",
    "HEIGHTFRAME",
    "HOMEURL",
    "HTTP_ACCEPT",
    "HTTP_USER_AGENT",
    "INCLUDE_BIN",
    "INCLUDE_COUNTRIES",
    "INITIAL_REC_TRN",
    "INVDATE",
    "INVDISCOUNT",
    "INVLEVEL",
    "INVORDERID",
    "ISSUERID",
    "IST_MOBILE",
    "ITEM_COUNT",
    "ITEMATTRIBUTES*XX*",
    "ITEMCATEGORY*XX*",
    "ITEMCOMMENTS*XX*",
    "ITEMDESC*XX*",
    "ITEMDISCOUNT*XX*",
    "ITEMFDMPRODUCTCATEG*XX*",
    "ITEMID*XX*",
    "ITEMNAME*XX*",
    "ITEMPRICE*XX*",
    "ITEMQUANT*XX*",
    "ITEMQUANTORIG*XX*",
    "ITEMUNITOFMEASURE*XX*",
    "ITEMVAT*XX*",
    "ITEMVATCODE*XX*",
    "ITEMWEIGHT*XX*",
    "LANGUAGE",
    "LEVEL1AUTHCPC",
    "LIDEXCL*XX*",
    "LIMITCLIENTSCRIPTUSAGE",
    "LINE_REF",
    "LINE_REF1",
    "LINE_REF2",
    "LINE_REF3",
    "LINE_REF4",
    "LINE_REF5",
    "LINE_REF6",
    "LIST_BIN",
    "LIST_COUNTRIES",
    "LOGO",
    "MANDATEID",
    "MAXITEMQUANT*XX*",
    "MERCHANTID",
    "MODE",
    "MPI.CARDHOLDERACCOUNTAGEINDICATOR",
    "MPI.CARDHOLDERACCOUNTCHANGE",
    "MPI.CARDHOLDERACCOUNTCHANGEINDICATOR",
    "MPI.CARDHOLDERACCOUNTDATE",
    "MPI.CARDHOLDERACCOUNTPASSWORDCHANGE",
    "MPI.CARDHOLDERACCOUNTPASSWORDCHANGEINDICATOR",
    "MPI.CHALLENGEWINDOWSIZE",
    "MPI.DELIVERYEMAILADDRESS",
    "MPI.DELIVERYTIMEFRAME",
    "MPI.GIFTCARDAMOUNT",
    "MPI.GIFTCARDCOUNT",
    "MPI.GIFTCARDCURRENCY",
    "MPI.HOMEPHONE.COUNTRYCODE",
    "MPI.HOMEPHONE.SUBSCRIBER",
    "MPI.MOBILEPHONE.COUNTRYCODE",
    "MPI.MOBILEPHONE.SUBSCRIBER",
    "MPI.MERCHANTFRAUDRATE",
    "MPI.NUMBEROFPURCHASEWITHACCOUNTINTHELASTSIXMONTHS",
    "MPI.PAYMENTACCOUNTAGE",
    "MPI.PAYMENTACCOUNTAGEINDICATOR",
    "MPI.PREORDERDATE",
    "MPI.PREORDERPURCHASEINDICATOR",
    "MPI.PROVISIONATTEMPTSINTHELAST24HOURS",
    "MPI.REORDERITEMSINDICATOR",
    "MPI.SECURECORPORATEPAYMENT",
    "MPI.SHIPPINGADDRESSUSAGE",
    "MPI.SHIPPINGADDRESSWASFIRSTUSED",
    "MPI.SHIPPINGINDICATOR",
    "MPI.SHIPPINGNAMEANDCARDHOLDERNAMEAREIDENTICAL",
    "MPI.SUSPICIOUSACCOUNTACTIVITYDETECTED",
    "MPI.THREEDSREQUESTORAUTHENTICATIONDATA",
    "MPI.THREEDSREQUESTORAUTHENTICATIONMETHOD",
    "MPI.THREEDSREQUESTORAUTHENTICATIONTIMESTAMP",
    "MPI.THREEDSREQUESTORCHALLENGEINDICATOR",
    "MPI.THREEDSREQUESTORPRIORAUTHENTICATIONDATA",
    "MPI.THREEDSREQUESTORPRIORAUTHENTICATIONMETHOD",
    "MPI.THREEDSREQUESTORPRIORAUTHENTICATIONTIMESTAMP",
    "MPI.THREEDSREQUESTORPRIORREFERENCE",
    "MPI.TRANSACTIONACTIVITYINTHELAST24HOURS",
    "MPI.TRANSACTIONACTIVITYLASTYEAR ",
    "MPI.TRANSACTIONTYPE",
    "MPI.WORKPHONE.COUNTRYCODE",
    "MPI.WORKPHONE.SUBSCRIBER",
    "MTIME",
    "MVER",
    "NETAMOUNT",
    "OPERATION",
    "ORDERID",
    "ORDERSHIPCOST",
    "ORDERSHIPMETH",
    "ORDERSHIPTAX",
    "ORDERSHIPTAXCODE",
    "ORIG",
    "OR_INVORDERID",
    "OR_ORDERID",
    "OWNERADDRESS",
    "OWNERCTY",
    "OWNERTELNO",
    "OWNERTOWN",
    "OWNERZIP",
    "PAIDAMOUNT",
    "PARAMPLUS",
    "PARAMVAR",
    "PAYID",
    "PAYMETHOD",
    "PM",
    "PMLIST",
    "PMLISTPMLISTTYPE",
    "PMLISTTYPE",
    "PMLISTTYPEPMLIST",
    "PMTYPE",
    "POPUP",
    "POST",
    "PSPID",
    "PSWD",
    "RECIPIENTACCOUNTNUMBER",
    "RECIPIENTDOB",
    "RECIPIENTLASTNAME",
    "RECIPIENTZIP",
    "REF",
    "REFER",
    "REFID",
    "REFKIND",
    "REF_CUSTOMERID",
    "REF_CUSTOMERREF",
    "REGISTRED",
    "REMOTE_ADDR",
    "REQGENFIELDS",
    "REQUESTCOMPLETIONID",
    "RNPOFFERT",
    "RTIMEOUT",
    "RTIMEOUTREQUESTEDTIMEOUT",
    "SCORINGCLIENT",
    "SEQUENCETYPE",
    "SETT_BATCH",
    "SID",
    "SIGNDATE",
    "STATUS_3D",
    "SUBSCRIPTION_ID",
    "SUB_AM",
    "SUB_AMOUNT",
    "SUB_COM",
    "SUB_COMMENT",
    "SUB_CUR",
    "SUB_ENDDATE",
    "SUB_ORDERID",
    "SUB_PERIOD_MOMENT",
    "SUB_PERIOD_MOMENT_M",
    "SUB_PERIOD_MOMENT_WW",
    "SUB_PERIOD_NUMBER",
    "SUB_PERIOD_NUMBER_D",
    "SUB_PERIOD_NUMBER_M",
    "SUB_PERIOD_NUMBER_WW",
    "SUB_PERIOD_UNIT",
    "SUB_STARTDATE",
    "SUB_STATUS",
    "TAAL",
    "TAXINCLUDED*XX*",
    "TBLBGCOLOR",
    "TBLTXTCOLOR",
    "TID",
    "TITLE",
    "TOTALAMOUNT",
    "TP",
    "TRACK2",
    "TXTBADDR2",
    "TXTCOLOR",
    "TXTOKEN",
    "TXTOKENTXTOKENPAYPAL",
    "TXSHIPPING",
    "TXSHIPPINGLOCATIONPROFILE",
    "TXURL",
    "TXVERIFIER",
    "TYPE_COUNTRY",
    "UCAF_AUTHENTICATION_DATA",
    "UCAF_PAYMENT_CARD_CVC2",
    "UCAF_PAYMENT_CARD_EXPDATE_MONTH",
    "UCAF_PAYMENT_CARD_EXPDATE_YEAR",
    "UCAF_PAYMENT_CARD_NUMBER",
    "USERID",
    "USERTYPE",
    "VERSION",
    "WBTU_MSISDN",
    "WBTU_ORDERID",
    "WEIGHTUNIT",
    "WIN3DS",
    "WITHROOT",
    "XDL",
)

SHA_OUT_PARAMETERS = (
    # https://shared.ecom-psp.com/v2/docs/guides/e-Commerce/SHA-OUT_params.txt
    "AAVADDRESS",
    "AAVCHECK",
    "AAVMAIL",
    "AAVNAME",
    "AAVPHONE",
    "AAVZIP",
    "ACCEPTANCE",
    "ALIAS",
    "AMOUNT",
    "BIC",
    "BIN",
    "BRAND",
    "CARDNO",
    "CCCTY",
    "CN",
    "COLLECTOR_BIC",
    "COLLECTOR_IBAN",
    "COMPLETIONID",
    "COMPLUS",
    "CREATION_STATUS",
    "CREDITDEBIT",
    "CURRENCY",
    "CVCCHECK",
    "DCC_COMMPERCENTAGE",
    "DCC_CONVAMOUNT",
    "DCC_CONVCCY",
    "DCC_EXCHRATE",
    "DCC_EXCHRATESOURCE",
    "DCC_EXCHRATETS",
    "DCC_INDICATOR",
    "DCC_MARGINPERCENTAGE",
    "DCC_VALIDHOURS",
    "DEVICEID",
    "DIGESTCARDNO",
    "ECI",
    "ED",
    "EMAIL",
    "ENCCARDNO",
    "FXAMOUNT",
    "FXCURRENCY",
    "IP",
    "IPCTY",
    "MANDATEID",
    "MOBILEMODE",
    "NBREMAILUSAGE",
    "NBRIPUSAGE",
    "NBRIPUSAGE_ALLTX",
    "NBRUSAGE",
    "NCERROR",
    "ORDERID",
    "PAYID",
    "PAYIDSUB",
    "PAYMENT_REFERENCE",
    "PM",
    "REQUESTCOMPLETIONID",
    "SCO_CATEGORY",
    "SCORING",
    "SEQUENCETYPE",
    "SIGNDATE",
    "STATUS",
    "SUBBRAND",
    "SUBSCRIPTION_ID",
    "TICKET",
    "TRXDATE",
    "VC",
)

STATUSES = {
    0: "Invalid or incomplete",
    1: "Cancelled by customer",
    2: "Authorisation declined",
    4: "Order stored",
    40: "Stored waiting external result",
    41: "Waiting for client payment",
    46: "Waiting authentication",
    5: "Authorised",
    50: "Authorized waiting external result",
    51: "Authorisation waiting",
    52: "Authorisation not known",
    55: "Standby",
    56: "OK with scheduled payments",
    57: "Not OK with scheduled payments",
    59: "Authoris. to be requested manually",
    6: "Authorised and cancelled",
    61: "Author. deletion waiting",
    62: "Author. deletion uncertain",
    63: "Author. deletion refused",
    64: "Authorised and cancelled",
    7: "Payment deleted",
    71: "Payment deletion pending",
    72: "Payment deletion uncertain",
    73: "Payment deletion refused",
    74: "Payment deleted",
    75: "Deletion handled by merchant",
    8: "Refund",
    81: "Refund pending",
    82: "Refund uncertain",
    83: "Refund refused",
    84: "Refund",
    85: "Refund handled by merchant",
    9: "Payment requested",
    91: "Payment processing",
    92: "Payment uncertain",
    93: "Payment refused",
    94: "Refund declined by the acquirer",
    95: "Payment handled by merchant",
    96: "Refund reversed",
    99: "Being processed",
}
PENDING_STATES = ("91", "92", "99")
