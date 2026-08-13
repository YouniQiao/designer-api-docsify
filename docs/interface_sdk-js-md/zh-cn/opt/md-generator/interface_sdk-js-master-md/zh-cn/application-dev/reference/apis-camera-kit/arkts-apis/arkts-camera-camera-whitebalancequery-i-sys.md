# WhiteBalanceQuery（系统接口）

提供了查询设备对指定的白平衡模式是否支持，以及获取设备支持的白平衡模式范围的方法。

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface WhiteBalanceQuery--><!--Device-camera-interface WhiteBalanceQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getWhiteBalanceRange

```TypeScript
getWhiteBalanceRange(): Array<number>
```

获取手动白平衡模式下，白平衡值的范围。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-WhiteBalanceQuery-getWhiteBalanceRange(): Array<int>--><!--Device-WhiteBalanceQuery-getWhiteBalanceRange(): Array<int>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isWhiteBalanceGainsSupported

```TypeScript
isWhiteBalanceGainsSupported(): boolean
```

Checks whether the RGB gain is supported.

**起始版本：** 26.1.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WhiteBalanceQuery-isWhiteBalanceGainsSupported(): boolean--><!--Device-WhiteBalanceQuery-isWhiteBalanceGainsSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isWhiteBalanceModeSupported

```TypeScript
isWhiteBalanceModeSupported(mode: WhiteBalanceMode): boolean
```

检测是否支持当前传入的白平衡模式。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-WhiteBalanceQuery-isWhiteBalanceModeSupported(mode: WhiteBalanceMode): boolean--><!--Device-WhiteBalanceQuery-isWhiteBalanceModeSupported(mode: WhiteBalanceMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WhiteBalanceMode](arkts-camera-camera-whitebalancemode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
