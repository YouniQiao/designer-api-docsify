# ManualExposureQuery (System API)

Provides APIs to obtain the manual exposure range supported.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface ManualExposureQuery--><!--Device-camera-interface ManualExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## getSupportedExposureRange

```TypeScript
getSupportedExposureRange(): Array<int>
```

Obtains the supported manual exposure durations.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ManualExposureQuery-getSupportedExposureRange(): Array<int>--><!--Device-ManualExposureQuery-getSupportedExposureRange(): Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | Array of manual exposure durations supported, in ms. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 and later |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## Examples

```TypeScript
function getSupportedExposureRange(nightPhotoSession: camera.NightPhotoSession): Array<number> {
  let exposureRange: Array<number> = nightPhotoSession.getSupportedExposureRange();
  return exposureRange;
}
```

