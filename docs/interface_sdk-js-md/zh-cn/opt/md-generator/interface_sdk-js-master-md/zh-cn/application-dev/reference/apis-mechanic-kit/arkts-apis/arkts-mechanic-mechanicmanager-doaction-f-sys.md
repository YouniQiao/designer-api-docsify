# doAction（系统接口）

## doAction

```TypeScript
function doAction(mechId: number, actionType: ActionType): Promise<Result>
```

执行一个动作序列

**起始版本：** 26.0.0

**废弃版本：** -1

<!--Device-mechanicManager-function doAction(mechId: int, actionType: ActionType): Promise<Result>--><!--Device-mechanicManager-function doAction(mechId: int, actionType: ActionType): Promise<Result>-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mechId | number | 是 |
| actionType | [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md) | 是 |

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
