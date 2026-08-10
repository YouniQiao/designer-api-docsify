# VideoDurationFilter

Describes the configuration for video duration filtering.

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-class VideoDurationFilter--><!--Device-photoAccessHelper-class VideoDurationFilter-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## extraVideoDuration

```TypeScript
extraVideoDuration?: int
```

Maximum video duration in **FilterOperator.BETWEEN** mode. The default value is **-1**.

The unit is milliseconds (ms).

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoDurationFilter-extraVideoDuration?: int--><!--Device-VideoDurationFilter-extraVideoDuration?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## filterOperator

```TypeScript
filterOperator: FilterOperator
```

Filter operator.

For example, files can be filtered based on being greater than or less than a certain file size.

**类型：** [FilterOperator](arkts-medialibrary-photoaccesshelper-filteroperator-e.md)

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoDurationFilter-filterOperator: FilterOperator--><!--Device-VideoDurationFilter-filterOperator: FilterOperator-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## videoDuration

```TypeScript
videoDuration: int
```

Video duration used for filtering.

The unit is milliseconds (ms).

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoDurationFilter-videoDuration: int--><!--Device-VideoDurationFilter-videoDuration: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

