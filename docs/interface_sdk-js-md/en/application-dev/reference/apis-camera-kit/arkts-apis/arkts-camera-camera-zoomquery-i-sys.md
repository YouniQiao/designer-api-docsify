# ZoomQuery

ZoomQuery provides APIs to query the zoom feature of a device camera, including the API to obtain the supported zoom ratio range. > **NOTE：**> > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface.

**Since:** 23

<!--Device-camera-interface ZoomQuery--><!--Device-camera-interface ZoomQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## getZoomPointInfos

```TypeScript
getZoomPointInfos(): Array<ZoomPointInfo>
```

Obtains the equivalent focal length information list in the current mode.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ZoomQuery-getZoomPointInfos(): Array<ZoomPointInfo>--><!--Device-ZoomQuery-getZoomPointInfos(): Array<ZoomPointInfo>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[ZoomPointInfo](arkts-camera-camera-zoompointinfo-i-sys.md)&gt; | Equivalent focal length information list in the current mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 24 |

**Examples**

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

## isZoomCenterPointSupported

```TypeScript
isZoomCenterPointSupported(): boolean
```

Checks whether zoom center point is supported.

**Since:** 23

<!--Device-ZoomQuery-isZoomCenterPointSupported(): boolean--><!--Device-ZoomQuery-isZoomCenterPointSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Is the zoom center point supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

