# onKeyPressed（系统接口）

## onKeyPressed

```TypeScript
function onKeyPressed(keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void
```

监听指定按键的按下抬起事件，支持监听META_LEFT键、META_RIGHT键、电源键、音量键。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onKeyPressed(keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void--><!--Device-inputMonitor-function onKeyPressed(keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keys | Array&lt;[KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)&gt; | 是 |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4100001](../errorcode-inputmonitor.md#4100001-按键不支持前置监听) |
