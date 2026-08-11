# ManualExposureQuery

Provides APIs to obtain the manual exposure range supported.

**Since:** 24

<!--Device-camera-interface ManualExposureQuery--><!--Device-camera-interface ManualExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getExposureBiasStep

```TypeScript
getExposureBiasStep(): number
```

Get exposure bias step.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualExposureQuery-getExposureBiasStep(): double--><!--Device-ManualExposureQuery-getExposureBiasStep(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getSupportedExposureDurationRange

```TypeScript
getSupportedExposureDurationRange(): Array<number>
```

Gets the supported manual exposure duration range, units: microseconds.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualExposureQuery-getSupportedExposureDurationRange(): Array<int>--><!--Device-ManualExposureQuery-getSupportedExposureDurationRange(): Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getSupportedExposureRange

```TypeScript
getSupportedExposureRange(): Array<number>
```

Obtains the supported manual exposure durations.

**Since:** 11

<!--Device-ManualExposureQuery-getSupportedExposureRange(): Array<int>--><!--Device-ManualExposureQuery-getSupportedExposureRange(): Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;number&gt; |

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
