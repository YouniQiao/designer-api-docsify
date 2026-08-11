# getDialogSessionInfo（系统接口）

## getDialogSessionInfo

```TypeScript
function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo
```

通过dialogSessionId获取会话信息。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dialogSession-function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo--><!--Device-dialogSession-function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dialogSessionId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DialogSessionInfo](arkts-ability-dialogsession-dialogsessioninfo-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
