# RecentPhotoOptions

RecentPhotoOptions Object

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare class RecentPhotoOptions--><!--Device-unnamed-export declare class RecentPhotoOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { RecentPhotoComponent, RecentPhotoCheckResultCallback, RecentPhotoCheckInfoCallback, PhotoSource, RecentPhotoClickCallback, RecentPhotoOptions, RecentPhotoInfo } from 'kits/@kit.MediaLibraryKit';
```

## MIMEType

```TypeScript
public MIMEType?: photoAccessHelper.PhotoViewMIMETypes
```

The Type of the file in the recent photo window.

**类型：** photoAccessHelper.PhotoViewMIMETypes

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecentPhotoOptions-public MIMEType?: photoAccessHelper.PhotoViewMIMETypes--><!--Device-RecentPhotoOptions-public MIMEType?: photoAccessHelper.PhotoViewMIMETypes-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## colorMode

```TypeScript
public colorMode?: PickerColorMode
```

color mode of recentPhotoComponent placeholder

**类型：** [PickerColorMode](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecentPhotoOptions-public colorMode?: PickerColorMode--><!--Device-RecentPhotoOptions-public colorMode?: PickerColorMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isAutoRefreshSupported

```TypeScript
public isAutoRefreshSupported?: boolean
```

isSupportAutoRefresh

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecentPhotoOptions-public isAutoRefreshSupported?: boolean--><!--Device-RecentPhotoOptions-public isAutoRefreshSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## period

```TypeScript
public period?: int
```

Support set period time

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecentPhotoOptions-public period?: int--><!--Device-RecentPhotoOptions-public period?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoSource

```TypeScript
public photoSource?: PhotoSource
```

PhotoSource

**类型：** [PhotoSource](arkts-medialibrary-photoaccesshelper-photosource-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecentPhotoOptions-public photoSource?: PhotoSource--><!--Device-RecentPhotoOptions-public photoSource?: PhotoSource-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

