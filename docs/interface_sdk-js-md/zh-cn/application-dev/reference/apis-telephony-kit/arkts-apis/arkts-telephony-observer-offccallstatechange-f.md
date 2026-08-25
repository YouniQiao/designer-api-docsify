# offCCallStateChange

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## offCCallStateChange

```TypeScript
function offCCallStateChange(callback?: Callback<CCallStateInfo>): void
```

取消三方应用监听运营商通话状态并获取通话号码，使用callback方式作为异步方法。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_CALL_FOR_DEVICES

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8800001](../errorcode-telephony.md#8800001-输入参数不在处理范围内) |
| [8800002](../errorcode-telephony.md#8800002-服务连接失败) |
| [8800003](../errorcode-telephony.md#8800003-系统内部错误) |
| [8800999](../errorcode-telephony.md#8800999-内部错误) |
