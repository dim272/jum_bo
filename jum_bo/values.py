"""
In a real project I would use yaml or dotenv
"""

PROXY_API = "api_key"

GRAPHQL_QUERY = "\n  fragment productFields on Product {\n    id: sku\n    brand\n    category\n    subtitle: " \
                "packSizeDisplay\n    title\n    image\n    inAssortment\n    availability {\n      availability\n    " \
                "  isAvailable\n      label\n    }\n    isAvailable\n    isSponsored\n    link\n    status\n    " \
                "retailSet\n    prices: price {\n      price\n      promoPrice\n      pricePerUnit {\n        price\n " \
                "       unit\n      }\n    }\n    crossSellSkus\n    quantityDetails {\n      maxAmount\n      " \
                "minAmount\n      stepAmount\n      defaultAmount\n      unit\n    }\n    quantityOptions {\n      " \
                "maxAmount\n      minAmount\n      stepAmount\n      unit\n    }\n    primaryBadge: primaryBadges {\n " \
                "     alt\n      image\n    }\n    secondaryBadges {\n      alt\n      image\n    }\n    promotions {" \
                "\n      id\n      group\n      isKiesAndMix\n      image\n      tags {\n        text\n        " \
                "inverse\n      }\n      start {\n        dayShort\n        date\n        monthShort\n      }\n      " \
                "end {\n        dayShort\n        date\n        monthShort\n      }\n      attachments{\n        " \
                "type\n        path\n      }\n    }\n  }\n\n  query searchResult(\n    $searchTerms: String\n    " \
                "$filters: String\n    $offSet: Int\n    $showMoreIds: String\n    $sortOption: String\n    " \
                "$pageSize: Int\n    $categoryUrl: String\n  ) {\n    searchResult(\n      searchTerms: " \
                "$searchTerms\n      filters: $filters\n      offSet: $offSet\n      showMoreIds: $showMoreIds\n      " \
                "sortOption: $sortOption\n      pageSize: $pageSize\n      categoryUrl: $categoryUrl\n    ) {\n      " \
                "canonicalRelativePath\n      categoryTiles {\n        id\n        label\n        imageLink\n        " \
                "navigationState\n        siteRootPath\n      }\n      urlState\n      newUrl\n      redirectUrl\n    " \
                "  shelfDescription\n      powerFilters {\n        displayName\n        navigationState\n        " \
                "siteRootPath\n      }\n      metaData {\n        title\n        description\n      }\n      " \
                "headerContent {\n        headerText\n        count\n      }\n      helperText {\n        show\n      " \
                "  shortBody\n        longBody\n        header\n        linkText\n        targetUrl\n        " \
                "messageType\n      }\n      recipeLink {\n        linkText\n        targetUrl\n        textIsRich\n  " \
                "    }\n      guidedNavigation {\n        displayName\n        dimensionName\n        groupName\n     " \
                "   name\n        multiSelect\n        moreLink {\n          label\n          navigationState\n       " \
                " }\n        lessLink {\n          label\n          navigationState\n        }\n        refinements {" \
                "\n          label\n          count\n          multiSelect\n          navigationState\n          " \
                "siteRootPath\n        }\n      }\n      selectedRefinements {\n        refinementCrumbs {\n          " \
                "label\n          count\n          multiSelect\n          dimensionName\n          ancestors {\n      " \
                "      label\n            navigationState\n          }\n          removeAction {\n            " \
                "navigationState\n          }\n        }\n        searchCrumbs {\n         terms\n         " \
                "removeAction {\n          navigationState\n         }\n        }\n        removeAllAction {\n        " \
                " navigationState\n        }\n      }\n      socialLists {\n        title\n        totalNumRecs\n     " \
                "   lists {\n          id\n          title\n          followers\n          productImages\n          " \
                "thumbnail\n          author\n          labels\n          isAuthorVerified\n        }\n      }\n      " \
                "mainContent {\n        searchWarning\n        searchResultBanners {\n          isExternal\n          " \
                "id\n          text\n          buttonText\n          textColor\n          url\n          " \
                "imageDesktop\n          imageMobile\n          textIsRich\n          position\n        }\n        " \
                "searchAdjustments {\n          originalTerms\n          adjustedSearches {\n            key\n        " \
                "    terms {\n              autoPhrased\n              adjustedTerms\n              spellCorrected\n  " \
                "          }\n          }\n        }\n      }\n      productsResultList {\n        " \
                "pagingActionTemplate {\n          navigationState\n        }\n        lastRecNum\n        " \
                "totalNumRecs\n        sortOptions {\n          navigationState\n          label\n          " \
                "selected\n        }\n        products {\n          ...productFields\n          retailSetProducts {\n " \
                "           ...productFields\n          }\n        }\n      }\n    }\n  }\n "

REQUEST_BODY = {
            "operation": "searchResult",
            "variables": {
                "searchTerms": "",
                "sortOption": "",
                "showMoreIds": "",
                "offSet": 0,
                "pageSize": 25,
                "categoryUrl": None
            },
            "query": GRAPHQL_QUERY
        }

HEADERS = {
    "Origin": "https://www.jumbo.com",
    "Refer": "https://www.jumbo.com/producten/diepvries/",
    "Host": "www.jumbo.com",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
}