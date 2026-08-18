# offFoldStatusChange

## 导入模块

```TypeScript
```

## offFoldStatusChange

```TypeScript
function offFoldStatusChange(callback?: Callback<FoldStatus>): void
```

Unregister the callback for fold status changes.

**起始版本：** 23

<!--Device-display-function offFoldStatusChange(callback?: Callback<FoldStatus>): void--><!--Device-display-function offFoldStatusChange(callback?: Callback<FoldStatus>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldStatus&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
