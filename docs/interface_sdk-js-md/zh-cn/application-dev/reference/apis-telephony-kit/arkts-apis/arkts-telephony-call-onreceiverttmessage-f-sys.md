# onReceiveRttMessage（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## onReceiveRttMessage

```TypeScript
function onReceiveRttMessage(callback: Callback<RttMessageInfo>): void
```

订阅RTT消息事件

**起始版本：** 22

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RttMessageInfo](arkts-telephony-call-rttmessageinfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
