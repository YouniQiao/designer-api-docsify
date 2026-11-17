# MovingPhotoViewOptions

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

## controller

```TypeScript
controller?: MovingPhotoViewController
```

MovePhotoView的控制器。

**类型：** [MovingPhotoViewController](arkts-medialibrary-movingphotoview-comp-movingphotoviewcontroller-c.md)

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewOptions-controller?: MovingPhotoViewController--><!--Device-MovingPhotoViewOptions-controller?: MovingPhotoViewController-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## imageAIOptions

```TypeScript
imageAIOptions?: ImageAIOptions
```

MovePhotoView的图像ai选项。

**类型：** [ImageAIOptions](../../apis-arkui/arkts-apis/arkts-arkui-imageaioptions-i.md)

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewOptions-imageAIOptions?: ImageAIOptions--><!--Device-MovingPhotoViewOptions-imageAIOptions?: ImageAIOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## movingPhoto

```TypeScript
movingPhoto: photoAccessHelper.MovingPhoto
```

动态照片数据。

**类型：** [photoAccessHelper.MovingPhoto](../arkts-apis/arkts-medialibrary-photoaccesshelper-movingphoto-i.md)

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewOptions-movingPhoto: photoAccessHelper.MovingPhoto--><!--Device-MovingPhotoViewOptions-movingPhoto: photoAccessHelper.MovingPhoto-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core
