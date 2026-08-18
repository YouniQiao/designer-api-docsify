# ControlCenterSession（系统接口）

Control center session object.

**继承/实现关系：** ControlCenterSession extends [Beauty](arkts-camera-camera-beauty-i-sys.md#beauty系统接口), [Aperture](arkts-camera-camera-aperture-i-sys.md#aperture系统接口), [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md#coloreffect系统接口)

**起始版本：** 23

<!--Device-camera-interface ControlCenterSession--><!--Device-camera-interface ControlCenterSession-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## enableAutoFraming

```TypeScript
enableAutoFraming(enabled: boolean): void
```

Enable auto-framing effect.

**起始版本：** 24

<!--Device-ControlCenterSession-enableAutoFraming(enabled: boolean): void--><!--Device-ControlCenterSession-enableAutoFraming(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-会话未运行) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getAutoFramingStatus

```TypeScript
getAutoFramingStatus(): boolean
```

Gets the status of auto-framing effect.

**起始版本：** 24

<!--Device-ControlCenterSession-getAutoFramingStatus(): boolean--><!--Device-ControlCenterSession-getAutoFramingStatus(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getControlCenterHeight

```TypeScript
getControlCenterHeight(): number
```

Gets the control center height.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ControlCenterSession-getControlCenterHeight(): double--><!--Device-ControlCenterSession-getControlCenterHeight(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getCurrentDevice

```TypeScript
getCurrentDevice(): CameraDevice
```

Gets the current camera device.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ControlCenterSession-getCurrentDevice(): CameraDevice--><!--Device-ControlCenterSession-getCurrentDevice(): CameraDevice-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [CameraDevice](arkts-camera-camera-cameradevice-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-会话未运行) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isAutoFramingSupported

```TypeScript
isAutoFramingSupported(): boolean
```

Checks whether auto-framing is supported.

**起始版本：** 24

<!--Device-ControlCenterSession-isAutoFramingSupported(): boolean--><!--Device-ControlCenterSession-isAutoFramingSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## release

```TypeScript
release(): Promise<void>
```

Release control center session object.

**起始版本：** 23

<!--Device-ControlCenterSession-release(): Promise<void>--><!--Device-ControlCenterSession-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## usedAsPosition

```TypeScript
usedAsPosition(position: CameraPosition): void
```

Sets the camera to be used as a camera at the specified position.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ControlCenterSession-usedAsPosition(position: CameraPosition): void--><!--Device-ControlCenterSession-usedAsPosition(position: CameraPosition): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-会话未运行) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
