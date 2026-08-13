# offSwipeInward（系统接口）

## offSwipeInward

```TypeScript
function offSwipeInward(receiver?: Callback<SwipeInward>): void
```

取消监听向内滑动事件。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function offSwipeInward(receiver?: Callback<SwipeInward>): void--><!--Device-inputMonitor-function offSwipeInward(receiver?: Callback<SwipeInward>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SwipeInward](arkts-input-multimodalinput-gestureevent-swipeinward-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
