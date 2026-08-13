# isEmergencyPhoneNumber

## isEmergencyPhoneNumber

```TypeScript
function isEmergencyPhoneNumber(phoneNumber: string, options: EmergencyNumberOptions, callback: AsyncCallback<boolean>): void
```

根据电话号码参数，判断是否是紧急电话号码。使用callback异步回调。

**起始版本：** 7

<!--Device-call-function isEmergencyPhoneNumber(phoneNumber: string, options: EmergencyNumberOptions, callback: AsyncCallback<boolean>): void--><!--Device-call-function isEmergencyPhoneNumber(phoneNumber: string, options: EmergencyNumberOptions, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| options | [EmergencyNumberOptions](arkts-telephony-call-emergencynumberoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

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
import { BusinessError } from '@kit.BasicServicesKit';

let options: call.EmergencyNumberOptions = {slotId: 1}
call.isEmergencyPhoneNumber("112", options, (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isEmergencyPhoneNumber fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`isEmergencyPhoneNumber success, data->${JSON.stringify(data)}`);
    }
});
```


## isEmergencyPhoneNumber

```TypeScript
function isEmergencyPhoneNumber(phoneNumber: string, options?: EmergencyNumberOptions): Promise<boolean>
```

根据电话号码参数，判断是否是紧急电话号码。使用Promise异步回调。

**起始版本：** 7

<!--Device-call-function isEmergencyPhoneNumber(phoneNumber: string, options?: EmergencyNumberOptions): Promise<boolean>--><!--Device-call-function isEmergencyPhoneNumber(phoneNumber: string, options?: EmergencyNumberOptions): Promise<boolean>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| options | [EmergencyNumberOptions](arkts-telephony-call-emergencynumberoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

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
import { BusinessError } from '@kit.BasicServicesKit';

let options: call.EmergencyNumberOptions = {slotId: 1}
call.isEmergencyPhoneNumber("138xxxxxxxx", options).then((data: boolean) => {
    console.info(`isEmergencyPhoneNumber success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isEmergencyPhoneNumber fail, promise: err->${JSON.stringify(err)}`);
});
```


## isEmergencyPhoneNumber

```TypeScript
function isEmergencyPhoneNumber(phoneNumber: string, callback: AsyncCallback<boolean>): void
```

判断是否是紧急电话号码。使用callback异步回调。

**起始版本：** 7

<!--Device-call-function isEmergencyPhoneNumber(phoneNumber: string, callback: AsyncCallback<boolean>): void--><!--Device-call-function isEmergencyPhoneNumber(phoneNumber: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

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
import { BusinessError } from '@kit.BasicServicesKit';

call.isEmergencyPhoneNumber("138xxxxxxxx", (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isEmergencyPhoneNumber fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`isEmergencyPhoneNumber success, data->${JSON.stringify(data)}`);
    }
});
```
