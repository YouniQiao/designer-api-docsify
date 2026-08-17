# PhotoOutput

PhotoOutput implements output information used in a photo session. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md#cameraoutput).

**Inheritance/Implementation:** PhotoOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md#cameraoutput)

**Since:** 23

<!--Device-camera-interface PhotoOutput--><!--Device-camera-interface PhotoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## capture

```TypeScript
capture(callback: AsyncCallback<void>): void
```

Captures a photo with the default photo capture parameters. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-capture(callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-capture(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the photo is successfully captured with the default parameters, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md#cameraerrorcode). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) | Session not running. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## capture

```TypeScript
capture(): Promise<void>
```

Captures a photo with the default photo capture parameters. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-capture(): Promise<void>--><!--Device-PhotoOutput-capture(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) | Session not running. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## capture

```TypeScript
capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void
```

Captures a photo with the specified photo capture parameters. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) | Yes | Photo capture settings. If the input data is of the **undefined** type, a photo capture operation is triggered based on the default settings. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation fails, an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md#cameraerrorcode) is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400104](../errorcode-camera.md#7400104-session-not-running) | Session not running. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## capture

```TypeScript
capture(setting: PhotoCaptureSetting): Promise<void>
```

Captures a photo with the specified photo capture parameters. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting): Promise<void>--><!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) | Yes | Photo capture settings. If the input data is of the **undefined** type, a photo capture operation is triggered based on the default settings. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400104](../errorcode-camera.md#7400104-session-not-running) | Session not running. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## enableAutoExtendedGainmapDelivery

```TypeScript
enableAutoExtendedGainmapDelivery(enabled: boolean): void
```

Enables or disables automatic extended gain map delivery.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PhotoOutput-enableAutoExtendedGainmapDelivery(enabled: boolean): void--><!--Device-PhotoOutput-enableAutoExtendedGainmapDelivery(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable automatic extended gain map delivery. The value **true** indicates it is enabled, and the value **false** indicates it is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## enableMirror

```TypeScript
enableMirror(enabled: boolean): void
```

Enables or disables dynamic photo capture. Before calling this API, check whether moving photo capture is supported by calling [isMovingPhotoSupported](#ismovingphotosupported) and whether mirroring is supported by calling [isMirrorSupported](#ismirrorsupported).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-enableMirror(enabled: boolean): void--><!--Device-PhotoOutput-enableMirror(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Enables or disables dynamic photo capture. **true** to enable, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## enableMovingPhoto

```TypeScript
enableMovingPhoto(enabled: boolean): void
```

Enables or disables the feature of taking moving photos.

**Since:** 23

**Required permissions:** ohos.permission.MICROPHONE

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-enableMovingPhoto(enabled: boolean): void--><!--Device-PhotoOutput-enableMovingPhoto(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Enables or disables the feature of taking moving photos. **true** to enable, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getActiveProfile

```TypeScript
getActiveProfile(): Profile
```

Obtains the profile that takes effect currently.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-getActiveProfile(): Profile--><!--Device-PhotoOutput-getActiveProfile(): Profile-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Profile](arkts-camera-camera-profile-i.md) | Profile obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getPhotoRotation

```TypeScript
getPhotoRotation(deviceDegree?: int): ImageRotation
```

Obtains the photo rotation angle. - Device' natural orientation: the default orientation for using a device. For example, the default orientation of the bar-type phone is in portrait mode, with the charging port facing downward. - Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's natural orientation. For example, the rear camera sensor of a bar-type phone is installed in landscape mode. Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural orientation.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-getPhotoRotation(deviceDegree?: int): ImageRotation--><!--Device-PhotoOutput-getPhotoRotation(deviceDegree?: int): ImageRotation-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceDegree | int | No | Device rotation angle, measured in degrees, within the range of [0, 360]. <br>If the input value goes beyond this range, the system uses the remainder of the input value divided by 36 0. <br>Since API version 23, the input parameter **deviceDegree** is optional. If no parameter is passed, the system obtains the **deviceDegree** value to calculate the photo rotation angle.<br>**Since:** 23 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageRotation](arkts-camera-camera-imagerotation-e.md) | Rotation angle of the photo. If the API call fails, undefined is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 22 |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getSupportedMovingPhotoVideoCodecTypes

```TypeScript
getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>
```

Obtains the supported video codec types of moving photos.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>--><!--Device-PhotoOutput-getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[VideoCodecType](arkts-camera-camera-videocodectype-e.md)&gt; | Array holding the supported video codec types. If the API call fails, undefined is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## isAutoExtendedGainmapDeliverySupported

```TypeScript
isAutoExtendedGainmapDeliverySupported(): boolean
```

Checks whether automatic extended gain map delivery is supported.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PhotoOutput-isAutoExtendedGainmapDeliverySupported(): boolean--><!--Device-PhotoOutput-isAutoExtendedGainmapDeliverySupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether automatic extended gain map delivery is supported. The value **true** indicates it is supported, and the value **false** indicates it is not supported. |

## isMirrorSupported

```TypeScript
isMirrorSupported(): boolean
```

Checks whether mirror photography is supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-isMirrorSupported(): boolean--><!--Device-PhotoOutput-isMirrorSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of mirror photography. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

## isMovingPhotoSupported

```TypeScript
isMovingPhotoSupported(): boolean
```

Checks whether taking moving photos is supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-isMovingPhotoSupported(): boolean--><!--Device-PhotoOutput-isMovingPhotoSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of taking moving photos. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## isPhotoQualityPrioritizationSupported

```TypeScript
isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean
```

Checks whether the specified photo quality prioritization strategy is supported.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-PhotoOutput-isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean--><!--Device-PhotoOutput-isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](arkts-camera-camera-photoqualityprioritization-e.md) | Yes | Photo quality prioritization strategy. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of the specified photo quality prioritization strategy. **true** if supported, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

## offCaptureEnd

```TypeScript
offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void
```

Unsubscribes from capture end event callback.

**Since:** 23

<!--Device-PhotoOutput-offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md)&gt; | No | Callback used to get the capture end information. |

## offCapturePhotoAvailable

```TypeScript
offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void
```

Unsubscribes from the events of returning full-quality images and uncompressed images. This API uses an asynchronous callback to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoOutput-offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void--><!--Device-PhotoOutput-offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CapturePhoto](arkts-camera-camera-capturephoto-i.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## offCaptureReady

```TypeScript
offCaptureReady(callback?: AsyncCallback<void>): void
```

Unsubscribes from capture ready event callback.

**Since:** 23

<!--Device-PhotoOutput-offCaptureReady(callback?: AsyncCallback<void>): void--><!--Device-PhotoOutput-offCaptureReady(callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | Callback used to notice capture ready. |

## offCaptureStartWithInfo

```TypeScript
offCaptureStartWithInfo(callback?: AsyncCallback<CaptureStartInfo>): void
```

Unsubscribes from capture start event callback.

**Since:** 23

<!--Device-PhotoOutput-offCaptureStartWithInfo(callback?: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-offCaptureStartWithInfo(callback?: AsyncCallback<CaptureStartInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)&gt; | No | Callback used to get the capture start info. |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**Since:** 23

<!--Device-PhotoOutput-offError(callback?: ErrorCallback): void--><!--Device-PhotoOutput-offError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to get the photo output errors. |

## offEstimatedCaptureDuration

```TypeScript
offEstimatedCaptureDuration(callback?: AsyncCallback<double>): void
```

Unsubscribes from estimated capture duration event callback.

**Since:** 23

<!--Device-PhotoOutput-offEstimatedCaptureDuration(callback?: AsyncCallback<double>): void--><!--Device-PhotoOutput-offEstimatedCaptureDuration(callback?: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | No | Callback used to notify the estimated capture duration (in milliseconds). |

## offFrameShutter

```TypeScript
offFrameShutter(callback?: AsyncCallback<FrameShutterInfo>): void
```

Unsubscribes from frame shutter event callback.

**Since:** 23

<!--Device-PhotoOutput-offFrameShutter(callback?: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-offFrameShutter(callback?: AsyncCallback<FrameShutterInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md)&gt; | No | Callback used to get the frame shutter information. |

## offFrameShutterEnd

```TypeScript
offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void
```

Unsubscribes from frame shutter end event callback.

**Since:** 23

<!--Device-PhotoOutput-offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md)&gt; | No | Callback used to get the frame shutter end information. |

## offPhotoAssetAvailable

```TypeScript
offPhotoAssetAvailable(callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

Unsubscribes photo asset event callback.

**Since:** 23

<!--Device-PhotoOutput-offPhotoAssetAvailable(callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-offPhotoAssetAvailable(callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | No | Callback used to get the asset. |

## offPhotoAvailable

```TypeScript
offPhotoAvailable(callback?: AsyncCallback<Photo>): void
```

Unsubscribes photo available event callback.

**Since:** 23

<!--Device-PhotoOutput-offPhotoAvailable(callback?: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-offPhotoAvailable(callback?: AsyncCallback<Photo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Photo](arkts-camera-camera-photo-i.md)&gt; | No | Callback used to get the Photo. |

## off_captureEnd

```TypeScript
off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void
```

Unsubscribes from capture end events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureEnd' | Yes | Event type. The value is fixed at **'captureEnd'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_captureReady

```TypeScript
off(type: 'captureReady', callback?: AsyncCallback<void>): void
```

Unsubscribes from capture ready events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'captureReady', callback?: AsyncCallback<void>): void--><!--Device-PhotoOutput-off(type: 'captureReady', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureReady' | Yes | Event type. The value is fixed at **'captureReady'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_captureStart

```TypeScript
off(type: 'captureStart', callback?: AsyncCallback<number>): void
```

Unsubscribes from capture start events. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [off](#offphotoavailable)(type: 'captureStartWithInfo', callback?: AsyncCallback&lt;CaptureStartInfo&gt;)

<!--Device-PhotoOutput-off(type: 'captureStart', callback?: AsyncCallback<number>): void--><!--Device-PhotoOutput-off(type: 'captureStart', callback?: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureStart' | Yes | Event type. The value is fixed at **'captureStart'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_captureStartWithInfo

```TypeScript
off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void
```

Unsubscribes from capture start events.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureStartWithInfo' | Yes | Event type. The value is fixed at **'captureStartWithInfo'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_error

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from PhotoOutput error events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-PhotoOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a photoOutput instance is created. |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_estimatedCaptureDuration

```TypeScript
off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<double>): void
```

Unsubscribes from estimated capture duration events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<double>): void--><!--Device-PhotoOutput-off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'estimatedCaptureDuration' | Yes | Event type. The value is fixed at **'estimatedCaptureDuration'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_frameShutter

```TypeScript
off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void
```

Unsubscribes from frame shutter events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameShutter' | Yes | Event type. The value is fixed at **'frameShutter'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_frameShutterEnd

```TypeScript
off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void
```

Unsubscribes from frame shutter end events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameShutterEnd' | Yes | Event type. The value is fixed at **'frameShutterEnd'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_photoAssetAvailable

```TypeScript
off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

Unsubscribes from photo asset available events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'photoAssetAvailable' | Yes | Event type. The value is fixed at **'photoAssetAvailable'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | No | Callback used for unsubscription. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off_photoAvailable

```TypeScript
off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void
```

Unsubscribes from the events of returning available photos.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'photoAvailable' | Yes | Event type. The value is fixed at **'photoAvailable'**. The event can be listened for when a **photoOutput** instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Photo](arkts-camera-camera-photo-i.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## onCaptureEnd

```TypeScript
onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void
```

Subscribes capture end event callback.

**Since:** 23

<!--Device-PhotoOutput-onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md)&gt; | Yes | Callback used to get the capture end information. |

## onCapturePhotoAvailable

```TypeScript
onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void
```

Subscribes to the events of returning full-quality images and uncompressed images. This API uses an asynchronous callback to return the result. > **NOTE：**> > - You cannot call > [offCapturePhotoAvailable](#offcapturephotoavailable) > to unregister the callback in the callback listened by this API. > > - This API can be used to register listeners only when uncompressed images in the YUV format are captured.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoOutput-onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void--><!--Device-PhotoOutput-onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CapturePhoto](arkts-camera-camera-capturephoto-i.md)&gt; | Yes | Callback used to listen for the event of returning full-quality images and uncompressed images. |

## onCaptureReady

```TypeScript
onCaptureReady(callback: AsyncCallback<void>): void
```

Subscribes capture ready event callback. After receiving the callback, can proceed to the next capture

**Since:** 23

<!--Device-PhotoOutput-onCaptureReady(callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-onCaptureReady(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to notice capture ready. |

## onCaptureStartWithInfo

```TypeScript
onCaptureStartWithInfo(callback: AsyncCallback<CaptureStartInfo>): void
```

Subscribes capture start event callback.

**Since:** 23

<!--Device-PhotoOutput-onCaptureStartWithInfo(callback: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-onCaptureStartWithInfo(callback: AsyncCallback<CaptureStartInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)&gt; | Yes | Callback used to get the capture start info. |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**Since:** 23

<!--Device-PhotoOutput-onError(callback: ErrorCallback): void--><!--Device-PhotoOutput-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to get the photo output errors. |

## onEstimatedCaptureDuration

```TypeScript
onEstimatedCaptureDuration(callback: AsyncCallback<double>): void
```

Subscribes estimated capture duration event callback.

**Since:** 23

<!--Device-PhotoOutput-onEstimatedCaptureDuration(callback: AsyncCallback<double>): void--><!--Device-PhotoOutput-onEstimatedCaptureDuration(callback: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | Yes | Callback used to notify the estimated capture duration (in milliseconds). |

## onFrameShutter

```TypeScript
onFrameShutter(callback: AsyncCallback<FrameShutterInfo>): void
```

Subscribes frame shutter event callback.

**Since:** 23

<!--Device-PhotoOutput-onFrameShutter(callback: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-onFrameShutter(callback: AsyncCallback<FrameShutterInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md)&gt; | Yes | Callback used to get the frame shutter information. |

## onFrameShutterEnd

```TypeScript
onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void
```

Subscribes frame shutter end event callback.

**Since:** 23

<!--Device-PhotoOutput-onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md)&gt; | Yes | Callback used to get the frame shutter end information. |

## onPhotoAssetAvailable

```TypeScript
onPhotoAssetAvailable(callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

Subscribes to photo asset event callback. This API processes deferred photo delivery data by quickly displaying low-quality images to give users the impression of faster photo capture, while also generating high-quality images to maintain the final output quality. For details about the design specifications, see [Optimizing Deferred Photo Delivery](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-camera-shot2see).

**Since:** 23

<!--Device-PhotoOutput-onPhotoAssetAvailable(callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-onPhotoAssetAvailable(callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | Yes | Callback used to get the asset. |

## onPhotoAvailable

```TypeScript
onPhotoAvailable(callback: AsyncCallback<Photo>): void
```

Subscribes photo available event callback.

**Since:** 23

<!--Device-PhotoOutput-onPhotoAvailable(callback: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-onPhotoAvailable(callback: AsyncCallback<Photo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Photo](arkts-camera-camera-photo-i.md)&gt; | Yes | Callback used to get the Photo. |

## on_captureEnd

```TypeScript
on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void
```

Subscribes to capture end events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureEnd' | Yes | Event type. The value is fixed at **'captureEnd'**. The event can be listened for when a photoOutput instance is created. This event is triggered and the corresponding information is returned when the photo capture is complete. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md)&gt; | Yes | Callback used to return the result. |

## on_captureReady

```TypeScript
on(type: 'captureReady', callback: AsyncCallback<void>): void
```

Subscribes to capture ready events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'captureReady', callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-on(type: 'captureReady', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureReady' | Yes | Event type. The value is fixed at **'captureReady'**. The event can be listened for when a photoOutput instance is created. The event is triggered and the corresponding information is returned when it is ready to take the next photo. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

## on_captureStart

```TypeScript
on(type: 'captureStart', callback: AsyncCallback<number>): void
```

Subscribes to capture start events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [on](#onphotoavailable)(type: 'captureStartWithInfo', callback: AsyncCallback&lt;CaptureStartInfo&gt;)

<!--Device-PhotoOutput-on(type: 'captureStart', callback: AsyncCallback<number>): void--><!--Device-PhotoOutput-on(type: 'captureStart', callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureStart' | Yes | Event type. The value is fixed at **'captureStart'**. The event can be listened for when a photoOutput instance is created. This event is triggered and returned when the bottom layer starts exposure each time a photo is taken. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the capture ID. |

## on_captureStartWithInfo

```TypeScript
on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void
```

Subscribes to capture start events. This API uses an asynchronous callback to return the [capture start ID](arkts-camera-camera-capturestartinfo-i.md#capturestartinfo). > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureStartWithInfo' | Yes | Event type. The value is fixed at **'captureStartWithInfo'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)&gt; | Yes | Callback used to return the capture ID. |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to PhotoOutput error events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-PhotoOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a photoOutput instance is created. This event is triggered and the corresponding error message is returned when an error occurs during the calling of a photo-related API. |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to return an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md#cameraerrorcode). |

## on_estimatedCaptureDuration

```TypeScript
on(type: 'estimatedCaptureDuration', callback: AsyncCallback<double>): void
```

Subscribes to estimated capture duration events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'estimatedCaptureDuration', callback: AsyncCallback<double>): void--><!--Device-PhotoOutput-on(type: 'estimatedCaptureDuration', callback: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'estimatedCaptureDuration' | Yes | Event type. The value is fixed at **'estimatedCaptureDuration'**. The event can be listened for when a photoOutput instance is created. This event is triggered and the corresponding information is returned when the photo capture is complete. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | Yes | Callback used to return the estimated duration when the sensor captures frames at the bottom layer in a single capture, measured in units of milliseconds. If **–1** is reported, there is no estimated duration. |

## on_frameShutter

```TypeScript
on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void
```

Subscribes to frame shutter events. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameShutter' | Yes | Event type. The value is fixed at **'frameShutter'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md)&gt; | Yes | Callback used to return the result. A new photo capture request can be delivered as long as this event is returned. |

## on_frameShutterEnd

```TypeScript
on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void
```

Subscribes to frame shutter end events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameShutterEnd' | Yes | Event type. The value is fixed at **'frameShutterEnd'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md)&gt; | Yes | Callback used to return the result. It is invoked when the frame shutter ends. |

## on_photoAssetAvailable

```TypeScript
on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

Subscribes to photo asset available events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'photoAssetAvailable' | Yes | Event type. The value is fixed at **'photoAssetAvailable'**. The event can be listened for when a photoOutput instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | Yes | Callback used to return the photo asset. |

## on_photoAvailable

```TypeScript
on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void
```

Subscribes to the events of returning available photos. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'photoAvailable' | Yes | Event type. The value is fixed at **'photoAvailable'**. The event can be listened for when a **photoOutput** instance is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Photo](arkts-camera-camera-photo-i.md)&gt; | Yes | Callback used to listen for the event of returning available photos. |

## setMovingPhotoVideoCodecType

```TypeScript
setMovingPhotoVideoCodecType(codecType: VideoCodecType): void
```

Sets a video codec type for moving photos.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-setMovingPhotoVideoCodecType(codecType: VideoCodecType): void--><!--Device-PhotoOutput-setMovingPhotoVideoCodecType(codecType: VideoCodecType): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| codecType | [VideoCodecType](arkts-camera-camera-videocodectype-e.md) | Yes | Video codec type. <br>If the value is not within the enumerated value range, this parameter does not take effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## setPhotoQualityPrioritization

```TypeScript
setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void
```

Sets the photo quality prioritization strategy. Before setting the strategy, you can call [isPhotoQualityPrioritizationSupported](#isphotoqualityprioritizationsupported) to check whether the device supports the specified photo quality prioritization strategy.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-PhotoOutput-setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void--><!--Device-PhotoOutput-setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](arkts-camera-camera-photoqualityprioritization-e.md) | Yes | Photo quality prioritization strategy. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

