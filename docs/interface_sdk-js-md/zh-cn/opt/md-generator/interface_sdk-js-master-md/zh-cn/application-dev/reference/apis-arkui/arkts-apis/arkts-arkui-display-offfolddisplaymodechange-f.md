# offFoldDisplayModeChange

## offFoldDisplayModeChange

```TypeScript
function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void
```

Unregister the callback for fold display mode changes.

**起始版本：** 23

**废弃版本：** -1

<!--Device-display-function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void--><!--Device-display-function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
