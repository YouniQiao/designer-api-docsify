# SecureSession

SecureSession继承自[Session](arkts-camera-camera-session-i.md#Session)、[Flash](arkts-camera-camera-flash-i.md#Flash)、  
[AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure)、[WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance)、[Focus](arkts-camera-camera-focus-i.md#Focus)、  
[Zoom](arkts-camera-camera-zoom-i.md#Zoom)。

安全模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦的操作。

通过[createSession](arkts-camera-camera-cameramanager-i.md#createSession)接口传入[SceneMode](arkts-camera-camera-scenemode-e.md#SceneMode)为SECURE_PHOTO模式创建一个安全模式的会话。该模式开放给人脸识别、银行等有安全诉求的应用，需要结合&lt;!--RP1--&gt;安全TA&lt;!--RP1End--&gt;使用，支持同时输出普通预览流和安全流的业务场景。&lt;!--RP2--&gt;

安全TA：可用于图片处理，它具备验证服务器下发数据的验签能力、图片签名、解析及组装tlv逻辑的能力，还具备密钥读取、创建及操作能力。&lt;!--RP2End--&gt;

**继承/实现关系：** SecureSession extends [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash), [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance), [Focus](arkts-camera-camera-focus-i.md#Focus), [Zoom](arkts-camera-camera-zoom-i.md#Zoom)

**起始版本：** 12

<!--Device-camera-interface SecureSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom--><!--Device-camera-interface SecureSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## addSecureOutput

```TypeScript
addSecureOutput(previewOutput: PreviewOutput): void
```

将其中一条[PreviewOutput](arkts-camera-camera-previewoutput-i.md#PreviewOutput)标记成安全输出。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-SecureSession-addSecureOutput(previewOutput: PreviewOutput): void--><!--Device-SecureSession-addSecureOutput(previewOutput: PreviewOutput): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| previewOutput | [PreviewOutput](arkts-camera-camera-previewoutput-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-无效入参) |
| [7400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-非法操作) |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听安全相机会话的错误事件，通过注册回调函数获取结果。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-SecureSession-off(type: 'error', callback?: ErrorCallback): void--><!--Device-SecureSession-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## off('focusStateChange')

```TypeScript
off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void
```

注销监听相机聚焦的状态变化。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-SecureSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void--><!--Device-SecureSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusStateChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 否 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听安全相机会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-SecureSession-on(type: 'error', callback: ErrorCallback): void--><!--Device-SecureSession-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## on('focusStateChange')

```TypeScript
on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void
```

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 12

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-SecureSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void--><!--Device-SecureSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusStateChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 是 |
