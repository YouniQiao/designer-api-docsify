# FetchOptions

Defines the retrieval options.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface FetchOptions--><!--Device-photoAccessHelper-interface FetchOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## fetchColumns

```TypeScript
fetchColumns: Array<string>
```

Names of the columns specified for query.

If this parameter is left blank for photos, photos are fetched by **'uri'**, **'media\_type'**, **'subtype'**, and  
**'display\_name'** by default. An error will be thrown if  
[get]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is used to obtain other attributes of this object.

Example: **fetchColumns: ['uri', 'title']**.

If this parameter is left blank for albums, albums are fetched by **'uri'** and **'album\_name'** by default.

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchOptions-fetchColumns: Array<string>--><!--Device-FetchOptions-fetchColumns: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## predicates

```TypeScript
predicates: dataSharePredicates.DataSharePredicates
```

Predicates that specify the fetch criteria.

**Type:** dataSharePredicates.DataSharePredicates

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchOptions-predicates: dataSharePredicates.DataSharePredicates--><!--Device-FetchOptions-predicates: dataSharePredicates.DataSharePredicates-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

