# AutoExposure

*AutoExposure** inherits from [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md).

It provides APIs related to auto exposure.

**Inheritance/Implementation:** AutoExposure extends [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md)

**Since:** 23

<!--Device-camera-interface AutoExposure--><!--Device-camera-interface AutoExposure-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## getExposureMode

```TypeScript
getExposureMode(): ExposureMode
```

Obtains the exposure mode in use.

> **NOTE：**
> 
> This API directly returns an invalid value if you have not set the exposure mode using
> [setExposureMode](#setexposuremode).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposure-getExposureMode(): ExposureMode--><!--Device-AutoExposure-getExposureMode(): ExposureMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ExposureMode](arkts-camera-camera-exposuremode-e.md) | Exposure mode obtained. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureMode(photoSession: camera.PhotoSession): camera.ExposureMode | undefined {
  let exposureMode: camera.ExposureMode | undefined = undefined;
  try {
    exposureMode = photoSession.getExposureMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getExposureMode call failed. error code: ${err.code}`);
  }
  return exposureMode;
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureMode(captureSession: camera.CaptureSession): camera.ExposureMode | undefined {
  let exposureMode: camera.ExposureMode | undefined = undefined;
  try {
    exposureMode = captureSession.getExposureMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getExposureMode call failed. error code: ${err.code}`);
  }
  return exposureMode;
}
```

## getExposureValue

```TypeScript
getExposureValue(): double
```

Obtains the exposure value in use.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposure-getExposureValue(): double--><!--Device-AutoExposure-getExposureValue(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| double | Exposure value obtained. There is a step for EV. For example, if the step is 0.5 and this parameter is set to 1.2, the EV that takes effect is 1.0. <br>If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureValue(photoSession: camera.PhotoSession): number {
  const invalidValue: number = -1;
  let exposureValue: number = invalidValue;
  try {
    exposureValue = photoSession.getExposureValue();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getExposureValue call failed. error code: ${err.code}`);
  }
  return exposureValue;
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureValue(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let exposureValue: number = invalidValue;
  try {
    exposureValue = captureSession.getExposureValue();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getExposureValue call failed. error code: ${err.code}`);
  }
  return exposureValue;
}
```

## getMeteringPoint

```TypeScript
getMeteringPoint(): Point
```

Obtains the metering point of the camera device.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposure-getMeteringPoint(): Point--><!--Device-AutoExposure-getMeteringPoint(): Point-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Point | Metering point obtained. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getMeteringPoint(photoSession: camera.PhotoSession): camera.Point | undefined {
  let exposurePoint: camera.Point | undefined = undefined;
  try {
    exposurePoint = photoSession.getMeteringPoint();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getMeteringPoint call failed. error code: ${err.code}`);
  }
  return exposurePoint;
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getMeteringPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
  let exposurePoint: camera.Point | undefined = undefined;
  try {
    exposurePoint = captureSession.getMeteringPoint();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getMeteringPoint call failed. error code: ${err.code}`);
  }
  return exposurePoint;
}
```

## offExposureStateChange

```TypeScript
offExposureStateChange(callback?: Callback<ExposureState>): void
```

Unregisters the listener for exposure state change events. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AutoExposure-offExposureStateChange(callback?: Callback<ExposureState>): void--><!--Device-AutoExposure-offExposureStateChange(callback?: Callback<ExposureState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExposureState](arkts-camera-camera-exposurestate-e.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. If the callback object is null or an anonymous function, the subscriptions to the specified event with all the callbacks are canceled. |

## onExposureStateChange

```TypeScript
onExposureStateChange(callback: Callback<ExposureState>): void
```

Listens to exposure state change events. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AutoExposure-onExposureStateChange(callback: Callback<ExposureState>): void--><!--Device-AutoExposure-onExposureStateChange(callback: Callback<ExposureState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExposureState](arkts-camera-camera-exposurestate-e.md)&gt; | Yes | Callback used to return the exposure state. |

## setExposureBias

```TypeScript
setExposureBias(exposureBias: double): void
```

Sets an exposure compensation value (EV).

Before the setting, you are advised to use [getExposureBiasRange](arkts-camera-camera-autoexposurequery-i.md#getexposurebiasrange) to obtain the supported values.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposure-setExposureBias(exposureBias: double): void--><!--Device-AutoExposure-setExposureBias(exposureBias: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exposureBias | double | Yes | EV. The supported EV range can be obtained by calling [getExposureBiasRange](arkts-camera-camera-autoexposurequery-i.md#getexposurebiasrange). If the value passed is not within the supported range, the nearest critical point is used. <br>Exposure compensation is adjusted in steps, and the step size may vary across devices due to hardware differences. For example, if the step size is 0.5, setting a value of 1.2 would result in an actual effective exposure compensation value of 1.0. <br>If the operation fails, an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md) is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureBias(photoSession: camera.PhotoSession, biasRangeArray: Array<number>): void {
  if (biasRangeArray && biasRangeArray.length > 0) {
    let exposureBias = biasRangeArray[0];
    try {
      photoSession.setExposureBias(exposureBias);
    } catch (error) {
      // If the operation fails, error.code is returned and processed.
      let err = error as BusinessError;
      console.error(`The setExposureBias call failed. error code: ${err.code}`);
    }
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureBias(captureSession: camera.CaptureSession, biasRangeArray: Array<number>): void {
  if (biasRangeArray && biasRangeArray.length > 0) {
    let exposureBias = biasRangeArray[0];
    try {
      captureSession.setExposureBias(exposureBias);
    } catch (error) {
      // If the operation fails, error.code is returned and processed.
      let err = error as BusinessError;
      console.error(`The setExposureBias call failed. error code: ${err.code}`);
    }
  }
}
```

## setExposureMode

```TypeScript
setExposureMode(aeMode: ExposureMode): void
```

Sets an exposure mode. Before the setting, call [isExposureModeSupported](arkts-camera-camera-autoexposurequery-i.md#isexposuremodesupported) to check whether the exposure mode is supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposure-setExposureMode(aeMode: ExposureMode): void--><!--Device-AutoExposure-setExposureMode(aeMode: ExposureMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aeMode | [ExposureMode](arkts-camera-camera-exposuremode-e.md) | Yes | Exposure mode. If the input parameter is null or undefined, it is treated as 0 and exposure is locked. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed.<br>**Applicable version:** 19 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureMode(photoSession: camera.PhotoSession): void {
  try {
    photoSession.setExposureMode(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The setExposureMode call failed. error code: ${err.code}`);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setExposureMode(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The setExposureMode call failed. error code: ${err.code}`);
  }
}
```

## setMeteringPoint

```TypeScript
setMeteringPoint(point: Point): void
```

Sets the metering point, which is the center point of the metering rectangle. The metering point must be in the coordinate system (0-1), where the top-left corner is {0, 0} and the bottom-right corner is {1, 1}.

The coordinate system is based on the horizontal device direction with the device's charging port on the right. If the layout of the preview screen of an application is based on the vertical direction with the charging port on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate point after conversion is {y/h, 1-x/w}.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposure-setMeteringPoint(point: Point): void--><!--Device-AutoExposure-setMeteringPoint(point: Point): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | Point | Yes | Metering point. The value range of x and y must be within [0, 1]. If a value less than 0 is passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setMeteringPoint(photoSession: camera.PhotoSession): void {
  const point: camera.Point = {x: 1, y: 1};
  try {
    photoSession.setMeteringPoint(point);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The setMeteringPoint call failed. error code: ${err.code}`);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setMeteringPoint(captureSession: camera.CaptureSession): void {
  const point: camera.Point = {x: 1, y: 1};
  try {
    captureSession.setMeteringPoint(point);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The setMeteringPoint call failed. error code: ${err.code}`);
  }
}
```

