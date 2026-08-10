# RecentPhotoOptions

RecentPhotoOptions Object

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-export class RecentPhotoOptions--><!--Device-photoAccessHelper-export class RecentPhotoOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## MIMEType

```TypeScript
MIMEType?: photoAccessHelper.PhotoViewMIMETypes
```

Types of the file displayed. The default value is **PhotoViewMIMETypes.IMAGE_VIDEO_TYPE**.

**类型：** photoAccessHelper.PhotoViewMIMETypes

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RecentPhotoOptions-MIMEType?: photoAccessHelper.PhotoViewMIMETypes--><!--Device-RecentPhotoOptions-MIMEType?: photoAccessHelper.PhotoViewMIMETypes-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## period

```TypeScript
period?: int
```

Time range for displaying the recent images or videos, measured in seconds. After setting, the system shows images or videos taken within the specified time from the current moment. The longest duration you can set is 1 day (86400s).

If the value is less than or equal to 0, greater than 86400, or not set, the system uses the longest duration (1 day) by default. If there are no images or videos within the set time range, the component does not show anything.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RecentPhotoOptions-period?: int--><!--Device-RecentPhotoOptions-period?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoSource

```TypeScript
photoSource?: PhotoSource
```

Source of the recent image or video, for example, image or video taken by the camera or screenshot. By default, the source is not restricted.

**类型：** [PhotoSource](arkts-medialibrary-photoaccesshelper-photosource-e.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RecentPhotoOptions-photoSource?: PhotoSource--><!--Device-RecentPhotoOptions-photoSource?: PhotoSource-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

