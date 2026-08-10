# PhotoCreationConfig

Represents the configuration for saving a media asset (image or video) to the media library, including the file name.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface PhotoCreationConfig--><!--Device-photoAccessHelper-interface PhotoCreationConfig-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## fileNameExtension

```TypeScript
fileNameExtension: string
```

File name extension, for example, **'jpg'**.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoCreationConfig-fileNameExtension: string--><!--Device-PhotoCreationConfig-fileNameExtension: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoType

```TypeScript
photoType: PhotoType
```

Type of the file to create, which can be **IMAGE** or **VIDEO**. See   
[PhotoType](arkts-medialibrary-photoaccesshelper-phototype-e.md).

**类型：** [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoCreationConfig-photoType: PhotoType--><!--Device-PhotoCreationConfig-photoType: PhotoType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## subtype

```TypeScript
subtype?: PhotoSubtype
```

Image or video file subtype. The default value is **DEFAULT**. See   
[PhotoSubtype](arkts-medialibrary-photoaccesshelper-photosubtype-e.md).

**类型：** [PhotoSubtype](arkts-medialibrary-sendablephotoaccesshelper-photosubtype-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoCreationConfig-subtype?: PhotoSubtype--><!--Device-PhotoCreationConfig-subtype?: PhotoSubtype-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## title

```TypeScript
title?: string
```

Title of the image or video. If this parameter is not passed, the system generates a title. The title must meet the following requirements:

- It must not contain a file name extension.  
- The total length of the file name, which is in the format of title+file name extension, must be between 1 and 2  
55 characters.  
- It must not contain any invalid characters, which are:\ / : * ? " ' ` &lt; &gt; | { } [ ]

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoCreationConfig-title?: string--><!--Device-PhotoCreationConfig-title?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

