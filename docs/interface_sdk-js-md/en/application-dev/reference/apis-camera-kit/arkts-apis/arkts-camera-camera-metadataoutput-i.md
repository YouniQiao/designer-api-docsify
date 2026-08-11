# MetadataOutput

MetadataOutput implements metadata streams. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md).

**Inheritance/Implementation:** MetadataOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface MetadataOutput extends CameraOutput--><!--Device-camera-interface MetadataOutput extends CameraOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## addMetadataObjectTypes

```TypeScript
addMetadataObjectTypes(types: Array<MetadataObjectType>): void
```

Adds the types of metadata objects to be detected.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MetadataOutput-addMetadataObjectTypes(types: Array<MetadataObjectType>): void--><!--Device-MetadataOutput-addMetadataObjectTypes(types: Array<MetadataObjectType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;MetadataObjectType&gt; | Yes | Metadata object types, which are obtained through **getSupportedOutputCapability**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 13 - 22 |

## isLockMetadataObjectTrackingSupported

```TypeScript
isLockMetadataObjectTrackingSupported(): boolean
```

Checks whether the device supports the function of locking a metadata object (such as a cat or dog face) for tracking.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataOutput-isLockMetadataObjectTrackingSupported(): boolean--><!--Device-MetadataOutput-isLockMetadataObjectTrackingSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the device supports the function of locking a metadata object for tracking. **true** if supported; **false** otherwise. |

## lockMetadataObjectTracking

```TypeScript
lockMetadataObjectTracking(point: Point): void
```

Locks a metadata object (such as a cat or dog face) for tracking.

> **NOTE：**
> 
> - This function tracks the object pointed to by **point**. If such object does not exist, this function does
> not take effect.
> 
> - Locking for tracking is automatically canceled when the tracked object has left the viewfinder range for more
> than three seconds or the object is unlocked.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataOutput-lockMetadataObjectTracking(point: Point): void--><!--Device-MetadataOutput-lockMetadataObjectTracking(point: Point): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-camera-camera-point-i.md) | Yes | Point used to lock the metadata object for tracking. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## off('metadataObjectsAvailable')

```TypeScript
off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void
```

Unsubscribes from events indicating available metadata objects.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataOutput-off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'metadataObjectsAvailable' | Yes | Event type. The value is fixed at **'metadataObjectsAvailable'**. The event can be listened for when a metadataOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;MetadataObject&gt;&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from VideoOutput error events.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-MetadataOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a photoOutput instance is created. |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-MetadataOutput-offError(callback?: ErrorCallback): void--><!--Device-MetadataOutput-offError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to get the metadata output errors. |

## offMetadataObjectsAvailable

```TypeScript
offMetadataObjectsAvailable(callback?: AsyncCallback<Array<MetadataObject>>): void
```

Unsubscribes from metadata objects available event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-MetadataOutput-offMetadataObjectsAvailable(callback?: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-offMetadataObjectsAvailable(callback?: AsyncCallback<Array<MetadataObject>>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;MetadataObject&gt;&gt; | No | Callback used to get the available metadata objects. |

## on('metadataObjectsAvailable')

```TypeScript
on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void
```

Subscribes to events indicating available metadata objects. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataOutput-on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'metadataObjectsAvailable' | Yes | Event type. The value is fixed at **'metadataObjectsAvailable'**. The event can be listened for when a metadataOutput instance is created. &lt;br&gt;This event is triggered and the corresponding metadata is returned when valid metadata is detected. If the input field is incorrect, no valid listening will be created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;MetadataObject&gt;&gt; | Yes | Callback used to return the metadata. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to metadata error events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-MetadataOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a metadataOutput instance is created. This event is triggered and the corresponding error message is returned when an error occurs during the use of a metadata-related API such as [start](arkts-camera-camera-metadataoutput-i.md#start) or [CameraOutput.release](arkts-camera-camera-cameraoutput-i.md#release). |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to return an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md). |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-MetadataOutput-onError(callback: ErrorCallback): void--><!--Device-MetadataOutput-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to get the metadata output errors. |

## onMetadataObjectsAvailable

```TypeScript
onMetadataObjectsAvailable(callback: AsyncCallback<Array<MetadataObject>>): void
```

Subscribes to metadata objects available event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-MetadataOutput-onMetadataObjectsAvailable(callback: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-onMetadataObjectsAvailable(callback: AsyncCallback<Array<MetadataObject>>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;MetadataObject&gt;&gt; | Yes | Callback used to get the available metadata objects. |

## removeMetadataObjectTypes

```TypeScript
removeMetadataObjectTypes(types: Array<MetadataObjectType>): void
```

Removes the types of metadata objects to be detected.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MetadataOutput-removeMetadataObjectTypes(types: Array<MetadataObjectType>): void--><!--Device-MetadataOutput-removeMetadataObjectTypes(types: Array<MetadataObjectType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;MetadataObjectType&gt; | Yes | Metadata object types, which are obtained through **getSupportedOutputCapability**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 13 - 22 |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts to output metadata. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataOutput-start(callback: AsyncCallback<void>): void--><!--Device-MetadataOutput-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the metadata output starts successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## start

```TypeScript
start(): Promise<void>
```

Starts to output metadata. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataOutput-start(): Promise<void>--><!--Device-MetadataOutput-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops outputting metadata. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataOutput-stop(callback: AsyncCallback<void>): void--><!--Device-MetadataOutput-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the metadata output stops successfully, **err** is **undefined**; otherwise, **err** is an error object. |

## stop

```TypeScript
stop(): Promise<void>
```

Stops outputting metadata. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataOutput-stop(): Promise<void>--><!--Device-MetadataOutput-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## unlockMetadataObjectTracking

```TypeScript
unlockMetadataObjectTracking(): void
```

Unlocks the metadata object (such as a cat or dog face) for tracking.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataOutput-unlockMetadataObjectTracking(): void--><!--Device-MetadataOutput-unlockMetadataObjectTracking(): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

