# Session

会话类，保存一次相机运行所需要的所有资源[CameraInput](arkts-camera-camera-camerainput-i.md)、[CameraOutput](arkts-camera-camera-cameraoutput-i.md)，并向相机设备申请完成相机功能（录像，拍照）。

**起始版本：** 11

<!--Device-camera-interface Session--><!--Device-camera-interface Session-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getActiveParameter

```TypeScript
getActiveParameter(key: string): string
```

Gets the active value of the given key in camera metadata.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Session-getActiveParameter(key: string): string--><!--Device-Session-getActiveParameter(key: string): string-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getCameraOutputCapabilities

```TypeScript
getCameraOutputCapabilities(camera: CameraDevice): Array<CameraOutputCapability>
```

Get the supported camera output capability set.

**起始版本：** 13

<!--Device-Session-getCameraOutputCapabilities(camera: CameraDevice): Array<CameraOutputCapability>--><!--Device-Session-getCameraOutputCapabilities(camera: CameraDevice): Array<CameraOutputCapability>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| camera | [CameraDevice](arkts-camera-camera-cameradevice-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;CameraOutputCapability&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getParameters

```TypeScript
getParameters(key: string): Array<string>
```

Gets the values of the given key in camera metadata.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Session-getParameters(key: string): Array<string>--><!--Device-Session-getParameters(key: string): Array<string>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSupportedKeys

```TypeScript
getSupportedKeys(): Array<string>
```

Gets the supported keys in camera metadata.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Session-getSupportedKeys(): Array<string>--><!--Device-Session-getSupportedKeys(): Array<string>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setParameters

```TypeScript
setParameters(kvpairs: Record<string, string>): void
```

Sets key-value pairs parameters for the session.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Session-setParameters(kvpairs: Record<string, string>): void--><!--Device-Session-setParameters(kvpairs: Record<string, string>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| kvpairs | Record&lt;string, string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setUsage

```TypeScript
setUsage(usage: UsageType, enabled: boolean): void
```

Set usage for the capture session.

**起始版本：** 13

<!--Device-Session-setUsage(usage: UsageType, enabled: boolean): void--><!--Device-Session-setUsage(usage: UsageType, enabled: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| usage | [UsageType](arkts-camera-camera-usagetype-e-sys.md) | 是 |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
