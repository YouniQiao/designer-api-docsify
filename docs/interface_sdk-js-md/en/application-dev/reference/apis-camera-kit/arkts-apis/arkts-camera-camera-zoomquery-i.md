# ZoomQuery

ZoomQuery provides APIs to query the zoom feature of a device camera, including the API to obtain the supported zoom ratio range.

> **NOTE：**
> 
> - This interface was first introduced in API version 12. In this version, a compatibility change was made that
> preserved the initial version information of inner elements. As a result, you might see outer element's @since
> version number being higher than that of the inner elements. However, this discrepancy does not affect the
> functionality of the interface.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface ZoomQuery--><!--Device-camera-interface ZoomQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getRAWCaptureZoomRatioRange

ArkTS-Dyn:
```TypeScript
getRAWCaptureZoomRatioRange(): Array<number>
```

ArkTS-Sta:
```TypeScript
getRAWCaptureZoomRatioRange(): Array<double>
```

Obtains the supported zoom ratio range during shooting in RAW format.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ZoomQuery-getRAWCaptureZoomRatioRange(): Array<double>--><!--Device-ZoomQuery-getRAWCaptureZoomRatioRange(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | Zoom ratio range. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal. |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config. |

## getZoomPointInfos

```TypeScript
getZoomPointInfos(): Array<ZoomPointInfo>
```

Obtains the equivalent focal length information list in the current mode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ZoomQuery-getZoomPointInfos(): Array<ZoomPointInfo>--><!--Device-ZoomQuery-getZoomPointInfos(): Array<ZoomPointInfo>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[ZoomPointInfo](arkts-camera-camera-zoompointinfo-i.md)&gt; | Equivalent focal length information list in the current mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 24 |

## Examples

```TypeScript
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomPointInfos(photoSessionForSys: camera.PhotoSessionForSys): Array<camera.ZoomPointInfo> {
  let zoomPointInfos: Array<camera.ZoomPointInfo> = [];
  try {
    zoomPointInfos = photoSessionForSys.getZoomPointInfos();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getZoomPointInfos call failed. error code: ${err.code}`);
  }
  return zoomPointInfos;
}
```

## getZoomRatioRange

ArkTS-Dyn:
```TypeScript
getZoomRatioRange(): Array<number>
```

ArkTS-Sta:
```TypeScript
getZoomRatioRange(): Array<double>
```

Obtains the supported zoom ratio range.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ZoomQuery-getZoomRatioRange(): Array<double>--><!--Device-ZoomQuery-getZoomRatioRange(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | Array containing the minimum and maximum zoom ratios. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

