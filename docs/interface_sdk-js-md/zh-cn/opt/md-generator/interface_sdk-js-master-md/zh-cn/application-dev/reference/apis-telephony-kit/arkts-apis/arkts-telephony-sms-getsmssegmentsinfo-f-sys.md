# getSmsSegmentsInfo（系统接口）

## getSmsSegmentsInfo

```TypeScript
function getSmsSegmentsInfo(slotId: number, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void
```

获取短信段信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void--><!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| message | string | 是 |
| force7bit | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmsSegmentsInfo](arkts-telephony-sms-smssegmentsinfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
sms.getSmsSegmentsInfo(slotId, "message", false, (err: BusinessError, data: sms.SmsSegmentsInfo) => {
      console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getSmsSegmentsInfo

```TypeScript
function getSmsSegmentsInfo(slotId: number, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>
```

获取短信段信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>--><!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| message | string | 是 |
| force7bit | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SmsSegmentsInfo](arkts-telephony-sms-smssegmentsinfo-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let promise = sms.getSmsSegmentsInfo(slotId, "message", false);
promise.then((data: sms.SmsSegmentsInfo) => {
    console.info(`getSmsSegmentsInfo success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSmsSegmentsInfo failed, promise: err->${JSON.stringify(err)}`);
});
```
