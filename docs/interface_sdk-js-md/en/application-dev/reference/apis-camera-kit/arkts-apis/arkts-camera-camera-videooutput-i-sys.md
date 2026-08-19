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

## attachMetaSurface

```TypeScript
attachMetaSurface(surfaceId: string, type: VideoMetaType): void
```

Attach a meta surface to VideoOutput.

**Since:** 23

<!--Device-VideoOutput-attachMetaSurface(surfaceId: string, type: VideoMetaType): void--><!--Device-VideoOutput-attachMetaSurface(surfaceId: string, type: VideoMetaType): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | Surface object id used for receiving meta infos. |
| type | [VideoMetaType](arkts-camera-camera-videometatype-e-sys.md) | Yes | Video meta type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## enableAutoDeferredVideoEnhancement

```TypeScript
enableAutoDeferredVideoEnhancement(enabled: boolean): void
```

Enable auto deferred video enhancement if needed.

**Since:** 23

<!--Device-VideoOutput-enableAutoDeferredVideoEnhancement(enabled: boolean): void--><!--Device-VideoOutput-enableAutoDeferredVideoEnhancement(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Status of auto deferred video enhancement. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## enableAutoVideoFrameRate

```TypeScript
enableAutoVideoFrameRate(enabled: boolean): void
```

Enable auto frame rate for video capture.

**Since:** 23

<!--Device-VideoOutput-enableAutoVideoFrameRate(enabled: boolean): void--><!--Device-VideoOutput-enableAutoVideoFrameRate(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | enable auto frame rate if TRUE. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## enableMirror

```TypeScript
enableMirror(enabled: boolean): void
```

Enables or disables mirror recording. - Before calling this API, check whether mirror recording is supported by using [isMirrorSupported](#ismirrorsupported). - After enabling or disabling mirror recording, call [getVideoRotation](arkts-camera-camera-videooutput-i.md#getvideorotation) to obtain the rotation angle and [updateRotation](../../apis-media-kit/arkts-apis/arkts-media-media-avrecorder-i.md#updaterotation) to update the rotation angle.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-enableMirror(enabled: boolean): void--><!--Device-VideoOutput-enableMirror(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable mirror recording. **true** to enable, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 14 |

## getSupportedRotations

```TypeScript
getSupportedRotations(): Array<ImageRotation>
```

Get supported video rotations.

**Since:** 23

<!--Device-VideoOutput-getSupportedRotations(): Array<ImageRotation>--><!--Device-VideoOutput-getSupportedRotations(): Array<ImageRotation>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[ImageRotation](arkts-camera-camera-imagerotation-e.md)&gt; | The array of supported video rotations. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## getSupportedVideoMetaTypes

```TypeScript
getSupportedVideoMetaTypes(): Array<VideoMetaType>
```

Get supported video meta types.

**Since:** 23

<!--Device-VideoOutput-getSupportedVideoMetaTypes(): Array<VideoMetaType>--><!--Device-VideoOutput-getSupportedVideoMetaTypes(): Array<VideoMetaType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[VideoMetaType](arkts-camera-camera-videometatype-e-sys.md)&gt; | The array of supported video meta type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## isAutoDeferredVideoEnhancementEnabled

```TypeScript
isAutoDeferredVideoEnhancementEnabled(): boolean
```

Confirm if auto deferred video enhancement is enabled.

**Since:** 23

<!--Device-VideoOutput-isAutoDeferredVideoEnhancementEnabled(): boolean--><!--Device-VideoOutput-isAutoDeferredVideoEnhancementEnabled(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | TRUE if auto deferred video enhancement is enabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## isAutoDeferredVideoEnhancementSupported

```TypeScript
isAutoDeferredVideoEnhancementSupported(): boolean
```

Confirm if auto deferred video enhancement is supported in the specific device.

**Since:** 23

<!--Device-VideoOutput-isAutoDeferredVideoEnhancementSupported(): boolean--><!--Device-VideoOutput-isAutoDeferredVideoEnhancementSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | TRUE if auto deferred video enhancement is supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## isAutoVideoFrameRateSupported

```TypeScript
isAutoVideoFrameRateSupported(): boolean
```

Determine whether auto frame rate is supported.

**Since:** 23

<!--Device-VideoOutput-isAutoVideoFrameRateSupported(): boolean--><!--Device-VideoOutput-isAutoVideoFrameRateSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Is auto frame rate supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## isMirrorSupported

```TypeScript
isMirrorSupported(): boolean
```

Checks whether mirror recording is supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoOutput-isMirrorSupported(): boolean--><!--Device-VideoOutput-isMirrorSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of mirror recording. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 14 |

## isRotationSupported

```TypeScript
isRotationSupported(): boolean
```

Determine whether video rotation is supported.

**Since:** 23

<!--Device-VideoOutput-isRotationSupported(): boolean--><!--Device-VideoOutput-isRotationSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Is video rotation supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## offDeferredVideoEnhancementInfo

```TypeScript
offDeferredVideoEnhancementInfo(callback?: AsyncCallback<DeferredVideoEnhancementInfo>): void
```

Unsubscribes from deferred video enhancement info callback.

**Since:** 23

<!--Device-VideoOutput-offDeferredVideoEnhancementInfo(callback?: AsyncCallback<DeferredVideoEnhancementInfo>): void--><!--Device-VideoOutput-offDeferredVideoEnhancementInfo(callback?: AsyncCallback<DeferredVideoEnhancementInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DeferredVideoEnhancementInfo](arkts-camera-camera-deferredvideoenhancementinfo-i-sys.md)&gt; | No | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## off_deferredVideoEnhancementInfo('deferredVideoEnhancementInfo')

```TypeScript
off(type: 'deferredVideoEnhancementInfo', callback?: AsyncCallback<DeferredVideoEnhancementInfo>): void
```

Unsubscribes from deferred video enhancement info callback.

**Since:** 13

<!--Device-VideoOutput-off(type: 'deferredVideoEnhancementInfo', callback?: AsyncCallback<DeferredVideoEnhancementInfo>): void--><!--Device-VideoOutput-off(type: 'deferredVideoEnhancementInfo', callback?: AsyncCallback<DeferredVideoEnhancementInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deferredVideoEnhancementInfo' | Yes | Event type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DeferredVideoEnhancementInfo](arkts-camera-camera-deferredvideoenhancementinfo-i-sys.md)&gt; | No | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## onDeferredVideoEnhancementInfo

```TypeScript
onDeferredVideoEnhancementInfo(callback: AsyncCallback<DeferredVideoEnhancementInfo>): void
```

Subscribes deferred video enhancement info callback.

**Since:** 23

<!--Device-VideoOutput-onDeferredVideoEnhancementInfo(callback: AsyncCallback<DeferredVideoEnhancementInfo>): void--><!--Device-VideoOutput-onDeferredVideoEnhancementInfo(callback: AsyncCallback<DeferredVideoEnhancementInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DeferredVideoEnhancementInfo](arkts-camera-camera-deferredvideoenhancementinfo-i-sys.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## on_deferredVideoEnhancementInfo('deferredVideoEnhancementInfo')

```TypeScript
on(type: 'deferredVideoEnhancementInfo', callback: AsyncCallback<DeferredVideoEnhancementInfo>): void
```

Subscribes deferred video enhancement info callback.

**Since:** 13

<!--Device-VideoOutput-on(type: 'deferredVideoEnhancementInfo', callback: AsyncCallback<DeferredVideoEnhancementInfo>): void--><!--Device-VideoOutput-on(type: 'deferredVideoEnhancementInfo', callback: AsyncCallback<DeferredVideoEnhancementInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deferredVideoEnhancementInfo' | Yes | Event type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DeferredVideoEnhancementInfo](arkts-camera-camera-deferredvideoenhancementinfo-i-sys.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## setRotation

```TypeScript
setRotation(rotation: ImageRotation): void
```

Set a video rotation.

**Since:** 23

<!--Device-VideoOutput-setRotation(rotation: ImageRotation): void--><!--Device-VideoOutput-setRotation(rotation: ImageRotation): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rotation | [ImageRotation](arkts-camera-camera-imagerotation-e.md) | Yes | The rotation angle. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

