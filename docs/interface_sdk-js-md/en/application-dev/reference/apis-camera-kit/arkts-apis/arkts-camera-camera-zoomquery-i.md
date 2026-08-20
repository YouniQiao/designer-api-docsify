# ZoomQuery

ZoomQuery provides APIs to query the zoom feature of a device camera, including the API to obtain the supported zoom ratio range.

> **NOTE：**
> 
> - This interface was first introduced in API version 12. In this version, a compatibility change was made that &gt; preserved the initial version information of inner elements. As a result, you might see outer element's

**Since:** 23

<!--Device-camera-interface ZoomQuery--><!--Device-camera-interface ZoomQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## getRAWCaptureZoomRatioRange

```TypeScript
getRAWCaptureZoomRatioRange(): Array<double>
```

Obtains the supported zoom ratio range during shooting in RAW format.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ZoomQuery-getRAWCaptureZoomRatioRange(): Array<double>--><!--Device-ZoomQuery-getRAWCaptureZoomRatioRange(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;double&gt; | Zoom ratio range. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

## getZoomRatioRange

```TypeScript
getZoomRatioRange(): Array<double>
```

Obtains the supported zoom ratio range.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ZoomQuery-getZoomRatioRange(): Array<double>--><!--Device-ZoomQuery-getZoomRatioRange(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;double&gt; | Array containing the minimum and maximum zoom ratios. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

