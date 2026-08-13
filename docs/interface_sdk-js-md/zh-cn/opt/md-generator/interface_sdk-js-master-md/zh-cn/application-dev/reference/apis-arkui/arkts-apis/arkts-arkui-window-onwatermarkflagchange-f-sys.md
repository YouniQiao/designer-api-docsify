# onWaterMarkFlagChange（系统接口）

## onWaterMarkFlagChange

```TypeScript
function onWaterMarkFlagChange(callback: Callback<boolean>): void
```

添加水印启用状态变化的监听。

**起始版本：** 23

**废弃版本：** -1

<!--Device-window-function onWaterMarkFlagChange(callback: Callback<boolean>): void--><!--Device-window-function onWaterMarkFlagChange(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
