# VideoOutput

VideoOutput implements output information used in a video session. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md).

**Inheritance/Implementation:** VideoOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md)

**Since:** 23

<!--Device-camera-interface VideoOutput--><!--Device-camera-interface VideoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## getActiveFrameRate

```TypeScript
getActiveFrameRate(): FrameRateRange
```

Obtains the configured frame rate range. This API is valid only after [setFrameRate](#setframerate) is called to set a frame rate range for video streams.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-getActiveFrameRate(): FrameRateRange--><!--Device-VideoOutput-getActiveFrameRate(): FrameRateRange-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [FrameRateRange](arkts-camera-camera-frameraterange-i.md) | Frame rate range. |

## getActiveProfile

```TypeScript
getActiveProfile(): VideoProfile
```

Obtains the profile that takes effect currently.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-getActiveProfile(): VideoProfile--><!--Device-VideoOutput-getActiveProfile(): VideoProfile-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [VideoProfile](arkts-camera-camera-videoprofile-i.md) | Profile obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getSupportedFrameRates

```TypeScript
getSupportedFrameRates(): Array<FrameRateRange>
```

Obtains the supported frame rates.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-getSupportedFrameRates(): Array<FrameRateRange>--><!--Device-VideoOutput-getSupportedFrameRates(): Array<FrameRateRange>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[FrameRateRange](arkts-camera-camera-frameraterange-i.md)&gt; | Array of supported frame rates. If the API call fails, undefined is returned. |

## getVideoRotation

```TypeScript
getVideoRotation(deviceDegree?: int): ImageRotation
```

Obtains the video rotation angle. - Device' natural orientation: the default orientation for using a device. For example, the default orientation of the bar-type phone is in portrait mode, with the charging port facing downward. - Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's natural orientation. For example, the rear camera sensor of a bar-type phone is installed in landscape mode. Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural orientation.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-getVideoRotation(deviceDegree?: int): ImageRotation--><!--Device-VideoOutput-getVideoRotation(deviceDegree?: int): ImageRotation-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceDegree | int | No | Device rotation angle, measured in degrees, within the range of [0, 360]. <br> Since API version 23, the input parameter **deviceDegree** is optional. If no parameter is passed, the system obtains the **deviceDegree** value to calculate the video rotation angle.<br>**Since:** 23 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageRotation](arkts-camera-camera-imagerotation-e.md) | Returns the rotation angle of a video. If the API call fails, undefined is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 22 |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**Since:** 23

<!--Device-VideoOutput-offError(callback?: ErrorCallback): void--><!--Device-VideoOutput-offError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) | No | Callback used to get the video output errors. |

## offFrameEnd

```TypeScript
offFrameEnd(callback?: AsyncCallback<void>): void
```

Unsubscribes from frame end event callback.

**Since:** 23

<!--Device-VideoOutput-offFrameEnd(callback?: AsyncCallback<void>): void--><!--Device-VideoOutput-offFrameEnd(callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | No | Callback used to return the result. |

## offFrameStart

```TypeScript
offFrameStart(callback?: AsyncCallback<void>): void
```

Unsubscribes from frame start event callback.

**Since:** 23

<!--Device-VideoOutput-offFrameStart(callback?: AsyncCallback<void>): void--><!--Device-VideoOutput-offFrameStart(callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | No | Callback used to return the result. |

## off_error('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from VideoOutput error events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-VideoOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a photoOutput instance is created. |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_frameEnd('frameEnd')

```TypeScript
off(type: 'frameEnd', callback?: AsyncCallback<void>): void
```

Unsubscribes from video recording stop events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-off(type: 'frameEnd', callback?: AsyncCallback<void>): void--><!--Device-VideoOutput-off(type: 'frameEnd', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameEnd' | Yes | Event type. The value is fixed at **'frameEnd'**. The event can be listened for when a videoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_frameStart('frameStart')

```TypeScript
off(type: 'frameStart', callback?: AsyncCallback<void>): void
```

Unsubscribes from video recording start events. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-off(type: 'frameStart', callback?: AsyncCallback<void>): void--><!--Device-VideoOutput-off(type: 'frameStart', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameStart' | Yes | Event type. The value is fixed at **'frameStart'**. The event can be listened for when a videoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**Since:** 23

<!--Device-VideoOutput-onError(callback: ErrorCallback): void--><!--Device-VideoOutput-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) | Yes | Callback used to get the video output errors. |

## onFrameEnd

```TypeScript
onFrameEnd(callback: AsyncCallback<void>): void
```

Subscribes frame end event callback.

**Since:** 23

<!--Device-VideoOutput-onFrameEnd(callback: AsyncCallback<void>): void--><!--Device-VideoOutput-onFrameEnd(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

## onFrameStart

```TypeScript
onFrameStart(callback: AsyncCallback<void>): void
```

Subscribes frame start event callback.

**Since:** 23

<!--Device-VideoOutput-onFrameStart(callback: AsyncCallback<void>): void--><!--Device-VideoOutput-onFrameStart(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

## on_error('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to VideoOutput error events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a videoOutput instance is created. This event is triggered and the corresponding error message is returned when an error occurs during the use of a recording-related API such as [start](#start) or [CameraOutput.release](arkts-camera-camera-cameraoutput-i.md#release). |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) | Yes | Callback used to return an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md). |

## on_frameEnd('frameEnd')

```TypeScript
on(type: 'frameEnd', callback: AsyncCallback<void>): void
```

Subscribes to video recording stop events. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-on(type: 'frameEnd', callback: AsyncCallback<void>): void--><!--Device-VideoOutput-on(type: 'frameEnd', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameEnd' | Yes | Event type. The value is fixed at **'frameEnd'**. The event can be listened for when a videoOutput instance is created. This event is triggered and returned when the last frame of recording is complete. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. The recording ends as long as this event is returned. |

## on_frameStart('frameStart')

```TypeScript
on(type: 'frameStart', callback: AsyncCallback<void>): void
```

Subscribes to video recording start events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-on(type: 'frameStart', callback: AsyncCallback<void>): void--><!--Device-VideoOutput-on(type: 'frameStart', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameStart' | Yes | Event type. The value is fixed at **'frameStart'**. The event can be listened for when a videoOutput instance is created. The event is triggered and the corresponding information is returned when the bottom layer starts exposure for the first time. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. The recording starts as long as this event is returned. |

## setFrameRate

```TypeScript
setFrameRate(minFps: int, maxFps: int): void
```

Sets a frame rate range for video streams. The range must be within the supported frame rate range, which can be obtained by calling [getSupportedFrameRates](#getsupportedframerates). > **NOTE：**> > This API is valid only in [PhotoSession](arkts-camera-camera-photosession-i.md) or > [VideoSession](arkts-camera-camera-videosession-i.md) mode. > > Before calling this API, call [getActiveFrameRate](#getactiveframerate) to obtain the > current frame rate of the video session. If the delivered frame rate matches the current frame rate, the > delivered frame rate is not applied.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-setFrameRate(minFps: int, maxFps: int): void--><!--Device-VideoOutput-setFrameRate(minFps: int, maxFps: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minFps | int | Yes | Minimum frame rate, in fps. When the maximum value is less than the minimum value, the API does not take effect. |
| maxFps | int | Yes | Maximum frame rate, in fps. When the minimum value is greater than the maximum value, the API does not take effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400110](../errorcode-camera.md#7400110-configuration-conflicts) | Unresolved conflicts with current configurations. |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts video recording. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-start(callback: AsyncCallback<void>): void--><!--Device-VideoOutput-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If video recording starts successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## start

```TypeScript
start(): Promise<void>
```

Starts video recording. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-start(): Promise<void>--><!--Device-VideoOutput-start(): Promise<void>-End-->

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

Stops video recording. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-stop(callback: AsyncCallback<void>): void--><!--Device-VideoOutput-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If video recording stops successfully, **err** is **undefined**; otherwise, **err** is an error object. |

## stop

```TypeScript
stop(): Promise<void>
```

Stops video recording. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-stop(): Promise<void>--><!--Device-VideoOutput-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

