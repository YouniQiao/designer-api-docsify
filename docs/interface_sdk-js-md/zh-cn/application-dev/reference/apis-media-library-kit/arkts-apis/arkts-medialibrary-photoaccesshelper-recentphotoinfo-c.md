# RecentPhotoInfo

Recent photo info

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-export class RecentPhotoInfo--><!--Device-photoAccessHelper-export class RecentPhotoInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## dateTaken

```TypeScript
dateTaken?: long
```

Time when the recent image or video was shot (in milliseconds since January 1, 1970). The unit is ms.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RecentPhotoInfo-dateTaken?: long--><!--Device-RecentPhotoInfo-dateTaken?: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## identifier

```TypeScript
identifier?: string
```

Hash value of the name of the recent image or video, which is used to help the application determine whether the image or video to be displayed is the same as the one displayed before.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RecentPhotoInfo-identifier?: string--><!--Device-RecentPhotoInfo-identifier?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

