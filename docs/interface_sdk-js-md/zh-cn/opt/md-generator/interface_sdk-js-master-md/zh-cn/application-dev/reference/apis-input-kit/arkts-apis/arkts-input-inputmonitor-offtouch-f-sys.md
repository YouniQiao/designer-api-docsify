# offTouch（系统接口）

## offTouch

```TypeScript
function offTouch(receiver?: TouchEventReceiver): void
```

取消监听全局触屏事件。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function offTouch(receiver?: TouchEventReceiver): void--><!--Device-inputMonitor-function offTouch(receiver?: TouchEventReceiver): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| receiver | [TouchEventReceiver](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
