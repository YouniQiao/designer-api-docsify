# PhotoOutput

拍照会话中使用的输出信息，继承[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)。

**继承/实现关系：** PhotoOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface PhotoOutput--><!--Device-camera-interface PhotoOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## capture

```TypeScript
capture(callback: AsyncCallback<void>): void
```

以默认设置触发一次拍照，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-capture(callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-capture(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-会话未运行) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## capture

```TypeScript
capture(): Promise<void>
```

以默认设置触发一次拍照。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-capture(): Promise<void>--><!--Device-PhotoOutput-capture(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-会话未运行) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## capture

```TypeScript
capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void
```

以指定参数触发一次拍照，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400104](../errorcode-camera.md#7400104-会话未运行) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## capture

```TypeScript
capture(setting: PhotoCaptureSetting): Promise<void>
```

以指定参数触发一次拍照。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting): Promise<void>--><!--Device-PhotoOutput-capture(setting: PhotoCaptureSetting): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400104](../errorcode-camera.md#7400104-会话未运行) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## enableAutoExtendedGainmapDelivery

```TypeScript
enableAutoExtendedGainmapDelivery(enabled: boolean): void
```

是否启用自动扩展增益图（Gainmap）的输出。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-enableAutoExtendedGainmapDelivery(enabled: boolean): void--><!--Device-PhotoOutput-enableAutoExtendedGainmapDelivery(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## enableMirror

```TypeScript
enableMirror(enabled: boolean): void
```

是否启用动态照片镜像拍照。 调用该接口前，需要通过[isMovingPhotoSupported](#isMovingPhotoSupported)查询是否支持动态照片拍摄功能以及通过 [isMirrorSupported](#isMirrorSupported)查询是否支持镜像拍照功能。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-enableMirror(enabled: boolean): void--><!--Device-PhotoOutput-enableMirror(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## enableMovingPhoto

```TypeScript
enableMovingPhoto(enabled: boolean): void
```

使能动态照片拍照。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MICROPHONE

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-enableMovingPhoto(enabled: boolean): void--><!--Device-PhotoOutput-enableMovingPhoto(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getActiveProfile

```TypeScript
getActiveProfile(): Profile
```

获取当前生效的配置信息。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-getActiveProfile(): Profile--><!--Device-PhotoOutput-getActiveProfile(): Profile-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [Profile](arkts-camera-camera-profile-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getPhotoRotation

```TypeScript
getPhotoRotation(deviceDegree?: number): ImageRotation
```

获取拍照旋转角度。 - 设备自然方向：设备默认使用方向。例如，直板机默认使用方向为竖屏（充电口向下）。 - 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度。例如，直板机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-getPhotoRotation(deviceDegree?: int): ImageRotation--><!--Device-PhotoOutput-getPhotoRotation(deviceDegree?: int): ImageRotation-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDegree | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageRotation](arkts-camera-camera-imagerotation-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getSupportedMovingPhotoVideoCodecTypes

```TypeScript
getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>
```

查询支持的动态照片短视频编码类型。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>--><!--Device-PhotoOutput-getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;[VideoCodecType](arkts-camera-camera-videocodectype-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## isAutoExtendedGainmapDeliverySupported

```TypeScript
isAutoExtendedGainmapDeliverySupported(): boolean
```

确认是否支持自动扩展增益图（Gainmap）的输出。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-isAutoExtendedGainmapDeliverySupported(): boolean--><!--Device-PhotoOutput-isAutoExtendedGainmapDeliverySupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isMirrorSupported

```TypeScript
isMirrorSupported(): boolean
```

查询是否支持镜像拍照。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-isMirrorSupported(): boolean--><!--Device-PhotoOutput-isMirrorSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isMovingPhotoSupported

```TypeScript
isMovingPhotoSupported(): boolean
```

查询是否支持动态照片拍摄。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-isMovingPhotoSupported(): boolean--><!--Device-PhotoOutput-isMovingPhotoSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## isPhotoQualityPrioritizationSupported

```TypeScript
isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean
```

检查是否支持指定的拍照画质优先策略。

**起始版本：** 24

**废弃版本：** -1

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean--><!--Device-PhotoOutput-isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](arkts-camera-camera-photoqualityprioritization-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## offCaptureEnd

```TypeScript
offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void
```

Unsubscribes from capture end event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-offCaptureEnd(callback?: AsyncCallback<CaptureEndInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md)&gt; | 否 |

## offCapturePhotoAvailable

```TypeScript
offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void
```

注销监听全质量图和未压缩图。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void--><!--Device-PhotoOutput-offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CapturePhoto](arkts-camera-camera-capturephoto-i.md)&gt; | 否 |

## offCaptureReady

```TypeScript
offCaptureReady(callback?: AsyncCallback<void>): void
```

Unsubscribes from capture ready event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offCaptureReady(callback?: AsyncCallback<void>): void--><!--Device-PhotoOutput-offCaptureReady(callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## offCaptureStartWithInfo

```TypeScript
offCaptureStartWithInfo(callback?: AsyncCallback<CaptureStartInfo>): void
```

Unsubscribes from capture start event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offCaptureStartWithInfo(callback?: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-offCaptureStartWithInfo(callback?: AsyncCallback<CaptureStartInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)&gt; | 否 |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offError(callback?: ErrorCallback): void--><!--Device-PhotoOutput-offError(callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## offEstimatedCaptureDuration

```TypeScript
offEstimatedCaptureDuration(callback?: AsyncCallback<number>): void
```

Unsubscribes from estimated capture duration event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offEstimatedCaptureDuration(callback?: AsyncCallback<double>): void--><!--Device-PhotoOutput-offEstimatedCaptureDuration(callback?: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 否 |

## offFrameShutter

```TypeScript
offFrameShutter(callback?: AsyncCallback<FrameShutterInfo>): void
```

Unsubscribes from frame shutter event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offFrameShutter(callback?: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-offFrameShutter(callback?: AsyncCallback<FrameShutterInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md)&gt; | 否 |

## offFrameShutterEnd

```TypeScript
offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void
```

Unsubscribes from frame shutter end event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-offFrameShutterEnd(callback?: AsyncCallback<FrameShutterEndInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md)&gt; | 否 |

## offPhotoAssetAvailable

```TypeScript
offPhotoAssetAvailable(callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

Unsubscribes photo asset event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offPhotoAssetAvailable(callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-offPhotoAssetAvailable(callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | 否 |

## offPhotoAvailable

```TypeScript
offPhotoAvailable(callback?: AsyncCallback<Photo>): void
```

Unsubscribes photo available event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-offPhotoAvailable(callback?: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-offPhotoAvailable(callback?: AsyncCallback<Photo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Photo](arkts-camera-camera-photo-i.md)&gt; | 否 |

## off_captureEnd

```TypeScript
off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void
```

注销监听拍照结束。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureEnd' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md)&gt; | 否 |

## off_captureReady

```TypeScript
off(type: 'captureReady', callback?: AsyncCallback<void>): void
```

注销监听可拍下一张。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'captureReady', callback?: AsyncCallback<void>): void--><!--Device-PhotoOutput-off(type: 'captureReady', callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureReady' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## off_captureStart

```TypeScript
off(type: 'captureStart', callback?: AsyncCallback<number>): void
```

注销拍照开始的监听。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。 > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [off](#off_photoAvailable)(type: 'captureStartWithInfo', callback?: AsyncCallback&lt;CaptureStartInfo&gt;)

<!--Device-PhotoOutput-off(type: 'captureStart', callback?: AsyncCallback<number>): void--><!--Device-PhotoOutput-off(type: 'captureStart', callback?: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureStart' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 否 |

## off_captureStartWithInfo

```TypeScript
off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void
```

注销监听拍照。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureStartWithInfo' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)&gt; | 否 |

## off_error

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听拍照输出发生错误。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-PhotoOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## off_estimatedCaptureDuration

```TypeScript
off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void
```

注销监听预估的拍照时间。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<double>): void--><!--Device-PhotoOutput-off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'estimatedCaptureDuration' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 否 |

## off_frameShutter

```TypeScript
off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void
```

注销监听拍照帧输出捕获。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameShutter' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md)&gt; | 否 |

## off_frameShutterEnd

```TypeScript
off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void
```

注销监听拍照曝光结束捕获。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameShutterEnd' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md)&gt; | 否 |

## off_photoAssetAvailable

```TypeScript
off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

注销photoAsset上报。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAssetAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | 否 |

## off_photoAvailable

```TypeScript
off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void
```

注销监听拍照返回照片上报事件。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Photo](arkts-camera-camera-photo-i.md)&gt; | 否 |

## onCaptureEnd

```TypeScript
onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void
```

Subscribes capture end event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-onCaptureEnd(callback: AsyncCallback<CaptureEndInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md)&gt; | 是 |

## onCapturePhotoAvailable

```TypeScript
onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void
```

注册监听全质量图和未压缩图。使用callback异步回调。 > **说明：** > > - 注册监听接口时，不支持在该接口监听的回调方法里调用 > [offCapturePhotoAvailable](#offCapturePhotoAvailable) > 注销回调。 > > - 拍摄未压缩图（YUV）格式图片时，仅支持使用此接口注册监听。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void--><!--Device-PhotoOutput-onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CapturePhoto](arkts-camera-camera-capturephoto-i.md)&gt; | 是 |

## onCaptureReady

```TypeScript
onCaptureReady(callback: AsyncCallback<void>): void
```

Subscribes capture ready event callback. After receiving the callback, can proceed to the next capture

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onCaptureReady(callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-onCaptureReady(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## onCaptureStartWithInfo

```TypeScript
onCaptureStartWithInfo(callback: AsyncCallback<CaptureStartInfo>): void
```

Subscribes capture start event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onCaptureStartWithInfo(callback: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-onCaptureStartWithInfo(callback: AsyncCallback<CaptureStartInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)&gt; | 是 |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onError(callback: ErrorCallback): void--><!--Device-PhotoOutput-onError(callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## onEstimatedCaptureDuration

```TypeScript
onEstimatedCaptureDuration(callback: AsyncCallback<number>): void
```

Subscribes estimated capture duration event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onEstimatedCaptureDuration(callback: AsyncCallback<double>): void--><!--Device-PhotoOutput-onEstimatedCaptureDuration(callback: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## onFrameShutter

```TypeScript
onFrameShutter(callback: AsyncCallback<FrameShutterInfo>): void
```

Subscribes frame shutter event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onFrameShutter(callback: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-onFrameShutter(callback: AsyncCallback<FrameShutterInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md)&gt; | 是 |

## onFrameShutterEnd

```TypeScript
onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void
```

Subscribes frame shutter end event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-onFrameShutterEnd(callback: AsyncCallback<FrameShutterEndInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md)&gt; | 是 |

## onPhotoAssetAvailable

```TypeScript
onPhotoAssetAvailable(callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

Subscribes to photo asset event callback. This API processes deferred photo delivery data by quickly displaying low-quality images to give users the impression of faster photo capture, while also generating high-quality images to maintain the final output quality. For details about the design specifications, see [Optimizing Deferred Photo Delivery](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-camera-shot2see).

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onPhotoAssetAvailable(callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-onPhotoAssetAvailable(callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | 是 |

## onPhotoAvailable

```TypeScript
onPhotoAvailable(callback: AsyncCallback<Photo>): void
```

Subscribes photo available event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoOutput-onPhotoAvailable(callback: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-onPhotoAvailable(callback: AsyncCallback<Photo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Photo](arkts-camera-camera-photo-i.md)&gt; | 是 |

## on_captureEnd

```TypeScript
on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void
```

监听拍照结束，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void--><!--Device-PhotoOutput-on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureEnd' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md)&gt; | 是 |

## on_captureReady

```TypeScript
on(type: 'captureReady', callback: AsyncCallback<void>): void
```

监听可拍下一张，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'captureReady', callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-on(type: 'captureReady', callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureReady' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## on_captureStart

```TypeScript
on(type: 'captureStart', callback: AsyncCallback<number>): void
```

监听拍照开始，通过注册回调函数获取Capture ID。使用callback异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。 > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [on](#on_photoAvailable)(type: 'captureStartWithInfo', callback: AsyncCallback&lt;CaptureStartInfo&gt;)

<!--Device-PhotoOutput-on(type: 'captureStart', callback: AsyncCallback<number>): void--><!--Device-PhotoOutput-on(type: 'captureStart', callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureStart' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## on_captureStartWithInfo

```TypeScript
on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void
```

监听拍照开始，通过注册回调函数获取[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md#CaptureStartInfo)。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void--><!--Device-PhotoOutput-on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureStartWithInfo' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md)&gt; | 是 |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听拍照输出发生错误，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-PhotoOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## on_estimatedCaptureDuration

```TypeScript
on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void
```

监听预估的拍照时间，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'estimatedCaptureDuration', callback: AsyncCallback<double>): void--><!--Device-PhotoOutput-on(type: 'estimatedCaptureDuration', callback: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'estimatedCaptureDuration' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## on_frameShutter

```TypeScript
on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void
```

监听拍照帧输出捕获，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void--><!--Device-PhotoOutput-on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameShutter' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md)&gt; | 是 |

## on_frameShutterEnd

```TypeScript
on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void
```

监听拍照曝光结束捕获，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void--><!--Device-PhotoOutput-on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameShutterEnd' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md)&gt; | 是 |

## on_photoAssetAvailable

```TypeScript
on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void
```

注册监听photoAsset上报。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void--><!--Device-PhotoOutput-on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAssetAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | 是 |

## on_photoAvailable

```TypeScript
on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void
```

注册监听拍照返回照片上报事件。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void--><!--Device-PhotoOutput-on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Photo](arkts-camera-camera-photo-i.md)&gt; | 是 |

## setMovingPhotoVideoCodecType

```TypeScript
setMovingPhotoVideoCodecType(codecType: VideoCodecType): void
```

设置动态照片短视频编码类型。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-setMovingPhotoVideoCodecType(codecType: VideoCodecType): void--><!--Device-PhotoOutput-setMovingPhotoVideoCodecType(codecType: VideoCodecType): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| codecType | [VideoCodecType](arkts-camera-camera-videocodectype-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## setPhotoQualityPrioritization

```TypeScript
setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void
```

设置拍照画质优先策略。 设置之前，可先使用方法 [isPhotoQualityPrioritizationSupported](#isPhotoQualityPrioritizationSupported)对设备是否支持指定的 拍照画质优先策略进行检查。

**起始版本：** 24

**废弃版本：** -1

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoOutput-setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void--><!--Device-PhotoOutput-setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](arkts-camera-camera-photoqualityprioritization-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
