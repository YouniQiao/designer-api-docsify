# AlbumPickerOptions

AlbumPickerOptions Object

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare class AlbumPickerOptions--><!--Device-unnamed-export declare class AlbumPickerOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { EmptyAreaClickCallback, AlbumPickerComponent, AlbumInfo, AlbumPickerOptions, AlbumPickerController } from 'kits/@kit.MediaLibraryKit';
```

## filterType

```TypeScript
public filterType?: photoAccessHelper.PhotoViewMIMETypes
```

The type of the content displayed in the album

**类型：** photoAccessHelper.PhotoViewMIMETypes

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlbumPickerOptions-public filterType?: photoAccessHelper.PhotoViewMIMETypes--><!--Device-AlbumPickerOptions-public filterType?: photoAccessHelper.PhotoViewMIMETypes-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## fontSize

```TypeScript
public fontSize?: int | string
```

The size of the font displayed in the album. When `fontSize` is an int type, must use 'fp' unit

**类型：** int \| string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlbumPickerOptions-public fontSize?: int | string--><!--Device-AlbumPickerOptions-public fontSize?: int | string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## themeColorMode

```TypeScript
public themeColorMode?: PickerColorMode
```

AlbumPickerComponent theme color

**类型：** [PickerColorMode](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlbumPickerOptions-public themeColorMode?: PickerColorMode--><!--Device-AlbumPickerOptions-public themeColorMode?: PickerColorMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

