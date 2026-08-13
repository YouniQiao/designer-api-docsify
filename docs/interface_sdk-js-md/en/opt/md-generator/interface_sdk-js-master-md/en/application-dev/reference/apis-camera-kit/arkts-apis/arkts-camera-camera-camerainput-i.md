# CameraInput

**CameraInput** defines the camera input object. It provides camera device information used in [Session](arkts-camera-camera-session-i.md#Session).

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface CameraInput--><!--Device-camera-interface CameraInput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes this camera device. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-close(callback: AsyncCallback<void>): void--><!--Device-CameraInput-close(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## close

```TypeScript
close(): Promise<void>
```

Closes this camera device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-close(): Promise<void>--><!--Device-CameraInput-close(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## getPhysicalCameraOrientation

```TypeScript
getPhysicalCameraOrientation(): number
```

Obtains the physical camera orientation in the current fold state of the device.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraInput-getPhysicalCameraOrientation(): int--><!--Device-CameraInput-getPhysicalCameraOrientation(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## isPhysicalCameraOrientationVariable

```TypeScript
isPhysicalCameraOrientationVariable(): boolean
```

Checks whether the physical camera orientation is adjustable in different fold states of the device.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraInput-isPhysicalCameraOrientationVariable(): boolean--><!--Device-CameraInput-isPhysicalCameraOrientationVariable(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## offCameraOcclusionDetection

```TypeScript
offCameraOcclusionDetection(callback?: AsyncCallback<CameraOcclusionDetectionResult>): void
```

Unsubscribes from camera occlusion detection results.

**Since:** 23

**Deprecated since:** -1

<!--Device-CameraInput-offCameraOcclusionDetection(callback?: AsyncCallback<CameraOcclusionDetectionResult>): void--><!--Device-CameraInput-offCameraOcclusionDetection(callback?: AsyncCallback<CameraOcclusionDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CameraOcclusionDetectionResult](arkts-camera-camera-cameraocclusiondetectionresult-i-sys.md)&gt; | No |

## offError

```TypeScript
offError(camera: CameraDevice, callback?: ErrorCallback): void
```

Unsubscribes from error events.

**Since:** 23

**Deprecated since:** -1

<!--Device-CameraInput-offError(camera: CameraDevice, callback?: ErrorCallback): void--><!--Device-CameraInput-offError(camera: CameraDevice, callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## off_error

```TypeScript
off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void
```

Unsubscribes from CameraInput error events.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void--><!--Device-CameraInput-off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## onCameraOcclusionDetection

```TypeScript
onCameraOcclusionDetection(callback: AsyncCallback<CameraOcclusionDetectionResult>): void
```

Subscribes to camera occlusion detection results.

**Since:** 23

**Deprecated since:** -1

<!--Device-CameraInput-onCameraOcclusionDetection(callback: AsyncCallback<CameraOcclusionDetectionResult>): void--><!--Device-CameraInput-onCameraOcclusionDetection(callback: AsyncCallback<CameraOcclusionDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CameraOcclusionDetectionResult](arkts-camera-camera-cameraocclusiondetectionresult-i-sys.md)&gt; | Yes |

## onError

```TypeScript
onError(camera: CameraDevice, callback: ErrorCallback): void
```

Subscribes to error events.

**Since:** 23

**Deprecated since:** -1

<!--Device-CameraInput-onError(camera: CameraDevice, callback: ErrorCallback): void--><!--Device-CameraInput-onError(camera: CameraDevice, callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## on_error

```TypeScript
on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void
```

Subscribes to CameraInput error events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void--><!--Device-CameraInput-on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## open

```TypeScript
open(callback: AsyncCallback<void>): void
```

Opens this camera device. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-open(callback: AsyncCallback<void>): void--><!--Device-CameraInput-open(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [7400107](../errorcode-camera.md#7400107-camera-conflict) |
| [7400108](../errorcode-camera.md#7400108-camera-disabled-due-to-security-reasons) |

## open

```TypeScript
open(): Promise<void>
```

Opens this camera device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-open(): Promise<void>--><!--Device-CameraInput-open(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [7400107](../errorcode-camera.md#7400107-camera-conflict) |
| [7400108](../errorcode-camera.md#7400108-camera-disabled-due-to-security-reasons) |

## open

```TypeScript
open(isSecureEnabled: boolean): Promise<bigint>
```

Opens this camera device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-open(isSecureEnabled: boolean): Promise<bigint>--><!--Device-CameraInput-open(isSecureEnabled: boolean): Promise<bigint>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isSecureEnabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;bigint & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [7400107](../errorcode-camera.md#7400107-camera-conflict) |
| [7400108](../errorcode-camera.md#7400108-camera-disabled-due-to-security-reasons) |

## open

```TypeScript
open(type: CameraConcurrentType): Promise<void>
```

Opens the camera with the specified concurrency type. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-open(type: CameraConcurrentType): Promise<void>--><!--Device-CameraInput-open(type: CameraConcurrentType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [CameraConcurrentType](arkts-camera-camera-cameraconcurrenttype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [7400107](../errorcode-camera.md#7400107-camera-conflict) |
| [7400108](../errorcode-camera.md#7400108-camera-disabled-due-to-security-reasons) |

## usePhysicalCameraOrientation

```TypeScript
usePhysicalCameraOrientation(isUsed: boolean): void
```

Enables or disables the use of the physical camera orientation.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraInput-usePhysicalCameraOrientation(isUsed: boolean): void--><!--Device-CameraInput-usePhysicalCameraOrientation(isUsed: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isUsed](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-runninglock-runninglock-c.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
