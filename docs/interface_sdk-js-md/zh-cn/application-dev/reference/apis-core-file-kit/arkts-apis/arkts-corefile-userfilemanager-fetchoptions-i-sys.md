# FetchOptions（系统接口）

Defines the options for fetching file attributes.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md)

<!--Device-userFileManager-interface FetchOptions--><!--Device-userFileManager-interface FetchOptions-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## fetchColumns

```TypeScript
fetchColumns: Array<string>
```

Options for fetching files based on the attributes in columns. If this parameter is left empty, files are fetched by URI, name, and type (the specific field names vary with the file asset or album object) by default. In addition, an error will be reported if   
[get](arkts-corefile-userfilemanager-userfilemanager-i-sys.md#getphotoassets)is called to obtain other attributes of this object. Example:

fetchColumns: ['uri', 'title']

**类型：** Array&lt;string&gt;

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.FetchOptions.fetchColumns](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md#fetchcolumns)

<!--Device-FetchOptions-fetchColumns: Array<string>--><!--Device-FetchOptions-fetchColumns: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## predicates

```TypeScript
predicates: dataSharePredicates.DataSharePredicates
```

Predicates that specify the fetch criteria.

**类型：** dataSharePredicates.DataSharePredicates

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.FetchOptions.predicates](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md#predicates)

<!--Device-FetchOptions-predicates: dataSharePredicates.DataSharePredicates--><!--Device-FetchOptions-predicates: dataSharePredicates.DataSharePredicates-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

