# MovingPhotoViewAttribute

Defines the moving photo view attribute functions.@extends CommonMethod&lt;MovingPhotoViewAttribute&gt;

**Inheritance/Implementation:** MovingPhotoViewAttribute extends CommonMethod<MovingPhotoViewAttribute>

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute, PixelMapFormat, DynamicRangeMode } from 'kits/@kit.MediaLibraryKit';
```

## setPlaybackStrategy

```TypeScript
setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute
```

Sets playback strategy.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | media.PlaybackStrategy | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MovingPhotoViewAttribute](arkts-medialibrary-multimedia-movingphotoview-movingphotoviewattribute-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
