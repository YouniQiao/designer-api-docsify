# moveBySpeed（系统接口）

## moveBySpeed

```TypeScript
function moveBySpeed(mechId: number, params: SpeedParams, duration: number): Promise<Result>
```

以特定速度移动一个具身设备

**起始版本：** 26.0.0

**废弃版本：** -1

<!--Device-mechanicManager-function moveBySpeed(mechId: int, params: SpeedParams, duration: int): Promise<Result>--><!--Device-mechanicManager-function moveBySpeed(mechId: int, params: SpeedParams, duration: int): Promise<Result>-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mechId | number | 是 |
| params | [SpeedParams](arkts-mechanic-mechanicmanager-speedparams-i-sys.md) | 是 |
| duration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../errorcode-mechanic.md#33300002-设备未连接) |
| [33300003](../errorcode-mechanic.md#33300003-功能不支持) |
