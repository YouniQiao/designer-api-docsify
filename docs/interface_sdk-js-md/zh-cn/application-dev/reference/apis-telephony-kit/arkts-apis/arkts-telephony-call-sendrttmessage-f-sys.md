# sendRttMessage（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## sendRttMessage

```TypeScript
function sendRttMessage(callId: number, rttMessage: string): Promise<void>
```

发送rtt消息

**起始版本：** 22

**需要权限：** ohos.permission.PLACE_CALL

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |
| [rttMessage](arkts-telephony-call-rttmessageinfo-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
