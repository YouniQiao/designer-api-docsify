# MovingPhotoViewOptions

Defines the moving photo view options.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-unnamed-declare interface MovingPhotoViewOptions--><!--Device-unnamed-declare interface MovingPhotoViewOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { PixelMapFormat, MovingPhotoViewAttribute, MovingPhotoView, MovingPhotoViewController, DynamicRangeMode } from 'kits/@kit.MediaLibraryKit';
```

## dynamicRangeMode

```TypeScript
dynamicRangeMode?: DynamicRangeMode
```

range mode of MovingPhotoView.

**类型：** [DynamicRangeMode](../../apis-arkui/arkts-apis/arkts-arkui-image-dynamicrangemode-e.md)

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-MovingPhotoViewOptions-dynamicRangeMode?: DynamicRangeMode--><!--Device-MovingPhotoViewOptions-dynamicRangeMode?: DynamicRangeMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## movingPhotoFormat

```TypeScript
movingPhotoFormat?: PixelMapFormat
```

format of MovingPhotoView.

**类型：** [PixelMapFormat](arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e-sys.md)

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-MovingPhotoViewOptions-movingPhotoFormat?: PixelMapFormat--><!--Device-MovingPhotoViewOptions-movingPhotoFormat?: PixelMapFormat-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## playWithMask

```TypeScript
playWithMask?: boolean
```

the watermask of the cover photo whether to contain during movingphoto playback

**类型：** boolean

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为19。

<!--Device-MovingPhotoViewOptions-playWithMask?: boolean--><!--Device-MovingPhotoViewOptions-playWithMask?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

