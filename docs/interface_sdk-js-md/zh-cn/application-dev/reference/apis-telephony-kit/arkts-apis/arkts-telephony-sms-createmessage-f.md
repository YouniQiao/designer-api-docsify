# createMessage

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## createMessage

```TypeScript
function createMessage(pdu: Array<number>, specification: string, callback: AsyncCallback<ShortMessage>): void
```

根据协议数据单元(PDU)和指定的短信协议创建短信实例。使用callback异步回调。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pdu | Array & lt;number & gt; | 是 |
| specification | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ShortMessage](arkts-telephony-sms-shortmessage-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## createMessage

```TypeScript
function createMessage(pdu: Array<number>, specification: string): Promise<ShortMessage>
```

根据协议数据单元(PDU)和指定的短信协议创建短信实例。使用Promise异步回调。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pdu | Array & lt;number & gt; | 是 |
| specification | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ShortMessage](arkts-telephony-sms-shortmessage-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
