# onRttErrCause（系统接口）

## onRttErrCause

```TypeScript
function onRttErrCause(callback: Callback<RttErrorInfo>): void
```

订阅rtt通话错误事件

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function onRttErrCause(callback: Callback<RttErrorInfo>): void--><!--Device-call-function onRttErrCause(callback: Callback<RttErrorInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RttErrorInfo](arkts-telephony-call-rtterrorinfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
