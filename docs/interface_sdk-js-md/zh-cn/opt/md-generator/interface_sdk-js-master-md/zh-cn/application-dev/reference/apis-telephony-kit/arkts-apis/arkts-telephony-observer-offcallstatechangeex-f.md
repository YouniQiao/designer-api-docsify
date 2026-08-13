# offCallStateChangeEx

## offCallStateChangeEx

```TypeScript
function offCallStateChangeEx(callback?: Callback<TelCallState>): void
```

Cancel callback when the telCall state is updated.

**起始版本：** 23

**废弃版本：** -1

<!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void--><!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [8800999](../errorcode-telephony.md#8800999-内部错误) |
| [8800002](../errorcode-telephony.md#8800002-服务连接失败) |
| [8800003](../errorcode-telephony.md#8800003-系统内部错误) |
| [8800001](../errorcode-telephony.md#8800001-输入参数不在处理范围内) |
