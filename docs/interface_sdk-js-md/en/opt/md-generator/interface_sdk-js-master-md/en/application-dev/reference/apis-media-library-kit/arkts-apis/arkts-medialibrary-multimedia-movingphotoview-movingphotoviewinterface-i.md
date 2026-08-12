# MovingPhotoViewInterface

Defines the moving photo view interface.

**Since:** 12

<!--Device-unnamed-interface MovingPhotoViewInterface--><!--Device-unnamed-interface MovingPhotoViewInterface-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { PixelMapFormat, MovingPhotoViewAttribute, MovingPhotoView, MovingPhotoViewController, DynamicRangeMode } from '@kit.MediaLibraryKit';
```

## [[Call]]

```TypeScript
(options: MovingPhotoViewOptions): MovingPhotoViewAttribute
```

Set the options.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MovingPhotoViewInterface-(options: MovingPhotoViewOptions): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewInterface-(options: MovingPhotoViewOptions): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MovingPhotoViewOptions](arkts-medialibrary-multimedia-movingphotoview-movingphotoviewoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MovingPhotoViewAttribute](arkts-medialibrary-multimedia-movingphotoview-movingphotoviewattribute-c.md) |
