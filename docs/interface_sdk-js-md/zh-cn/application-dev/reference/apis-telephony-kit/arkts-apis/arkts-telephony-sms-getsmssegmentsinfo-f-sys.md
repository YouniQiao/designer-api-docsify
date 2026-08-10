# getSmsSegmentsInfo（系统接口）

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## getSmsSegmentsInfo

```TypeScript
function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void
```

Get an SMS segment encode relation information.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void--><!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| message | string | 是 | Indicates short message. |
| force7bit | boolean | 是 | Indicates whether to use 7 bit encoding. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SmsSegmentsInfo&gt; | 是 | Indicates the callback for getting a {@code SmsSegmentsInfo} object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

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
function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>
```

Get an SMS segment encode relation information.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>--><!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| message | string | 是 | Indicates short message. |
| force7bit | boolean | 是 | Indicates whether to use 7 bit encoding. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;SmsSegmentsInfo&gt; | Returns a { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

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

