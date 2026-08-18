# offGetFormRect（系统接口）

## 导入模块

```TypeScript
```

## offGetFormRect

```TypeScript
function offGetFormRect(callback?: formInfo.GetFormRectInfoCallback): void
```

Cancels listening to the event of get form rect. You can use this method to cancel listening to the event of get form rect.

**起始版本：** 23

<!--Device-formHost-function offGetFormRect(callback?: formInfo.GetFormRectInfoCallback): void--><!--Device-formHost-function offGetFormRect(callback?: formInfo.GetFormRectInfoCallback): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | formInfo.GetFormRectInfoCallback | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
