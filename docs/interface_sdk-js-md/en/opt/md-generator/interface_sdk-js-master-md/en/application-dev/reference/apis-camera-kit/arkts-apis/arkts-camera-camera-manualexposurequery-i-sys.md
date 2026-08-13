# ManualExposureQuery (System API)

Provides APIs to obtain the manual exposure range supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface ManualExposureQuery--><!--Device-camera-interface ManualExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getSupportedExposureRange

```TypeScript
getSupportedExposureRange(): Array<number>
```

Obtains the supported manual exposure durations.

**Since:** 23

**Deprecated since:** -1

<!--Device-ManualExposureQuery-getSupportedExposureRange(): Array<int>--><!--Device-ManualExposureQuery-getSupportedExposureRange(): Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function getSupportedExposureRange(nightPhotoSession: camera.NightPhotoSession): Array<number> {
  let exposureRange: Array<number> = nightPhotoSession.getSupportedExposureRange();
  return exposureRange;
}
```
