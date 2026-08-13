# Session

会话类，保存一次相机运行所需要的所有资源[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput)、[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)，并向相机设备申请完成相机功 能（录像，拍照）。

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface Session--><!--Device-camera-interface Session-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## addInput

```TypeScript
addInput(cameraInput: CameraInput): void
```

把[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput)加入到会话。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-addInput(cameraInput: CameraInput): void--><!--Device-Session-addInput(cameraInput: CameraInput): void-End-->

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
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## addOutput

```TypeScript
addOutput(cameraOutput: CameraOutput): void
```

把[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)加入到会话。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-addOutput(cameraOutput: CameraOutput): void--><!--Device-Session-addOutput(cameraOutput: CameraOutput): void-End-->

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
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## beginConfig

```TypeScript
beginConfig(): void
```

开始配置会话。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-beginConfig(): void--><!--Device-Session-beginConfig(): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

| 错误码ID |
| --- |
| [7400105](../errorcode-camera.md#7400105-会话配置被锁定) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## canAddInput

```TypeScript
canAddInput(cameraInput: CameraInput): boolean
```

判断当前cameraInput是否可以添加到session中。当前函数需要在[beginConfig](#beginConfig)和 [commitConfig](#commitConfig)之间生效。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-canAddInput(cameraInput: CameraInput): boolean--><!--Device-Session-canAddInput(cameraInput: CameraInput): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cameraInput | [CameraInput](arkts-camera-camera-camerainput-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## canAddOutput

```TypeScript
canAddOutput(cameraOutput: CameraOutput): boolean
```

判断当前cameraOutput是否可以添加到session中。当前函数需要在[addInput](#addInput)和 [commitConfig](#commitConfig)之间生效。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-canAddOutput(cameraOutput: CameraOutput): boolean--><!--Device-Session-canAddOutput(cameraOutput: CameraOutput): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cameraOutput | [CameraOutput](arkts-camera-camera-cameraoutput-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## commitConfig

```TypeScript
commitConfig(callback: AsyncCallback<void>): void
```

提交配置信息，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-commitConfig(callback: AsyncCallback<void>): void--><!--Device-Session-commitConfig(callback: AsyncCallback<void>): void-End-->

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

提交配置信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-commitConfig(): Promise<void>--><!--Device-Session-commitConfig(): Promise<void>-End-->

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

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放会话资源，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-release(callback: AsyncCallback<void>): void--><!--Device-Session-release(callback: AsyncCallback<void>): void-End-->

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

释放会话资源。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-release(): Promise<void>--><!--Device-Session-release(): Promise<void>-End-->

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

移除[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput)。当前函数需要在[beginConfig](#beginConfig)和 [commitConfig](#commitConfig)之间生效。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-removeInput(cameraInput: CameraInput): void--><!--Device-Session-removeInput(cameraInput: CameraInput): void-End-->

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
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## removeOutput

```TypeScript
removeOutput(cameraOutput: CameraOutput): void
```

从会话中移除[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-removeOutput(cameraOutput: CameraOutput): void--><!--Device-Session-removeOutput(cameraOutput: CameraOutput): void-End-->

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
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

开始会话工作，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-start(callback: AsyncCallback<void>): void--><!--Device-Session-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## start

```TypeScript
start(): Promise<void>
```

开始会话工作。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-start(): Promise<void>--><!--Device-Session-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止会话工作，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-stop(callback: AsyncCallback<void>): void--><!--Device-Session-stop(callback: AsyncCallback<void>): void-End-->

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

停止会话工作。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Session-stop(): Promise<void>--><!--Device-Session-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
