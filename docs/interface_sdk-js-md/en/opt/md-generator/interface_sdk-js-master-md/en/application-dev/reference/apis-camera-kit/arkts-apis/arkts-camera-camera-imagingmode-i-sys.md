# ImagingMode (System API)

Implements imaging mode.

**Inheritance/Implementation:** ImagingMode extends [ImagingModeQuery](arkts-camera-camera-imagingmodequery-i-sys.md#ImagingModeQuery-(System-API))

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-camera-interface ImagingMode--><!--Device-camera-interface ImagingMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getImagingMode

```TypeScript
getImagingMode(): CameraImagingMode
```

Gets current imaging mode.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImagingMode-getImagingMode(): CameraImagingMode--><!--Device-ImagingMode-getImagingMode(): CameraImagingMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setImagingMode

```TypeScript
setImagingMode(mode: CameraImagingMode): void
```

Sets imaging mode.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImagingMode-setImagingMode(mode: CameraImagingMode): void--><!--Device-ImagingMode-setImagingMode(mode: CameraImagingMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
