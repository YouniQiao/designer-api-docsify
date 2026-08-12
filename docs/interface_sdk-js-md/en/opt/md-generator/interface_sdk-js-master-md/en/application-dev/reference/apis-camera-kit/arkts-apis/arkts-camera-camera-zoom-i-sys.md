# Zoom

**Zoom** inherits from [ZoomQuery](arkts-camera-camera-zoomquery-i.md#ZoomQuery).

It provides APIs related to zoom operations.

**Inheritance/Implementation:** Zoom extends [ZoomQuery](arkts-camera-camera-zoomquery-i.md#ZoomQuery)

**Since:** 11

<!--Device-camera-interface Zoom extends ZoomQuery--><!--Device-camera-interface Zoom extends ZoomQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getZoomCenterPoint

```TypeScript
getZoomCenterPoint(): Point
```

Gets zoom center point.

**Since:** 20

<!--Device-Zoom-getZoomCenterPoint(): Point--><!--Device-Zoom-getZoomCenterPoint(): Point-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Point](arkts-camera-camera-point-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## prepareZoom

```TypeScript
prepareZoom(): void
```

Instructs the bottom layer to prepare for zooming, for example, powering on the sensor.

**Since:** 11

<!--Device-Zoom-prepareZoom(): void--><!--Device-Zoom-prepareZoom(): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function prepareZoom(sessionExtendsZoom: camera.Zoom): void {
  try {
    sessionExtendsZoom.prepareZoom();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The prepareZoom call failed. error code: ${err.code}`);
  }
}
```

## setZoomCenterPoint

```TypeScript
setZoomCenterPoint(point: Point): void
```

Sets zoom center point.

**Since:** 20

<!--Device-Zoom-setZoomCenterPoint(point: Point): void--><!--Device-Zoom-setZoomCenterPoint(point: Point): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-camera-camera-point-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## unprepareZoom

```TypeScript
unprepareZoom(): void
```

Instructs the bottom layer to unprepare for zooming.

**Since:** 11

<!--Device-Zoom-unprepareZoom(): void--><!--Device-Zoom-unprepareZoom(): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function unprepareZoom(sessionExtendsZoom: camera.Zoom): void {
  try {
    sessionExtendsZoom.unprepareZoom();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The unprepareZoom call failed. error code: ${err.code}`);
  }
}
```
