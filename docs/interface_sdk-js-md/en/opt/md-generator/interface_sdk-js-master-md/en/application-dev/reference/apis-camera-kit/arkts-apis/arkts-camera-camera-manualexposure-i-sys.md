# ManualExposure (System API)

ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md#ManualExposureQuery-(System-API)) Provides APIs to obtain and set the exposure duration.

**Inheritance/Implementation:** ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md#ManualExposureQuery-(System-API))

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface ManualExposure--><!--Device-camera-interface ManualExposure-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getExposure

```TypeScript
getExposure(): number
```

Obtains the manual exposure duration in use.

**Since:** 23

**Deprecated since:** -1

<!--Device-ManualExposure-getExposure(): int--><!--Device-ManualExposure-getExposure(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function getExposure(nightPhotoSession: camera.NightPhotoSession): number | undefined {
  let exposureRange: Array<number> = nightPhotoSession.getSupportedExposureRange();
  if (exposureRange === undefined || exposureRange.length <= 0) {
    return undefined;
  }
  let exposure: number = nightPhotoSession.getExposure();
  return exposure;
}
```

## setExposure

```TypeScript
setExposure(exposure: number): void
```

Sets the manual exposure duration. Before using this API, call [getSupportedExposureRange](arkts-camera-camera-manualexposurequery-i-sys.md#getSupportedExposureRange) to obtain the supported manual exposure durations, in ms.

**Since:** 23

**Deprecated since:** -1

<!--Device-ManualExposure-setExposure(exposure: int): void--><!--Device-ManualExposure-setExposure(exposure: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [exposure](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenepostprocesssettings-tonemappingsettings-i.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
