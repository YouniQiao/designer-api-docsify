# CaptureSession

拍照会话类，保存一次相机运行所需要的所有资源[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput)、[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)，并向相机设备申请完成相 机功能(录像，拍照)。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [VideoSession](arkts-camera-camera-videosession-i.md#VideoSession)

<!--Device-camera-interface CaptureSession--><!--Device-camera-interface CaptureSession-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## addInput

```TypeScript
addInput(cameraInput: CameraInput): void
```

把[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput)加入到会话。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [addInput](arkts-camera-camera-session-i.md#addInput)

<!--Device-CaptureSession-addInput(cameraInput: CameraInput): void--><!--Device-CaptureSession-addInput(cameraInput: CameraInput): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cameraInput | [CameraInput](arkts-camera-camera-camerainput-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |

## addOutput

```TypeScript
addOutput(cameraOutput: CameraOutput): void
```

把[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)加入到会话。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [addOutput](arkts-camera-camera-session-i.md#addOutput)

<!--Device-CaptureSession-addOutput(cameraOutput: CameraOutput): void--><!--Device-CaptureSession-addOutput(cameraOutput: CameraOutput): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cameraOutput | [CameraOutput](arkts-camera-camera-cameraoutput-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |

## beginConfig

```TypeScript
beginConfig(): void
```

开始配置会话。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [beginConfig](arkts-camera-camera-session-i.md#beginConfig)

<!--Device-CaptureSession-beginConfig(): void--><!--Device-CaptureSession-beginConfig(): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

| 错误码ID |
| --- |
| [7400105](../errorcode-camera.md#7400105-会话配置被锁定) |

## commitConfig

```TypeScript
commitConfig(callback: AsyncCallback<void>): void
```

提交配置信息，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [commitConfig](arkts-camera-camera-session-i.md#commitConfig)(callback: AsyncCallback&lt;void&gt;)

<!--Device-CaptureSession-commitConfig(callback: AsyncCallback<void>): void--><!--Device-CaptureSession-commitConfig(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## commitConfig

```TypeScript
commitConfig(): Promise<void>
```

提交配置信息。使用Promise异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [commitConfig](arkts-camera-camera-session-i.md#commitConfig)()

<!--Device-CaptureSession-commitConfig(): Promise<void>--><!--Device-CaptureSession-commitConfig(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getActiveVideoStabilizationMode

```TypeScript
getActiveVideoStabilizationMode(): VideoStabilizationMode
```

查询当前正在使用的视频防抖模式。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getActiveVideoStabilizationMode](arkts-camera-camera-stabilization-i.md#getActiveVideoStabilizationMode)

<!--Device-CaptureSession-getActiveVideoStabilizationMode(): VideoStabilizationMode--><!--Device-CaptureSession-getActiveVideoStabilizationMode(): VideoStabilizationMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getExposureBiasRange

```TypeScript
getExposureBiasRange(): Array<number>
```

查询曝光补偿范围。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getExposureBiasRange](arkts-camera-camera-autoexposurequery-i.md#getExposureBiasRange)

<!--Device-CaptureSession-getExposureBiasRange(): Array<number>--><!--Device-CaptureSession-getExposureBiasRange(): Array<number>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getExposureMode

```TypeScript
getExposureMode(): ExposureMode
```

获取当前曝光模式。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getExposureMode](arkts-camera-camera-autoexposure-i.md#getExposureMode)

<!--Device-CaptureSession-getExposureMode(): ExposureMode--><!--Device-CaptureSession-getExposureMode(): ExposureMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [ExposureMode](arkts-camera-camera-exposuremode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getExposureValue

```TypeScript
getExposureValue(): number
```

查询当前的曝光值。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getExposureValue](arkts-camera-camera-autoexposure-i.md#getExposureValue)

<!--Device-CaptureSession-getExposureValue(): number--><!--Device-CaptureSession-getExposureValue(): number-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getFlashMode

```TypeScript
getFlashMode(): FlashMode
```

获取当前设备的闪光灯模式。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getFlashMode](arkts-camera-camera-flash-i.md#getFlashMode)

<!--Device-CaptureSession-getFlashMode(): FlashMode--><!--Device-CaptureSession-getFlashMode(): FlashMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [FlashMode](arkts-camera-camera-flashmode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getFocalLength

```TypeScript
getFocalLength(): number
```

查询焦距值。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getFocalLength](arkts-camera-camera-focus-i.md#getFocalLength)

<!--Device-CaptureSession-getFocalLength(): number--><!--Device-CaptureSession-getFocalLength(): number-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getFocusMode

```TypeScript
getFocusMode(): FocusMode
```

获取当前的对焦模式。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getFocusMode](arkts-camera-camera-focus-i.md#getFocusMode)

<!--Device-CaptureSession-getFocusMode(): FocusMode--><!--Device-CaptureSession-getFocusMode(): FocusMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [FocusMode](arkts-camera-camera-focusmode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getFocusPoint

```TypeScript
getFocusPoint(): Point
```

查询焦点。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getFocusPoint](arkts-camera-camera-focus-i.md#getFocusPoint)

<!--Device-CaptureSession-getFocusPoint(): Point--><!--Device-CaptureSession-getFocusPoint(): Point-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getMeteringPoint

```TypeScript
getMeteringPoint(): Point
```

查询曝光区域中心点。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getMeteringPoint](arkts-camera-camera-autoexposure-i.md#getMeteringPoint)

<!--Device-CaptureSession-getMeteringPoint(): Point--><!--Device-CaptureSession-getMeteringPoint(): Point-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getZoomRatio

```TypeScript
getZoomRatio(): number
```

获取当前的变焦比。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getZoomRatio](arkts-camera-camera-zoom-i.md#getZoomRatio)

<!--Device-CaptureSession-getZoomRatio(): number--><!--Device-CaptureSession-getZoomRatio(): number-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getZoomRatioRange

```TypeScript
getZoomRatioRange(): Array<number>
```

获取支持的变焦范围。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getZoomRatioRange](arkts-camera-camera-zoomquery-i.md#getZoomRatioRange)

<!--Device-CaptureSession-getZoomRatioRange(): Array<number>--><!--Device-CaptureSession-getZoomRatioRange(): Array<number>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## hasFlash

```TypeScript
hasFlash(): boolean
```

检测是否有闪光灯。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [hasFlash](arkts-camera-camera-flashquery-i.md#hasFlash)

<!--Device-CaptureSession-hasFlash(): boolean--><!--Device-CaptureSession-hasFlash(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## isExposureModeSupported

```TypeScript
isExposureModeSupported(aeMode: ExposureMode): boolean
```

查询曝光模式是否支持。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [isExposureModeSupported](arkts-camera-camera-autoexposurequery-i.md#isExposureModeSupported)

<!--Device-CaptureSession-isExposureModeSupported(aeMode: ExposureMode): boolean--><!--Device-CaptureSession-isExposureModeSupported(aeMode: ExposureMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aeMode | [ExposureMode](arkts-camera-camera-exposuremode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## isFlashModeSupported

```TypeScript
isFlashModeSupported(flashMode: FlashMode): boolean
```

检测闪光灯模式是否支持。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [isFlashModeSupported](arkts-camera-camera-flashquery-i.md#isFlashModeSupported)

<!--Device-CaptureSession-isFlashModeSupported(flashMode: FlashMode): boolean--><!--Device-CaptureSession-isFlashModeSupported(flashMode: FlashMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flashMode | [FlashMode](arkts-camera-camera-flashmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## isFocusModeSupported

```TypeScript
isFocusModeSupported(afMode: FocusMode): boolean
```

查询对焦模式是否支持。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [isFocusModeSupported](arkts-camera-camera-focusquery-i.md#isFocusModeSupported)

<!--Device-CaptureSession-isFocusModeSupported(afMode: FocusMode): boolean--><!--Device-CaptureSession-isFocusModeSupported(afMode: FocusMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| afMode | [FocusMode](arkts-camera-camera-focusmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## isVideoStabilizationModeSupported

```TypeScript
isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean
```

查询是否支持指定的视频防抖模式。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [isVideoStabilizationModeSupported](arkts-camera-camera-stabilizationquery-i.md#isVideoStabilizationModeSupported)

<!--Device-CaptureSession-isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean--><!--Device-CaptureSession-isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| vsMode | [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## off_error

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听拍照会话的错误事件，通过注册回调函数获取结果。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [off](arkts-camera-camera-videosession-i.md#off_error)(type: 'error', callback?: ErrorCallback)

<!--Device-CaptureSession-off(type: 'error', callback?: ErrorCallback): void--><!--Device-CaptureSession-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## off_focusStateChange

```TypeScript
off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void
```

注销监听相机聚焦的状态变化。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [off](arkts-camera-camera-videosession-i.md#off_error)(type: 'focusStateChange', callback?: AsyncCallback&lt;FocusState&gt;)

<!--Device-CaptureSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void--><!--Device-CaptureSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusStateChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 否 |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听拍照会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。 > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [on](arkts-camera-camera-videosession-i.md#on_error)(type: 'error', callback: ErrorCallback)

<!--Device-CaptureSession-on(type: 'error', callback: ErrorCallback): void--><!--Device-CaptureSession-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## on_focusStateChange

```TypeScript
on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void
```

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。 > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [on](arkts-camera-camera-videosession-i.md#on_error)(type: 'focusStateChange', callback: AsyncCallback&lt;FocusState&gt;)

<!--Device-CaptureSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void--><!--Device-CaptureSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusStateChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 是 |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放会话资源，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [release](arkts-camera-camera-session-i.md#release)(callback: AsyncCallback&lt;void&gt;)

<!--Device-CaptureSession-release(callback: AsyncCallback<void>): void--><!--Device-CaptureSession-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## release

```TypeScript
release(): Promise<void>
```

释放会话资源。使用Promise异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [release](arkts-camera-camera-session-i.md#release)()

<!--Device-CaptureSession-release(): Promise<void>--><!--Device-CaptureSession-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## removeInput

```TypeScript
removeInput(cameraInput: CameraInput): void
```

移除[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput)。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [removeInput](arkts-camera-camera-session-i.md#removeInput)

<!--Device-CaptureSession-removeInput(cameraInput: CameraInput): void--><!--Device-CaptureSession-removeInput(cameraInput: CameraInput): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cameraInput | [CameraInput](arkts-camera-camera-camerainput-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |

## removeOutput

```TypeScript
removeOutput(cameraOutput: CameraOutput): void
```

从会话中移除[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [removeOutput](arkts-camera-camera-session-i.md#removeOutput)

<!--Device-CaptureSession-removeOutput(cameraOutput: CameraOutput): void--><!--Device-CaptureSession-removeOutput(cameraOutput: CameraOutput): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cameraOutput | [CameraOutput](arkts-camera-camera-cameraoutput-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |

## setExposureBias

```TypeScript
setExposureBias(exposureBias: number): void
```

设置曝光补偿，曝光补偿值（EV）。 进行设置之前，建议先通过方法[getExposureBiasRange](#getExposureBiasRange)查询支持的范围。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setExposureBias](arkts-camera-camera-autoexposure-i.md#setExposureBias)

<!--Device-CaptureSession-setExposureBias(exposureBias: number): void--><!--Device-CaptureSession-setExposureBias(exposureBias: number): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exposureBias | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setExposureMode

```TypeScript
setExposureMode(aeMode: ExposureMode): void
```

设置曝光模式。进行设置之前，需要先检查设备是否支持指定的曝光模式，可使用方法 [isExposureModeSupported](#isExposureModeSupported)。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setExposureMode](arkts-camera-camera-autoexposure-i.md#setExposureMode)

<!--Device-CaptureSession-setExposureMode(aeMode: ExposureMode): void--><!--Device-CaptureSession-setExposureMode(aeMode: ExposureMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aeMode | [ExposureMode](arkts-camera-camera-exposuremode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setFlashMode

```TypeScript
setFlashMode(flashMode: FlashMode): void
```

设置闪光灯模式。 进行设置之前，需要先检查： 1. 设备是否支持闪光灯，可使用方法[hasFlash](#hasFlash)。 2. 设备是否支持指定的闪光灯模式，可使用方法[isFlashModeSupported](#isFlashModeSupported)。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setFlashMode](arkts-camera-camera-flash-i.md#setFlashMode)

<!--Device-CaptureSession-setFlashMode(flashMode: FlashMode): void--><!--Device-CaptureSession-setFlashMode(flashMode: FlashMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flashMode | [FlashMode](arkts-camera-camera-flashmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setFocusMode

```TypeScript
setFocusMode(afMode: FocusMode): void
```

设置对焦模式。 进行设置之前，需要先检查设备是否支持指定的焦距模式，可使用方法[isFocusModeSupported](#isFocusModeSupported)。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setFocusMode](arkts-camera-camera-focus-i.md#setFocusMode)

<!--Device-CaptureSession-setFocusMode(afMode: FocusMode): void--><!--Device-CaptureSession-setFocusMode(afMode: FocusMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| afMode | [FocusMode](arkts-camera-camera-focusmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setFocusPoint

```TypeScript
setFocusPoint(point: Point): void
```

设置焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。 此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setFocusPoint](arkts-camera-camera-focus-i.md#setFocusPoint)

<!--Device-CaptureSession-setFocusPoint(point: Point): void--><!--Device-CaptureSession-setFocusPoint(point: Point): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setMeteringPoint

```TypeScript
setMeteringPoint(point: Point): void
```

设置曝光区域中心点，曝光点应位于0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。 此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setMeteringPoint](arkts-camera-camera-autoexposure-i.md#setMeteringPoint)

<!--Device-CaptureSession-setMeteringPoint(point: Point): void--><!--Device-CaptureSession-setMeteringPoint(point: Point): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setVideoStabilizationMode

```TypeScript
setVideoStabilizationMode(mode: VideoStabilizationMode): void
```

设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过 [isVideoStabilizationModeSupported](#isVideoStabilizationModeSupported)方法判断所设置的模式是否支持。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setVideoStabilizationMode](arkts-camera-camera-stabilization-i.md#setVideoStabilizationMode)

<!--Device-CaptureSession-setVideoStabilizationMode(mode: VideoStabilizationMode): void--><!--Device-CaptureSession-setVideoStabilizationMode(mode: VideoStabilizationMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setZoomRatio

```TypeScript
setZoomRatio(zoomRatio: number): void
```

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setZoomRatio](arkts-camera-camera-zoom-i.md#setZoomRatio)

<!--Device-CaptureSession-setZoomRatio(zoomRatio: number): void--><!--Device-CaptureSession-setZoomRatio(zoomRatio: number): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [zoomRatio](arkts-camera-camera-zoompointinfo-i-sys.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

开始会话工作，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [start](arkts-camera-camera-session-i.md#start)(callback: AsyncCallback&lt;void&gt;)

<!--Device-CaptureSession-start(callback: AsyncCallback<void>): void--><!--Device-CaptureSession-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## start

```TypeScript
start(): Promise<void>
```

开始会话工作。使用Promise异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [start](arkts-camera-camera-session-i.md#start)()

<!--Device-CaptureSession-start(): Promise<void>--><!--Device-CaptureSession-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止会话工作，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [stop](arkts-camera-camera-session-i.md#stop)(callback: AsyncCallback&lt;void&gt;)

<!--Device-CaptureSession-stop(callback: AsyncCallback<void>): void--><!--Device-CaptureSession-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## stop

```TypeScript
stop(): Promise<void>
```

停止会话工作。使用Promise异步回调。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [stop](arkts-camera-camera-session-i.md#stop)()

<!--Device-CaptureSession-stop(): Promise<void>--><!--Device-CaptureSession-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
