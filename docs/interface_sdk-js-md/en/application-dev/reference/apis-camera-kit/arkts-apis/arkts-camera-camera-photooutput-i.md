# PhotoOutput

拍照会话中使用的输出信息，继承[CameraOutput](arkts-camera-camera-cameraoutput-i.md)。

**Inheritance/Implementation:** PhotoOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface PhotoOutput extends CameraOutput--><!--Device-camera-interface PhotoOutput extends CameraOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## capture

```TypeScript
capture(callback: AsyncCallback<void>): void
```

以默认设置触发一次拍照，通过注册回调函数获取结果。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-capture(callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-capture(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当以默认设置触发拍照成功，err为undefined，否则为错误对象。错误码类型 [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md)。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

## capture

```TypeScript
capture(): Promise<void>
```

以默认设置触发一次拍照。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-capture(): Promise<void>--><!--Device-PhotoOutput-capture(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

## capture

```TypeScript
capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void
```

以指定参数触发一次拍照，通过注册回调函数获取结果。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) | Yes | 拍照设置，传入undefined类型数据按默认设置触发一次拍照处理。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，用于获取结果。接口调用失败会返回相应错误码，错误码类型 [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md)。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

## capture

```TypeScript
capture(setting: PhotoCaptureSetting): Promise<void>
```

以指定参数触发一次拍照。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting): Promise<void>--><!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) | Yes | 拍照设置，传入undefined类型数据按默认设置触发一次拍照处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

## enableAutoExtendedGainmapDelivery

```TypeScript
enableAutoExtendedGainmapDelivery(enabled: boolean): void
```

是否启用自动扩展增益图（Gainmap）的输出。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PhotoOutput-enableAutoExtendedGainmapDelivery(enabled: boolean): void--><!--Device-PhotoOutput-enableAutoExtendedGainmapDelivery(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 是否启用自动扩展增益图（Gainmap）的输出。true表示启用，false表示不启用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config, only throw in session usage. |
| 7400201 | Camera service fatal error. |

## enableMirror

```TypeScript
enableMirror(enabled: boolean): void
```

是否启用动态照片镜像拍照。

调用该接口前，需要通过[isMovingPhotoSupported](arkts-camera-camera-photooutput-i.md#ismovingphotosupported)查询是否支持动态照片拍摄功能以及通过  
[isMirrorSupported](arkts-camera-camera-photooutput-i.md#ismirrorsupported)查询是否支持镜像拍照功能。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-enableMirror(enabled: boolean): void--><!--Device-PhotoOutput-enableMirror(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 是否启用动态照片镜像拍照。true为开启动态照片镜像拍照，false为关闭动态照片镜像拍照。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

## enableMovingPhoto

```TypeScript
enableMovingPhoto(enabled: boolean): void
```

使能动态照片拍照。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MICROPHONE

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-enableMovingPhoto(enabled: boolean): void--><!--Device-PhotoOutput-enableMovingPhoto(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 使能动态照片拍照。true为开启动态照片，false为关闭动态照片。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 201 | permission denied. |
| 7400201 | Camera service fatal error. |

## getActiveProfile

```TypeScript
getActiveProfile(): Profile
```

获取当前生效的配置信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-getActiveProfile(): Profile--><!--Device-PhotoOutput-getActiveProfile(): Profile-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Profile](arkts-camera-camera-profile-i.md) | 当前生效的配置信息 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error. |

## getPhotoRotation

ArkTS-Dyn:
```TypeScript
getPhotoRotation(deviceDegree?: number): ImageRotation
```

ArkTS-Sta:
```TypeScript
getPhotoRotation(deviceDegree?: int): ImageRotation
```

获取拍照旋转角度。

- 设备自然方向：设备默认使用方向。例如，直板机默认使用方向为竖屏（充电口向下）。  
- 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度。例如，直板机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-getPhotoRotation(deviceDegree?: int): ImageRotation--><!--Device-PhotoOutput-getPhotoRotation(deviceDegree?: int): ImageRotation-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceDegree | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 设备旋转角度，单位度，取值范围：[0, 360]。 &lt;br&gt;若入参超过该范围，则取入参除以360的余数。 &lt;br&gt;从API version 23开始，入参deviceDegree为可选参数，当不传入参数时，由系统获取deviceDegree进行拍照旋转角度计算。<br>**Since:** 23 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageRotation](arkts-camera-camera-imagerotation-e.md) | 返回拍照旋转角度。若接口调用失败，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 22 |
| 7400201 | Camera service fatal error. |

## getSupportedMovingPhotoVideoCodecTypes

```TypeScript
getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>
```

查询支持的动态照片短视频编码类型。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>--><!--Device-PhotoOutput-getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;VideoCodecType&gt; | 支持的动态照片短视频编码类型列表。若接口调用失败，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error. |

## isAutoExtendedGainmapDeliverySupported

```TypeScript
isAutoExtendedGainmapDeliverySupported(): boolean
```

确认是否支持自动扩展增益图（Gainmap）的输出。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PhotoOutput-isAutoExtendedGainmapDeliverySupported(): boolean--><!--Device-PhotoOutput-isAutoExtendedGainmapDeliverySupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持自动扩展增益图（Gainmap）的输出。true表示支持，false表示不支持。 |

## isMirrorSupported

```TypeScript
isMirrorSupported(): boolean
```

查询是否支持镜像拍照。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-isMirrorSupported(): boolean--><!--Device-PhotoOutput-isMirrorSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回是否支持镜像拍照，true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

## isMovingPhotoSupported

```TypeScript
isMovingPhotoSupported(): boolean
```

查询是否支持动态照片拍摄。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-isMovingPhotoSupported(): boolean--><!--Device-PhotoOutput-isMovingPhotoSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回是否支持动态照片拍照。true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error. |

## isPhotoQualityPrioritizationSupported

```TypeScript
isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean
```

检查是否支持指定的拍照画质优先策略。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PhotoOutput-isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean--><!--Device-PhotoOutput-isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](arkts-camera-camera-photoqualityprioritization-e.md) | Yes | 要检查的拍照画质优先策略。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持指定的拍照画质优先策略。true表示支持，false表示不支持。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

## off('photoAvailable')

```TypeScript
off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void
```

注销监听拍照返回照片上报事件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'photoAvailable' | Yes | 监听事件，固定为'photoAvailable'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Photo&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('photoAssetAvailable')

```TypeScript
off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

注销photoAsset上报。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'photoAssetAvailable' | Yes | 监听事件，固定为'photoAssetAvailable'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | No | 需要解监听的回调方法。如果callback不为空且与此对应的监听方法一致，不为匿名方法，则解注 册该方法；如果callback为空，则解监听所有回调。 |

## off('captureStart')

```TypeScript
off(type: 'captureStart', callback?: AsyncCallback<number>): void
```

注销拍照开始的监听。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

**Substitutes:** camera.PhotoOutput.off(type:

<!--Device-PhotoOutput-off(type: 'captureStart', callback?: AsyncCallback<number>): void--><!--Device-PhotoOutput-off(type: 'captureStart', callback?: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureStart' | Yes | 监听事件，固定为'captureStart'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('captureStartWithInfo')

```TypeScript
off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void
```

注销监听拍照。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureStartWithInfo' | Yes | 监听事件，固定为'captureStartWithInfo'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CaptureStartInfo&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('frameShutter')

```TypeScript
off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void
```

注销监听拍照帧输出捕获。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameShutter' | Yes | 监听事件，固定为'frameShutter'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FrameShutterInfo&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('frameShutterEnd')

```TypeScript
off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void
```

注销监听拍照曝光结束捕获。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameShutterEnd' | Yes | 监听事件，固定为'frameShutterEnd'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FrameShutterEndInfo&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有 callback。 |

## off('captureEnd')

```TypeScript
off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void
```

注销监听拍照结束。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureEnd' | Yes | 监听事件，固定为'captureEnd'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CaptureEndInfo&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('captureReady')

```TypeScript
off(type: 'captureReady', callback?: AsyncCallback<void>): void
```

注销监听可拍下一张。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'captureReady', callback?: AsyncCallback<void>): void--><!--Device-PhotoOutput-off(type: 'captureReady', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureReady' | Yes | 监听事件，固定为'captureReady'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('estimatedCaptureDuration')

```TypeScript
off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<double>): void
```

注销监听预估的拍照时间。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<double>): void--><!--Device-PhotoOutput-off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'estimatedCaptureDuration' | Yes | 监听事件，固定为'estimatedCaptureDuration'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听拍照输出发生错误。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-PhotoOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | 监听事件，固定为'error'，photoOutput创建成功后可监听。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## offCaptureEnd

```TypeScript
offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void
```

Unsubscribes from capture end event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CaptureEndInfo&gt; | No | Callback used to get the capture end information. |

## offCapturePhotoAvailable

```TypeScript
offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void
```

注销监听全质量图和未压缩图。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoOutput-offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void--><!--Device-PhotoOutput-offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CapturePhoto&gt; | No | 回调函数，如果指定参数则取消对应callback，callback对象不可是匿名函数，否则取消所有callback。 |

## offCaptureReady

```TypeScript
offCaptureReady(callback?: AsyncCallback<void>): void
```

Unsubscribes from capture ready event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-offCaptureStartWithInfo(callback?: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-offCaptureStartWithInfo(callback?: AsyncCallback<CaptureStartInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CaptureStartInfo&gt; | No | Callback used to get the capture start info. |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-offFrameShutter(callback?: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-offFrameShutter(callback?: AsyncCallback<FrameShutterInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FrameShutterInfo&gt; | No | Callback used to get the frame shutter information. |

## offFrameShutterEnd

```TypeScript
offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void
```

Unsubscribes from frame shutter end event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FrameShutterEndInfo&gt; | No | Callback used to get the frame shutter end information. |

## offPhotoAssetAvailable

```TypeScript
offPhotoAssetAvailable(callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

Unsubscribes photo asset event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-offPhotoAvailable(callback?: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-offPhotoAvailable(callback?: AsyncCallback<Photo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Photo&gt; | No | Callback used to get the Photo. |

## on('photoAvailable')

```TypeScript
on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void
```

注册监听拍照返回照片上报事件。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'photoAvailable' | Yes | 监听事件，固定为'photoAvailable'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Photo&gt; | Yes | 回调函数，用于监听拍照返回照片上报事件。 |

## on('photoAssetAvailable')

```TypeScript
on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

注册监听photoAsset上报。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'photoAssetAvailable' | Yes | 监听事件，固定为'photoAssetAvailable'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | Yes | 回调函数，用于监听photoAsset上报。 |

## on('captureStart')

```TypeScript
on(type: 'captureStart', callback: AsyncCallback<number>): void
```

监听拍照开始，通过注册回调函数获取Capture ID。使用callback异步回调。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

**Substitutes:** camera.PhotoOutput.on(type:

<!--Device-PhotoOutput-on(type: 'captureStart', callback: AsyncCallback<number>): void--><!--Device-PhotoOutput-on(type: 'captureStart', callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureStart' | Yes | 监听事件，固定为'captureStart'，photoOutput创建成功后可监听。每次拍照，底层开始曝光时触发该事件并返回。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 使用callback的方式获取Capture ID。 |

## on('captureStartWithInfo')

```TypeScript
on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void
```

监听拍照开始，通过注册回调函数获取[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureStartWithInfo' | Yes | 监听事件，固定为'captureStartWithInfo'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CaptureStartInfo&gt; | Yes | 使用callback的方式获取Capture ID。 |

## on('frameShutter')

```TypeScript
on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void
```

监听拍照帧输出捕获，通过注册回调函数获取结果。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameShutter' | Yes | 监听事件，固定为'frameShutter'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FrameShutterInfo&gt; | Yes | 回调函数，用于获取相关信息。该回调返回意味着可以再次下发拍照请求。 |

## on('frameShutterEnd')

```TypeScript
on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void
```

监听拍照曝光结束捕获，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frameShutterEnd' | Yes | 监听事件，固定为'frameShutterEnd'，photoOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FrameShutterEndInfo&gt; | Yes | 回调函数，用于获取相关信息。该回调返回表示拍照曝光结束。 |

## on('captureEnd')

```TypeScript
on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void
```

监听拍照结束，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureEnd' | Yes | 监听事件，固定为'captureEnd'。photoOutput创建成功后可监听。拍照完全结束可触发该事件发生并返回相应信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CaptureEndInfo&gt; | Yes | 回调函数，用于获取相关信息。 |

## on('captureReady')

```TypeScript
on(type: 'captureReady', callback: AsyncCallback<void>): void
```

监听可拍下一张，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'captureReady', callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-on(type: 'captureReady', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'captureReady' | Yes | 监听事件，固定为'captureReady'，photoOutput创建成功后可监听。当下一张可拍时可触发该事件发生并返回相应信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，用于获取相关信息。 |

## on('estimatedCaptureDuration')

```TypeScript
on(type: 'estimatedCaptureDuration', callback: AsyncCallback<double>): void
```

监听预估的拍照时间，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'estimatedCaptureDuration', callback: AsyncCallback<double>): void--><!--Device-PhotoOutput-on(type: 'estimatedCaptureDuration', callback: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'estimatedCaptureDuration' | Yes | 监听事件，固定为'estimatedCaptureDuration'，photoOutput创建成功后可监听。拍照完全结束可触发该事件发 生并返回相应信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | Yes | 回调函数，用于获取预估的单次拍照底层出sensor采集帧时间，单位：毫秒。如果上报-1，代表没有预估时间。 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听拍照输出发生错误，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-PhotoOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | 监听事件，固定为'error'，photoOutput创建成功后可监听。拍照接口调用时出现错误触发该事件并返回错误信息。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md)。 |

## onCaptureEnd

```TypeScript
onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void
```

Subscribes capture end event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CaptureEndInfo&gt; | Yes | Callback used to get the capture end information. |

## onCapturePhotoAvailable

```TypeScript
onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void
```

注册监听全质量图和未压缩图。使用callback异步回调。

> **说明：**
> 
> - 注册监听接口时，不支持在该接口监听的回调方法里调用
> [offCapturePhotoAvailable](camera.PhotoOutput.offCapturePhotoAvailable(callback?: Callback&lt;CapturePhoto&gt;))
> 注销回调。
> 
> - 拍摄未压缩图（YUV）格式图片时，仅支持使用此接口注册监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoOutput-onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void--><!--Device-PhotoOutput-onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CapturePhoto&gt; | Yes | 回调函数，用于监听全质量图和未压缩图上报事件。 |

## onCaptureReady

```TypeScript
onCaptureReady(callback: AsyncCallback<void>): void
```

Subscribes capture ready event callback. After receiving the callback, can proceed to the next capture

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-onCaptureStartWithInfo(callback: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-onCaptureStartWithInfo(callback: AsyncCallback<CaptureStartInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CaptureStartInfo&gt; | Yes | Callback used to get the capture start info. |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-onFrameShutter(callback: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-onFrameShutter(callback: AsyncCallback<FrameShutterInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FrameShutterInfo&gt; | Yes | Callback used to get the frame shutter information. |

## onFrameShutterEnd

```TypeScript
onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void
```

Subscribes frame shutter end event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FrameShutterEndInfo&gt; | Yes | Callback used to get the frame shutter end information. |

## onPhotoAssetAvailable

```TypeScript
onPhotoAssetAvailable(callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

Subscribes to photo asset event callback.

This API processes deferred photo delivery data by quickly displaying low-quality images to give users the impression of faster photo capture, while also generating high-quality images to maintain the final output quality. For details about the design specifications, see  
[Optimizing Deferred Photo Delivery](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-camera-shot2see).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoOutput-onPhotoAvailable(callback: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-onPhotoAvailable(callback: AsyncCallback<Photo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Photo&gt; | Yes | Callback used to get the Photo. |

## setMovingPhotoVideoCodecType

```TypeScript
setMovingPhotoVideoCodecType(codecType: VideoCodecType): void
```

设置动态照片短视频编码类型。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoOutput-setMovingPhotoVideoCodecType(codecType: VideoCodecType): void--><!--Device-PhotoOutput-setMovingPhotoVideoCodecType(codecType: VideoCodecType): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| codecType | [VideoCodecType](arkts-camera-camera-videocodectype-e.md) | Yes | 动态照片短视频编码类型。 &lt;br&gt;如果设置不在枚举范围内，则该参数不会生效。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error. |

## setPhotoQualityPrioritization

```TypeScript
setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void
```

设置拍照画质优先策略。

设置之前，可先使用方法  
[isPhotoQualityPrioritizationSupported](arkts-camera-camera-photooutput-i.md#isphotoqualityprioritizationsupported)对设备是否支持指定的拍照画质优先策略进行检查。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PhotoOutput-setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void--><!--Device-PhotoOutput-setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](arkts-camera-camera-photoqualityprioritization-e.md) | Yes | 要设置的拍照画质优先策略。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

