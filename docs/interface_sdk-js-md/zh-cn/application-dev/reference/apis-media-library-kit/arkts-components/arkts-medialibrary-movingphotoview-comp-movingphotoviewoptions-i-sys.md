# MovingPhotoViewOptions（系统接口）

```TypeScript
declare interface MovingPhotoViewOptions
```

定义动态照片视图选项。

**起始版本：** 12

<!--Device-unnamed-declare interface MovingPhotoViewOptions--><!--Device-unnamed-declare interface MovingPhotoViewOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute, PixelMapFormat, DynamicRangeMode, DisplayMode } from '@kit.MediaLibraryKit';
```

## dynamicRangeMode

```TypeScript
dynamicRangeMode?: DynamicRangeMode
```

MovePhotoView的范围模式。

**类型：** [DynamicRangeMode](arkts-medialibrary-movingphotoview-comp-dynamicrangemode-e-sys.md)

**起始版本：** 14

<!--Device-MovingPhotoViewOptions-dynamicRangeMode?: DynamicRangeMode--><!--Device-MovingPhotoViewOptions-dynamicRangeMode?: DynamicRangeMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## movingPhotoFormat

```TypeScript
movingPhotoFormat?: PixelMapFormat
```

动态照片视图的格式。

**类型：** [PixelMapFormat](arkts-medialibrary-movingphotoview-comp-pixelmapformat-e-sys.md)

**起始版本：** 14

<!--Device-MovingPhotoViewOptions-movingPhotoFormat?: PixelMapFormat--><!--Device-MovingPhotoViewOptions-movingPhotoFormat?: PixelMapFormat-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## playWithMask

```TypeScript
playWithMask?: boolean
```

动态图片播放时是否包含封面图片的水印。

**类型：** boolean

**起始版本：** 19

<!--Device-MovingPhotoViewOptions-playWithMask?: boolean--><!--Device-MovingPhotoViewOptions-playWithMask?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。
