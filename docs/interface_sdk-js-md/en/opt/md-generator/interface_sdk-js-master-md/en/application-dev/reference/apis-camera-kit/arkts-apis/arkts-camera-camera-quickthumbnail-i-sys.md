# QuickThumbnail (System API)

Quick thumbnail object

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface QuickThumbnail--><!--Device-camera-interface QuickThumbnail-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## release

```TypeScript
release(): Promise<void>
```

Release quick thumbnail object.

**Since:** 23

**Deprecated since:** -1

<!--Device-QuickThumbnail-release(): Promise<void>--><!--Device-QuickThumbnail-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## captureId

```TypeScript
readonly captureId: number
```

capture id.

**Type:** number

**Since:** 23

**Deprecated since:** -1

<!--Device-QuickThumbnail-readonly captureId: int--><!--Device-QuickThumbnail-readonly captureId: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## thumbnailImage

```TypeScript
thumbnailImage: image.PixelMap
```

Thumbnail image.

**Type:** image.PixelMap

**Since:** 23

**Deprecated since:** -1

<!--Device-QuickThumbnail-thumbnailImage: image.PixelMap--><!--Device-QuickThumbnail-thumbnailImage: image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.
