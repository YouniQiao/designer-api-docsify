# MetadataOutput

metadata流。继承[CameraOutput](arkts-camera-camera-cameraoutput-i.md)。

**继承/实现关系：** MetadataOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md)

**起始版本：** 10

<!--Device-camera-interface MetadataOutput extends CameraOutput--><!--Device-camera-interface MetadataOutput extends CameraOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## addMetadataObjectTypes

```TypeScript
addMetadataObjectTypes(types: Array<MetadataObjectType>): void
```

新增需要上报的检测对象类型。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-addMetadataObjectTypes(types: Array<MetadataObjectType>): void--><!--Device-MetadataOutput-addMetadataObjectTypes(types: Array<MetadataObjectType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;MetadataObjectType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isLockMetadataObjectTrackingSupported

```TypeScript
isLockMetadataObjectTrackingSupported(): boolean
```

检查设备是否支持锁定元数据对象（如猫脸、狗脸）追踪功能。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-isLockMetadataObjectTrackingSupported(): boolean--><!--Device-MetadataOutput-isLockMetadataObjectTrackingSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## lockMetadataObjectTracking

```TypeScript
lockMetadataObjectTracking(point: Point): void
```

锁定对特定元数据对象（如猫脸、狗脸）的追踪。

> **说明：**
> 
> - 该功能以point所指向的点所在的对象为追踪对象，如果该点不存在追踪对象，则功能不生效。
> 
> - 被锁定追踪的对象离开取景范围超过三秒或调用解锁追踪后，锁定追踪自动取消。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-lockMetadataObjectTracking(point: Point): void--><!--Device-MetadataOutput-lockMetadataObjectTracking(point: Point): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## off('metadataObjectsAvailable')

```TypeScript
off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void
```

注销监听检测到的metadata对象。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'metadataObjectsAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;MetadataObject&gt;&gt; | 否 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听metadata流的错误。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-MetadataOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## on('metadataObjectsAvailable')

```TypeScript
on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void
```

监听检测到的metadata对象，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'metadataObjectsAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;MetadataObject&gt;&gt; | 是 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听metadata流的错误，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-MetadataOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## removeMetadataObjectTypes

```TypeScript
removeMetadataObjectTypes(types: Array<MetadataObjectType>): void
```

删除需要上报的检测对象类型。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-removeMetadataObjectTypes(types: Array<MetadataObjectType>): void--><!--Device-MetadataOutput-removeMetadataObjectTypes(types: Array<MetadataObjectType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;MetadataObjectType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

开始输出metadata，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-start(callback: AsyncCallback<void>): void--><!--Device-MetadataOutput-start(callback: AsyncCallback<void>): void-End-->

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

开始输出metadata。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-start(): Promise<void>--><!--Device-MetadataOutput-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止输出metadata，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-stop(callback: AsyncCallback<void>): void--><!--Device-MetadataOutput-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## stop

```TypeScript
stop(): Promise<void>
```

停止输出metadata。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-stop(): Promise<void>--><!--Device-MetadataOutput-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## unlockMetadataObjectTracking

```TypeScript
unlockMetadataObjectTracking(): void
```

解锁元数据对象（如猫脸、狗脸）追踪。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-unlockMetadataObjectTracking(): void--><!--Device-MetadataOutput-unlockMetadataObjectTracking(): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
