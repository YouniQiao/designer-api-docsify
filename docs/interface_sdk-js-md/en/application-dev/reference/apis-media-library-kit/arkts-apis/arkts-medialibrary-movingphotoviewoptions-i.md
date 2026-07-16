# MovingPhotoViewOptions

Defines the moving photo view options.

**Since:** 12

<!--Device-unnamed-declare interface MovingPhotoViewOptions--><!--Device-unnamed-declare interface MovingPhotoViewOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { PixelMapFormat, MovingPhotoViewAttribute, MovingPhotoView, MovingPhotoViewController, DynamicRangeMode } from '@kit.MediaLibraryKit';
```

## controller

```TypeScript
controller?: MovingPhotoViewController
```

controller of MovingPhotoView.

**Type:** MovingPhotoViewController

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MovingPhotoViewOptions-controller?: MovingPhotoViewController--><!--Device-MovingPhotoViewOptions-controller?: MovingPhotoViewController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## imageAIOptions

```TypeScript
imageAIOptions?: ImageAIOptions
```

image ai options of MovingPhotoView.

**Type:** ImageAIOptions

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MovingPhotoViewOptions-imageAIOptions?: ImageAIOptions--><!--Device-MovingPhotoViewOptions-imageAIOptions?: ImageAIOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## movingPhoto

```TypeScript
movingPhoto: photoAccessHelper.MovingPhoto
```

moving photo data.

**Type:** photoAccessHelper.MovingPhoto

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MovingPhotoViewOptions-movingPhoto: photoAccessHelper.MovingPhoto--><!--Device-MovingPhotoViewOptions-movingPhoto: photoAccessHelper.MovingPhoto-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

