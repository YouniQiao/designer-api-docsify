# QuickThumbnail (System API)

Quick thumbnail object

**Since:** 19

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## release

```TypeScript
release(): Promise<void>
```

Release quick thumbnail object.

**Since:** 19

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

**Since:** 19

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## thumbnailImage

```TypeScript
thumbnailImage: image.PixelMap
```

Thumbnail image.

**Type:** image.PixelMap

**Since:** 19

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.
