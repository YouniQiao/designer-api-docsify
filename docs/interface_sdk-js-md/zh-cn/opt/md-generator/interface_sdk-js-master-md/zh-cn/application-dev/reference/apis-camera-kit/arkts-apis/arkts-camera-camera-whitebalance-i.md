# WhiteBalance

WhiteBalance继承自[WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md)。

提供了处理设备白平衡的相关功能，包括获取和设置白平衡模式以及白平衡值。

**继承/实现关系：** WhiteBalance extends [WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md)

**起始版本：** 20

<!--Device-camera-interface WhiteBalance extends WhiteBalanceQuery--><!--Device-camera-interface WhiteBalance extends WhiteBalanceQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getColorTint

```TypeScript
getColorTint(): number
```

获取当前白平衡的色调调节值。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-WhiteBalance-getColorTint(): int--><!--Device-WhiteBalance-getColorTint(): int-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getWhiteBalance

```TypeScript
getWhiteBalance(): number
```

获取当前手动白平衡的值。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-WhiteBalance-getWhiteBalance(): int--><!--Device-WhiteBalance-getWhiteBalance(): int-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getWhiteBalanceGains

```TypeScript
getWhiteBalanceGains(): WhiteBalanceGains
```

Gets RGB white balance gain values.

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WhiteBalance-getWhiteBalanceGains(): WhiteBalanceGains--><!--Device-WhiteBalance-getWhiteBalanceGains(): WhiteBalanceGains-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [WhiteBalanceGains](arkts-camera-camera-whitebalancegains-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getWhiteBalanceMode

```TypeScript
getWhiteBalanceMode(): WhiteBalanceMode
```

获取当前白平衡模式。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-WhiteBalance-getWhiteBalanceMode(): WhiteBalanceMode--><!--Device-WhiteBalance-getWhiteBalanceMode(): WhiteBalanceMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [WhiteBalanceMode](arkts-camera-camera-whitebalancemode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setColorTint

```TypeScript
setColorTint(colorTint: number): void
```

设置白平衡的色调调节值。

设置之前需要先检查设备支持配置的白平衡色调调节范围，具体方法请参考[getColorTintRange](arkts-camera-camera-whitebalancequery-i.md#getcolortintrange)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-WhiteBalance-setColorTint(colorTint: int): void--><!--Device-WhiteBalance-setColorTint(colorTint: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorTint | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setWhiteBalance

```TypeScript
setWhiteBalance(whiteBalance: number): void
```

设置手动白平衡值。

设置之前需要先检查设备支持的白平衡值范围，具体方法请参考[getWhiteBalanceRange](arkts-camera-camera-whitebalancequery-i.md#getwhitebalancerange)。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-WhiteBalance-setWhiteBalance(whiteBalance: int): void--><!--Device-WhiteBalance-setWhiteBalance(whiteBalance: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| whiteBalance | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setWhiteBalanceGains

```TypeScript
setWhiteBalanceGains(gains: WhiteBalanceGains): void
```

Sets RGB white balance gain values.

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WhiteBalance-setWhiteBalanceGains(gains: WhiteBalanceGains): void--><!--Device-WhiteBalance-setWhiteBalanceGains(gains: WhiteBalanceGains): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gains | [WhiteBalanceGains](arkts-camera-camera-whitebalancegains-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setWhiteBalanceMode

```TypeScript
setWhiteBalanceMode(mode: WhiteBalanceMode): void
```

设置白平衡模式。设置之前需要先检查设备是否支持指定的白平衡模式，具体方法请参考  
[isWhiteBalanceModeSupported](arkts-camera-camera-whitebalancequery-i.md#iswhitebalancemodesupported)。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-WhiteBalance-setWhiteBalanceMode(mode: WhiteBalanceMode): void--><!--Device-WhiteBalance-setWhiteBalanceMode(mode: WhiteBalanceMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WhiteBalanceMode](arkts-camera-camera-whitebalancemode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
