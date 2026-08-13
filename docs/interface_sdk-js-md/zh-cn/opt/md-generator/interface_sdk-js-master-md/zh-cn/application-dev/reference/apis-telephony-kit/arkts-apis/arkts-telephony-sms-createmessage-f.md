# createMessage

## createMessage

```TypeScript
function createMessage(pdu: Array<number>, specification: string, callback: AsyncCallback<ShortMessage>): void
```

根据协议数据单元(PDU)和指定的短信协议创建短信实例。使用callback异步回调。

**起始版本：** 6

<!--Device-sms-function createMessage(pdu: Array<int>, specification: string, callback: AsyncCallback<ShortMessage>): void--><!--Device-sms-function createMessage(pdu: Array<int>, specification: string, callback: AsyncCallback<ShortMessage>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pdu | Array & lt;number & gt; | 是 |
| specification | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ShortMessage](arkts-telephony-sms-shortmessage-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

const specification: string = '3gpp';
// 以数组的形式显示协议数据单元(PDU)，类型为number。
const pdu: Array<number> = [0x01, 0x00, 0x05, 0x81, 0x01, 0x80, 0xF6, 0x00, 0x00, 0x05, 0xE8, 0x32, 0x9B, 0xFD, 0x06];
sms.createMessage(pdu, specification, (err: BusinessError, data: sms.ShortMessage) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## createMessage

```TypeScript
function createMessage(pdu: Array<number>, specification: string): Promise<ShortMessage>
```

根据协议数据单元(PDU)和指定的短信协议创建短信实例。使用Promise异步回调。

**起始版本：** 6

<!--Device-sms-function createMessage(pdu: Array<int>, specification: string): Promise<ShortMessage>--><!--Device-sms-function createMessage(pdu: Array<int>, specification: string): Promise<ShortMessage>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

const specification: string = '3gpp';
// 以数组的形式显示协议数据单元(PDU)，类型为number。
const pdu: Array<number> = [0x01, 0x00, 0x05, 0x81, 0x01, 0x80, 0xF6, 0x00, 0x00, 0x05, 0xE8, 0x32, 0x9B, 0xFD, 0x06];
sms.createMessage(pdu, specification).then((data: sms.ShortMessage) => {
    console.info(`createMessage success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`createMessage failed, promise: err->${JSON.stringify(err)}`);
});
```
