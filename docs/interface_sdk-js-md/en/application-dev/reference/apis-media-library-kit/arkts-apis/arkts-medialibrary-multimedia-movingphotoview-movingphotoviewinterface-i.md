# MovingPhotoViewInterface

Defines the moving photo view interface.

@interface MovingPhotoViewInterface

**Since:** 12

<!--Device-unnamed-interface MovingPhotoViewInterface--><!--Device-unnamed-interface MovingPhotoViewInterface-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute, PixelMapFormat, DynamicRangeMode } from '@kit.MediaLibraryKit';
```

## constructor

```TypeScript
(options: MovingPhotoViewOptions): MovingPhotoViewAttribute
```

Set the options.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MovingPhotoViewInterface-(options: MovingPhotoViewOptions): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewInterface-(options: MovingPhotoViewOptions): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [MovingPhotoViewOptions](arkts-medialibrary-multimedia-movingphotoview-movingphotoviewoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-medialibrary-multimedia-movingphotoview-movingphotoviewattribute-c.md) |  |

