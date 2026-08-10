# CreateOptions

Options for creating an image or video asset.

The title must meet the following requirements:

- It must not contain a file name extension.  
- The total length of the file name must be between 1 and 255 characters.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface CreateOptions--><!--Device-photoAccessHelper-interface CreateOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## subtype

```TypeScript
subtype?: PhotoSubtype
```

Subtype of the image or video file.

**类型：** [PhotoSubtype](arkts-medialibrary-sendablephotoaccesshelper-photosubtype-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CreateOptions-subtype?: PhotoSubtype--><!--Device-CreateOptions-subtype?: PhotoSubtype-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## title

```TypeScript
title?: string
```

Title of the image or video.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CreateOptions-title?: string--><!--Device-CreateOptions-title?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

