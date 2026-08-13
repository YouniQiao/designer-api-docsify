# onImsCallModeChange（系统接口）

## onImsCallModeChange

```TypeScript
function onImsCallModeChange(callback: Callback<ImsCallModeInfo>): void
```

Subscribe to the imsCallModeChange event.

**起始版本：** 26.1.0

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function onImsCallModeChange(callback: Callback<ImsCallModeInfo>): void--><!--Device-call-function onImsCallModeChange(callback: Callback<ImsCallModeInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ImsCallModeInfo](arkts-telephony-call-imscallmodeinfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
