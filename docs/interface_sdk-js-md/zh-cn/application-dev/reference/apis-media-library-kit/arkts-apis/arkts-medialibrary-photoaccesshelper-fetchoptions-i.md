# FetchOptions

Defines the retrieval options.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface FetchOptions--><!--Device-photoAccessHelper-interface FetchOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## fetchColumns

```TypeScript
fetchColumns: Array<string>
```

Names of the columns specified for query.

If this parameter is left blank for photos, photos are fetched by **'uri'**, **'media_type'**, **'subtype'**, and  
**'display_name'** by default. An error will be thrown if   
[get](arkts-medialibrary-photoaccesshelper-photoasset-i.md#get) is used to obtain other attributes of this object. 

Example: **fetchColumns: ['uri', 'title']**.

If this parameter is left blank for albums, albums are fetched by **'uri'** and **'album_name'** by default.

**类型：** Array&lt;string&gt;

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchOptions-fetchColumns: Array<string>--><!--Device-FetchOptions-fetchColumns: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## predicates

```TypeScript
predicates: dataSharePredicates.DataSharePredicates
```

Predicates that specify the fetch criteria.

**类型：** dataSharePredicates.DataSharePredicates

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchOptions-predicates: dataSharePredicates.DataSharePredicates--><!--Device-FetchOptions-predicates: dataSharePredicates.DataSharePredicates-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

