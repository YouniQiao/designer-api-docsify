# ContextRecoveryInfo

Describes the information about the context of exiting the PhotoPicker. It can be used during the subsequent launch of the PhotoPicker to restore the state from the previous exit.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-export class ContextRecoveryInfo--><!--Device-photoAccessHelper-export class ContextRecoveryInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## albumUri

```TypeScript
albumUri: string
```

URI of the album in the media library when the user selects an image and exits.

- If the user selects from all images, **albumUri** is a fixed **"allPhotos"** string.  
- If the user exits after selecting from search results, text recommendations, or avatar recommendations, the   
next restoration is not supported, and the returned **albumUri** is an empty string.

The default value is an empty string.

**类型：** string

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-albumUri: string--><!--Device-ContextRecoveryInfo-albumUri: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## displayName

```TypeScript
displayName: string
```

File name of the top-left image in the grid interface when the user last selected an image. The default value is an empty string.

**类型：** string

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-displayName: string--><!--Device-ContextRecoveryInfo-displayName: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## fileSize

```TypeScript
fileSize?: int
```

File size of the top-left image in the grid interface when the user last selected an image. The default value is   
**0**.Unit: Byte, The value must be an integer greater than or equal to 0.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-fileSize?: int--><!--Device-ContextRecoveryInfo-fileSize?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## gridLevel

```TypeScript
gridLevel?: GridLevel
```

Level of the grid when the user exits last time.

**类型：** [GridLevel](arkts-medialibrary-photoaccesshelper-gridlevel-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-gridLevel?: GridLevel--><!--Device-ContextRecoveryInfo-gridLevel?: GridLevel-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## recommendationType

```TypeScript
recommendationType: int
```

Enumerated value of the recommended content set by the user during the last selection. For details, see   
[RecommendationType](arkts-medialibrary-photoaccesshelper-recommendationtype-e.md).

If no recommendation was set during the last selection, the default value is **0**.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-recommendationType: int--><!--Device-ContextRecoveryInfo-recommendationType: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## selectedRecommendationType

```TypeScript
selectedRecommendationType: int
```

Enumerated value of the recommended content selected by the user during the last selection. For details, see   
[RecommendationType](arkts-medialibrary-photoaccesshelper-recommendationtype-e.md).

If no recommendation was selected during the last selection or **All** was selected, the default value is **0**.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-selectedRecommendationType: int--><!--Device-ContextRecoveryInfo-selectedRecommendationType: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## sortRule

```TypeScript
sortRule?: string
```

Sorting rule of the grid interface when the user last selected an image. The default value is an empty string.

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-sortRule?: string--><!--Device-ContextRecoveryInfo-sortRule?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## time

```TypeScript
time: long
```

Time of the top-left image in the grid interface when the user last selected an image.

- For albums sorted by capture time, the capture time is returned.  
- For albums sorted by save time, the save time is returned. The default value is **0**.

Unit: ms, The value must be greater than or equal to 0.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-time: long--><!--Device-ContextRecoveryInfo-time: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## version

```TypeScript
version: int
```

Version number of the state data, used to verify the compatibility of the state information data with the state recovery capability.

The version number must be greater than or equal to 1.0.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-ContextRecoveryInfo-version: int--><!--Device-ContextRecoveryInfo-version: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

