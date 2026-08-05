# CameraInput

**CameraInput** defines the camera input object. It provides camera device information used in [Session]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface CameraInput--><!--Device-camera-interface CameraInput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes this camera device. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-close(callback: AsyncCallback<void>): void--><!--Device-CameraInput-close(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the camera device is closed successfully, **err** is **undefined**. Otherwise, **err** is an error object with an error code defined in [CameraErrorCode]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## close

```TypeScript
close(): Promise<void>
```

Closes this camera device. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-close(): Promise<void>--><!--Device-CameraInput-close(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getPhysicalCameraOrientation

ArkTS-Dyn:
```TypeScript
getPhysicalCameraOrientation(): number
```

ArkTS-Sta:
```TypeScript
getPhysicalCameraOrientation(): int
```

Obtains the physical camera orientation in the current fold state of the device.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CameraInput-getPhysicalCameraOrientation(): int--><!--Device-CameraInput-getPhysicalCameraOrientation(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Physical camera orientation. |

## isPhysicalCameraOrientationVariable

```TypeScript
isPhysicalCameraOrientationVariable(): boolean
```

Checks whether the physical camera orientation is adjustable in different fold states of the device.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CameraInput-isPhysicalCameraOrientationVariable(): boolean--><!--Device-CameraInput-isPhysicalCameraOrientationVariable(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Checks whether the physical camera orientation is adjustable in different fold states of the |

## off('error')

```TypeScript
off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void
```

Unsubscribes from CameraInput error events.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void--><!--Device-CameraInput-off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a CameraInput instance is created. This event is triggered and the result is returned when an error occurs on the camera device. For example, if the camera device is unavailable or a conflict occurs, the error information is returned. |
| camera | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Camera device. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to return the result. If this parameter is specified, only the corresponding callback will be unregistered (the callback object cannot be an anonymous function); otherwise,all registered callbacks will be unregistered. |

## off('cameraOcclusionDetection')

```TypeScript
off(type: 'cameraOcclusionDetection', callback?: AsyncCallback<CameraOcclusionDetectionResult>): void
```

Unsubscribes from **CameraInput** occlusion events. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraInput-off(type: 'cameraOcclusionDetection', callback?: AsyncCallback<CameraOcclusionDetectionResult>): void--><!--Device-CameraInput-off(type: 'cameraOcclusionDetection', callback?: AsyncCallback<CameraOcclusionDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cameraOcclusionDetection' | Yes | Event type. The value is fixed at **'cameraOcclusionDetection'**.The event can be listened for when a **CameraInput** instance is created. It is triggered when the occlusion status of the camera lens changes, and the occlusion status is returned. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CameraOcclusionDetectionResult&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 - 22 |

## offCameraOcclusionDetection

```TypeScript
offCameraOcclusionDetection(callback?: AsyncCallback<CameraOcclusionDetectionResult>): void
```

Unsubscribes from camera occlusion detection results.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraInput-offCameraOcclusionDetection(callback?: AsyncCallback<CameraOcclusionDetectionResult>): void--><!--Device-CameraInput-offCameraOcclusionDetection(callback?: AsyncCallback<CameraOcclusionDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CameraOcclusionDetectionResult&gt; | No | Callback used to get detection results. |

## offError

```TypeScript
offError(camera: CameraDevice, callback?: ErrorCallback): void
```

Unsubscribes from error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraInput-offError(camera: CameraDevice, callback?: ErrorCallback): void--><!--Device-CameraInput-offError(camera: CameraDevice, callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Camera device. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to get the camera input errors. |

## on('error')

```TypeScript
on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void
```

Subscribes to CameraInput error events. This API uses an asynchronous callback to return the result. > **NOTE** > > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void--><!--Device-CameraInput-on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a CameraInput instance is created. This event is triggered and the result is returned when an error occurs on the camera device. For example, if the camera device is unavailable or a conflict occurs, the error information is returned. |
| camera | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Camera device. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return an error code defined in [CameraErrorCode]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

## on('cameraOcclusionDetection')

```TypeScript
on(type: 'cameraOcclusionDetection', callback: AsyncCallback<CameraOcclusionDetectionResult>): void
```

Subscribes to **CameraInput** occlusion events. This API uses an asynchronous callback to return the result. > **NOTE** > > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraInput-on(type: 'cameraOcclusionDetection', callback: AsyncCallback<CameraOcclusionDetectionResult>): void--><!--Device-CameraInput-on(type: 'cameraOcclusionDetection', callback: AsyncCallback<CameraOcclusionDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cameraOcclusionDetection' | Yes | Event type. The value is fixed at **'cameraOcclusionDetection'**.The event can be listened for when a **CameraInput** instance is created. It is triggered when the occlusion status of the camera lens changes, and the occlusion status is returned. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CameraOcclusionDetectionResult&gt; | Yes | Callback used to return the occlusion status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 - 22 |

## onCameraOcclusionDetection

```TypeScript
onCameraOcclusionDetection(callback: AsyncCallback<CameraOcclusionDetectionResult>): void
```

Subscribes to camera occlusion detection results.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraInput-onCameraOcclusionDetection(callback: AsyncCallback<CameraOcclusionDetectionResult>): void--><!--Device-CameraInput-onCameraOcclusionDetection(callback: AsyncCallback<CameraOcclusionDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CameraOcclusionDetectionResult&gt; | Yes | Callback used to get detection results. |

## onError

```TypeScript
onError(camera: CameraDevice, callback: ErrorCallback): void
```

Subscribes to error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraInput-onError(camera: CameraDevice, callback: ErrorCallback): void--><!--Device-CameraInput-onError(camera: CameraDevice, callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Camera device. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to get the camera input errors. |

## open

```TypeScript
open(callback: AsyncCallback<void>): void
```

Opens this camera device. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-open(callback: AsyncCallback<void>): void--><!--Device-CameraInput-open(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the camera device is opened successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400107](../errorcode-camera.md#7400107-camera-conflict) | Can not use camera cause of conflict. |
| [7400108](../errorcode-camera.md#7400108-camera-disabled-due-to-security-reasons) | Camera disabled cause of security reason. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## open

```TypeScript
open(): Promise<void>
```

Opens this camera device. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-open(): Promise<void>--><!--Device-CameraInput-open(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed. |
| [7400107](../errorcode-camera.md#7400107-camera-conflict) | Can not use camera cause of conflict. |
| [7400108](../errorcode-camera.md#7400108-camera-disabled-due-to-security-reasons) | Camera disabled cause of security reason. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## open

```TypeScript
open(isSecureEnabled: boolean): Promise<bigint>
```

Opens this camera device. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-open(isSecureEnabled: boolean): Promise<bigint>--><!--Device-CameraInput-open(isSecureEnabled: boolean): Promise<bigint>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSecureEnabled | boolean | Yes | Whether to open the camera device in secure mode. **true** to open in secure mode, **false** otherwise. If the operation fails, an error code defined in [CameraErrorCode]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;bigint&gt; | Promise used to return the handle to the camera device in secure mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400107](../errorcode-camera.md#7400107-camera-conflict) | Can not use camera cause of conflict. |
| [7400108](../errorcode-camera.md#7400108-camera-disabled-due-to-security-reasons) | Camera disabled cause of security reason. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## open

```TypeScript
open(type: CameraConcurrentType): Promise<void>
```

Opens the camera with the specified concurrency type. This API uses a promise to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraInput-open(type: CameraConcurrentType): Promise<void>--><!--Device-CameraInput-open(type: CameraConcurrentType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Concurrency type. If the API fails to be called, an error code is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed. |
| [7400107](../errorcode-camera.md#7400107-camera-conflict) | Can not use camera cause of conflict. |
| [7400108](../errorcode-camera.md#7400108-camera-disabled-due-to-security-reasons) | Camera disabled cause of security reason. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## usePhysicalCameraOrientation

```TypeScript
usePhysicalCameraOrientation(isUsed: boolean): void
```

Enables or disables the use of the physical camera orientation.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CameraInput-usePhysicalCameraOrientation(isUsed: boolean): void--><!--Device-CameraInput-usePhysicalCameraOrientation(isUsed: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isUsed | boolean | Yes | Enables or disables the use of the physical camera orientation. **true** to enable,**false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

