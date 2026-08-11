# PreviewOutput

预览输出类。继承[CameraOutput](arkts-camera-camera-cameraoutput-i.md)。

**继承/实现关系：** PreviewOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md)

**起始版本：** 10

<!--Device-camera-interface PreviewOutput extends CameraOutput--><!--Device-camera-interface PreviewOutput extends CameraOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## addDeferredSurface

```TypeScript
addDeferredSurface(surfaceId: string): void
```

配置延迟预览的Surface，可以在[commitConfig](arkts-camera-camera-session-i.md#commitconfig)配流和[start](arkts-camera-camera-session-i.md#start)启流之后运行。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-addDeferredSurface(surfaceId: string): void--><!--Device-PreviewOutput-addDeferredSurface(surfaceId: string): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## enableBandwidthCompression

```TypeScript
enableBandwidthCompression(enabled: boolean): void
```

使能预览带宽压缩。

使能之前，可先使用方法[isBandwidthCompressionSupported](arkts-camera-camera-previewoutput-i.md#isbandwidthcompressionsupported)对设备是否支持预览带宽压缩进行检查。

> **说明：**
> 
> 该接口只能在使用[Session.commitConfig](arkts-camera-camera-session-i.md#commitconfig)接口之前调用，否则会影响预览流
> 出流格式。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-enableBandwidthCompression(enabled: boolean): void--><!--Device-PreviewOutput-enableBandwidthCompression(enabled: boolean): void-End-->

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

## getActiveFrameRate

```TypeScript
getActiveFrameRate(): FrameRateRange
```

获取已设置的帧率范围。

使用[setFrameRate](arkts-camera-camera-previewoutput-i.md#setframerate)接口对预览流设置过帧率后可查询。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-getActiveFrameRate(): FrameRateRange--><!--Device-PreviewOutput-getActiveFrameRate(): FrameRateRange-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [FrameRateRange](arkts-camera-camera-frameraterange-i.md) |

## getActiveProfile

```TypeScript
getActiveProfile(): Profile
```

获取当前生效的配置信息。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-getActiveProfile(): Profile--><!--Device-PreviewOutput-getActiveProfile(): Profile-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [Profile](arkts-camera-camera-profile-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getPreviewRotation

```TypeScript
getPreviewRotation(displayRotation?: number): ImageRotation
```

获取预览旋转角度。

- 设备自然方向：设备默认使用方向。例如，直板机默认使用方向为竖屏（充电口向下）。  
- 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度。例如，直板机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。  
-   
[屏幕旋转角度](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-direction#section737072712182)：显示设备的屏幕顺时针旋转角度。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-getPreviewRotation(displayRotation?: int): ImageRotation--><!--Device-PreviewOutput-getPreviewRotation(displayRotation?: int): ImageRotation-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayRotation | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageRotation](arkts-camera-camera-imagerotation-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getSupportedFrameRates

```TypeScript
getSupportedFrameRates(): Array<FrameRateRange>
```

查询支持的帧率范围。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-getSupportedFrameRates(): Array<FrameRateRange>--><!--Device-PreviewOutput-getSupportedFrameRates(): Array<FrameRateRange>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;FrameRateRange&gt; |

## isBandwidthCompressionSupported

```TypeScript
isBandwidthCompressionSupported(): boolean
```

检查是否支持预览带宽压缩（指通过编码减少数据量，降低其在传输链路中的带宽占用）。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-isBandwidthCompressionSupported(): boolean--><!--Device-PreviewOutput-isBandwidthCompressionSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isLogViewAssistSupported

```TypeScript
isLogViewAssistSupported(): boolean
```

LOG视频下，查询是否支持辅助监看功能。辅助监看开启后，预览画面还原至原色域，录制出的视频仍然是LOG视频格式。

> **说明：**
> 
> 辅助监看效果仅支持1080P及以下分辨率。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-isLogViewAssistSupported(): boolean--><!--Device-PreviewOutput-isLogViewAssistSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## off('frameStart')

```TypeScript
off(type: 'frameStart', callback?: AsyncCallback<void>): void
```

注销预览帧启动的监听。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-off(type: 'frameStart', callback?: AsyncCallback<void>): void--><!--Device-PreviewOutput-off(type: 'frameStart', callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameStart' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## off('frameEnd')

```TypeScript
off(type: 'frameEnd', callback?: AsyncCallback<void>): void
```

注销监听预览帧结束。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-off(type: 'frameEnd', callback?: AsyncCallback<void>): void--><!--Device-PreviewOutput-off(type: 'frameEnd', callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameEnd' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听预览输出的错误事件。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-PreviewOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## on('frameStart')

```TypeScript
on(type: 'frameStart', callback: AsyncCallback<void>): void
```

监听预览帧启动，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-on(type: 'frameStart', callback: AsyncCallback<void>): void--><!--Device-PreviewOutput-on(type: 'frameStart', callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameStart' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## on('frameEnd')

```TypeScript
on(type: 'frameEnd', callback: AsyncCallback<void>): void
```

监听预览帧结束，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-on(type: 'frameEnd', callback: AsyncCallback<void>): void--><!--Device-PreviewOutput-on(type: 'frameEnd', callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameEnd' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听预览输出的错误事件，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-PreviewOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## setFrameRate

```TypeScript
setFrameRate(minFps: number, maxFps: number): void
```

设置预览流帧率范围，设置的范围必须在支持的帧率范围内。

进行设置前，可通过[getSupportedFrameRates](arkts-camera-camera-previewoutput-i.md#getsupportedframerates)接口查询支持的帧率范围。

> **说明：**
> 
> 仅在[PhotoSession](arkts-camera-camera-photosession-i.md)或[VideoSession](arkts-camera-camera-videosession-i.md)模式下支持。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-setFrameRate(minFps: int, maxFps: int): void--><!--Device-PreviewOutput-setFrameRate(minFps: int, maxFps: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| minFps | number | 是 |
| maxFps | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400110](../errorcode-camera.md#7400110-与当前配置存在冲突) |

## setLogViewAssistEnable

```TypeScript
setLogViewAssistEnable(enable: boolean): void
```

LOG视频下，使能辅助监看之前，可先使用方法[isLogViewAssistSupported](arkts-camera-camera-previewoutput-i.md#islogviewassistsupported)查询设备是否支持预览辅助监看。

> **说明：**
> 
> - 该接口只能在使用[Session.commitConfig](arkts-camera-camera-session-i.md#commitconfig)接口之后调用。
> 
> - 预览辅助监看效果仅支持1080P及以下分辨率。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-setLogViewAssistEnable(enable: boolean): void--><!--Device-PreviewOutput-setLogViewAssistEnable(enable: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## setPreviewRotation

```TypeScript
setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void
```

设置预览旋转角度。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PreviewOutput-setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void--><!--Device-PreviewOutput-setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| previewRotation | [ImageRotation](arkts-camera-camera-imagerotation-e.md) | 是 |
| isDisplayLocked | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

开始输出预览流，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [camera.Session.start](arkts-camera-camera-session-i.md#start)(callback:

<!--Device-PreviewOutput-start(callback: AsyncCallback<void>): void--><!--Device-PreviewOutput-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## start

```TypeScript
start(): Promise<void>
```

开始输出预览流。使用Promise异步回调。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [camera.Session.start](arkts-camera-camera-session-i.md#start)()

<!--Device-PreviewOutput-start(): Promise<void>--><!--Device-PreviewOutput-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止输出预览流，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [camera.Session.stop](arkts-camera-camera-session-i.md#stop)(callback:

<!--Device-PreviewOutput-stop(callback: AsyncCallback<void>): void--><!--Device-PreviewOutput-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## stop

```TypeScript
stop(): Promise<void>
```

停止输出预览流。使用Promise异步回调。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [camera.Session.stop](arkts-camera-camera-session-i.md#stop)()

<!--Device-PreviewOutput-stop(): Promise<void>--><!--Device-PreviewOutput-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |
