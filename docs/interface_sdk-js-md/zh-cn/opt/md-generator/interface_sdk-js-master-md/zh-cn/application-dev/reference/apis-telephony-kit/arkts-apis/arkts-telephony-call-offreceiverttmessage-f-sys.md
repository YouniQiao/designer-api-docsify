# offReceiveRttMessage（系统接口）

## offReceiveRttMessage

```TypeScript
function offReceiveRttMessage(callback?: Callback<RttMessageInfo>): void
```

去订阅rtt消息事件

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function offReceiveRttMessage(callback?: Callback<RttMessageInfo>): void--><!--Device-call-function offReceiveRttMessage(callback?: Callback<RttMessageInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RttMessageInfo](arkts-telephony-call-rttmessageinfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
