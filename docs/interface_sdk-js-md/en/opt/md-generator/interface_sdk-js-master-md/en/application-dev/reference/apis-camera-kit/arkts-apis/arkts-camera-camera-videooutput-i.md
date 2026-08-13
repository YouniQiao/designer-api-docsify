# VideoOutput

VideoOutput implements output information used in a video session. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput).

**Inheritance/Implementation:** VideoOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface VideoOutput--><!--Device-camera-interface VideoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getActiveFrameRate

```TypeScript
getActiveFrameRate(): FrameRateRange
```

Obtains the configured frame rate range. This API is valid only after [setFrameRate](#setFrameRate) is called to set a frame rate range for video streams.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-getActiveFrameRate(): FrameRateRange--><!--Device-VideoOutput-getActiveFrameRate(): FrameRateRange-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameRateRange](arkts-camera-camera-frameraterange-i.md) |

## getActiveProfile

```TypeScript
getActiveProfile(): VideoProfile
```

Obtains the profile that takes effect currently.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-getActiveProfile(): VideoProfile--><!--Device-VideoOutput-getActiveProfile(): VideoProfile-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VideoProfile](arkts-camera-camera-videoprofile-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## getSupportedFrameRates

```TypeScript
getSupportedFrameRates(): Array<FrameRateRange>
```

Obtains the supported frame rates.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-getSupportedFrameRates(): Array<FrameRateRange>--><!--Device-VideoOutput-getSupportedFrameRates(): Array<FrameRateRange>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[FrameRateRange](arkts-camera-camera-frameraterange-i.md)&gt; |

## getVideoRotation

```TypeScript
getVideoRotation(deviceDegree?: number): ImageRotation
```

Obtains the video rotation angle. - Device' natural orientation: the default orientation for using a device. For example, the default orientation of the bar-type phone is in portrait mode, with the charging port facing downward. - Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's natural orientation. For example, the rear camera sensor of a bar-type phone is installed in landscape mode. Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural orientation.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-getVideoRotation(deviceDegree?: int): ImageRotation--><!--Device-VideoOutput-getVideoRotation(deviceDegree?: int): ImageRotation-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceDegree | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageRotation](arkts-camera-camera-imagerotation-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**Since:** 23

**Deprecated since:** -1

<!--Device-VideoOutput-offError(callback?: ErrorCallback): void--><!--Device-VideoOutput-offError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## offFrameEnd

```TypeScript
offFrameEnd(callback?: AsyncCallback<void>): void
```

Unsubscribes from frame end event callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-VideoOutput-offFrameEnd(callback?: AsyncCallback<void>): void--><!--Device-VideoOutput-offFrameEnd(callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

## offFrameStart

```TypeScript
offFrameStart(callback?: AsyncCallback<void>): void
```

Unsubscribes from frame start event callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-VideoOutput-offFrameStart(callback?: AsyncCallback<void>): void--><!--Device-VideoOutput-offFrameStart(callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

## off_error

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from VideoOutput error events.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-VideoOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## off_frameEnd

```TypeScript
off(type: 'frameEnd', callback?: AsyncCallback<void>): void
```

Unsubscribes from video recording stop events.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-off(type: 'frameEnd', callback?: AsyncCallback<void>): void--><!--Device-VideoOutput-off(type: 'frameEnd', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'frameEnd' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

## off_frameStart

```TypeScript
off(type: 'frameStart', callback?: AsyncCallback<void>): void
```

Unsubscribes from video recording start events. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-off(type: 'frameStart', callback?: AsyncCallback<void>): void--><!--Device-VideoOutput-off(type: 'frameStart', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'frameStart' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**Since:** 23

**Deprecated since:** -1

<!--Device-VideoOutput-onError(callback: ErrorCallback): void--><!--Device-VideoOutput-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## onFrameEnd

```TypeScript
onFrameEnd(callback: AsyncCallback<void>): void
```

Subscribes frame end event callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-VideoOutput-onFrameEnd(callback: AsyncCallback<void>): void--><!--Device-VideoOutput-onFrameEnd(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## onFrameStart

```TypeScript
onFrameStart(callback: AsyncCallback<void>): void
```

Subscribes frame start event callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-VideoOutput-onFrameStart(callback: AsyncCallback<void>): void--><!--Device-VideoOutput-onFrameStart(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to VideoOutput error events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## on_frameEnd

```TypeScript
on(type: 'frameEnd', callback: AsyncCallback<void>): void
```

Subscribes to video recording stop events. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-on(type: 'frameEnd', callback: AsyncCallback<void>): void--><!--Device-VideoOutput-on(type: 'frameEnd', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'frameEnd' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## on_frameStart

```TypeScript
on(type: 'frameStart', callback: AsyncCallback<void>): void
```

Subscribes to video recording start events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-on(type: 'frameStart', callback: AsyncCallback<void>): void--><!--Device-VideoOutput-on(type: 'frameStart', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'frameStart' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setFrameRate

```TypeScript
setFrameRate(minFps: number, maxFps: number): void
```

Sets a frame rate range for video streams. The range must be within the supported frame rate range, which can be obtained by calling [getSupportedFrameRates](#getSupportedFrameRates). > **NOTE：**> > This API is valid only in [PhotoSession](arkts-camera-camera-photosession-i.md#PhotoSession) or > [VideoSession](arkts-camera-camera-videosession-i.md#VideoSession) mode. > > Before calling this API, call [getActiveFrameRate](#getActiveFrameRate) to obtain the > current frame rate of the video session. If the delivered frame rate matches the current frame rate, the > delivered frame rate is not applied.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-setFrameRate(minFps: int, maxFps: int): void--><!--Device-VideoOutput-setFrameRate(minFps: int, maxFps: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| minFps | number | Yes |
| maxFps | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400110](../errorcode-camera.md#7400110-configuration-conflicts) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts video recording. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-start(callback: AsyncCallback<void>): void--><!--Device-VideoOutput-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## start

```TypeScript
start(): Promise<void>
```

Starts video recording. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-start(): Promise<void>--><!--Device-VideoOutput-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops video recording. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-stop(callback: AsyncCallback<void>): void--><!--Device-VideoOutput-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## stop

```TypeScript
stop(): Promise<void>
```

Stops video recording. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-stop(): Promise<void>--><!--Device-VideoOutput-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
