# offFormUninstall（系统接口）

## 导入模块

```TypeScript
```

## offFormUninstall

```TypeScript
function offFormUninstall(callback?: Callback<string>): void
```

Cancels listening to the event of uninstall form. You can use this method to cancel listening to the event of uninstall form.

**起始版本：** 23

<!--Device-formHost-function offFormUninstall(callback?: Callback<string>): void--><!--Device-formHost-function offFormUninstall(callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
