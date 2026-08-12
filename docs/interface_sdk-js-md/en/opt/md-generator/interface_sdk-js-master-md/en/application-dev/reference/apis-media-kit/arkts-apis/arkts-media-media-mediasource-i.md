# MediaSource

The MediaSource class defines the media data information, which is from   
[createMediaSourceWithUrl](arkts-media-media-createmediasourcewithurl-f.md#createMediaSourceWithUrl).

**Since:** 12

<!--Device-media-interface MediaSource--><!--Device-media-interface MediaSource-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## enableOfflineCache

```TypeScript
enableOfflineCache(enable: boolean): void
```

Sets whether to enable offline caching during video playback.

**Since:** 23

<!--Device-MediaSource-enableOfflineCache(enable: boolean): void--><!--Device-MediaSource-enableOfflineCache(enable: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## getID

```TypeScript
getID(): string
```

Gets the identifier of the media source.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MediaSource-getID(): string--><!--Device-MediaSource-getID(): string-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## setMediaResourceLoaderDelegate

```TypeScript
setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void
```

Sets a MediaSourceLoader object, which is used to help the player request media data.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSource-setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void--><!--Device-MediaSource-setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceLoader | [MediaSourceLoader](arkts-media-media-mediasourceloader-i.md) | Yes |

## setMimeType

```TypeScript
setMimeType(mimeType: AVMimeTypes): void
```

Sets the MIME type to help the player process extended media sources.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaSource-setMimeType(mimeType: AVMimeTypes): void--><!--Device-MediaSource-setMimeType(mimeType: AVMimeTypes): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | [AVMimeTypes](arkts-media-media-avmimetypes-e.md) | Yes |
