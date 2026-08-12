# ImagingModeQuery (System API)

Imaging mode query object.

**Since:** 26.0.0

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImagingModeQuery-isImagingModeSupported(mode: CameraImagingMode): boolean--><!--Device-ImagingModeQuery-isImagingModeSupported(mode: CameraImagingMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
