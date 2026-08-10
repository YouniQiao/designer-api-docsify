# GalleryFormInfo（系统接口）

Defines the Gallery widget information.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface GalleryFormInfo--><!--Device-photoAccessHelper-interface GalleryFormInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## assetUris

```TypeScript
assetUris?: Array<string>
```

URIs of the images or albums bound to the widget.

This parameter cannot be empty when creating or updating a widget.

If you attempt to create or update a widget with more than 500 URIs in **assetUris**, only the first 500 URIs are registered for listening. Any URIs beyond the first 500 are not registered. 

When deleting a widget, this parameter can be omitted.

**类型：** Array&lt;string&gt;

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GalleryFormInfo-assetUris?: Array<string>--><!--Device-GalleryFormInfo-assetUris?: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## formId

```TypeScript
formId: string
```

Widget ID, which is provided when a widget is created in Gallery.

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GalleryFormInfo-formId: string--><!--Device-GalleryFormInfo-formId: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

