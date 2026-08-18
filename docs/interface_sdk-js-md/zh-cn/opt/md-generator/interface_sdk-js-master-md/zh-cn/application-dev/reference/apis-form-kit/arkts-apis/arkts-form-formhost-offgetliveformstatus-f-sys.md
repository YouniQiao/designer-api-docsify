# offGetLiveFormStatus（系统接口）

## 导入模块

```TypeScript
```

## offGetLiveFormStatus

```TypeScript
function offGetLiveFormStatus(callback?: formInfo.GetLiveFormStatusCallback): void
```

Cancels Listening to the event of get live form status.

**起始版本：** 23

<!--Device-formHost-function offGetLiveFormStatus(callback?: formInfo.GetLiveFormStatusCallback): void--><!--Device-formHost-function offGetLiveFormStatus(callback?: formInfo.GetLiveFormStatusCallback): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | formInfo.GetLiveFormStatusCallback | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
