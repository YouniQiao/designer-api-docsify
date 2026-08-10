# CreationSetting

Represents the configuration for saving images or videos to the media library, including the file name, file type, and other related parameters.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-export interface CreationSetting--><!--Device-photoAccessHelper-export interface CreationSetting-End-->

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CreationSetting-fileNameExtension: string--><!--Device-CreationSetting-fileNameExtension: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoType

```TypeScript
photoType: PhotoType
```

[PhotoType](arkts-medialibrary-photoaccesshelper-phototype-e.md) of the created media file, which can be **IMAGE** or **VIDEO**.

**类型：** [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CreationSetting-photoType: PhotoType--><!--Device-CreationSetting-photoType: PhotoType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## title

```TypeScript
title?: string
```

Title of the image or video.

If this parameter is not passed, the system generates a value. The parameter specifications are as follows:

- It must not contain a file name extension.  
- It must not contain any invalid characters, which are:\ / : * ? " ' ` &lt; &gt; | { } [ ]  
- The file name consists of the title and file name extension. The file name string length ranges from 1 to 255.   
Therefore, the title length cannot be too long.

**类型：** string

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CreationSetting-title?: string--><!--Device-CreationSetting-title?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

