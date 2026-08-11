# ZoomQuery

ZoomQuery provides APIs to query the zoom feature of a device camera, including the API to obtain the supported zoom ratio range.

> **NOTE：**
> 
> - This interface was first introduced in API version 12. In this version, a compatibility change was made that
> preserved the initial version information of inner elements. As a result, you might see outer element's @since
> version number being higher than that of the inner elements. However, this discrepancy does not affect the
> functionality of the interface.

**Since:** 12

<!--Device-camera-interface ZoomQuery--><!--Device-camera-interface ZoomQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getRAWCaptureZoomRatioRange

```TypeScript
getRAWCaptureZoomRatioRange(): Array<number>
```

Obtains the supported zoom ratio range during shooting in RAW format.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ZoomQuery-getRAWCaptureZoomRatioRange(): Array<double>--><!--Device-ZoomQuery-getRAWCaptureZoomRatioRange(): Array<double>-End-->

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

## getZoomPointInfos

```TypeScript
getZoomPointInfos(): Array<ZoomPointInfo>
```

Obtains the equivalent focal length information list in the current mode.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ZoomQuery-getZoomPointInfos(): Array<ZoomPointInfo>--><!--Device-ZoomQuery-getZoomPointInfos(): Array<ZoomPointInfo>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;ZoomPointInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getZoomRatioRange

```TypeScript
getZoomRatioRange(): Array<number>
```

Obtains the supported zoom ratio range.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ZoomQuery-getZoomRatioRange(): Array<double>--><!--Device-ZoomQuery-getZoomRatioRange(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
