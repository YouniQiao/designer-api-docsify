# ImagingModeQuery (System API)

Imaging mode query object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-camera-interface ImagingModeQuery--><!--Device-camera-interface ImagingModeQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## isImagingModeSupported

```TypeScript
isImagingModeSupported(mode: CameraImagingMode): boolean
```

Checks whether a camera imaging mode is supported.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImagingModeQuery-isImagingModeSupported(mode: CameraImagingMode): boolean--><!--Device-ImagingModeQuery-isImagingModeSupported(mode: CameraImagingMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) | Yes | Imaging mode. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Is the imaging mode supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

