# getImsShortMessageFormat（系统接口）

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## getImsShortMessageFormat

```TypeScript
function getImsShortMessageFormat(callback: AsyncCallback<string>): void
```

Gets SMS format supported on IMS. SMS over IMS format is either 3GPP or 3GPP2.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-function getImsShortMessageFormat(callback: AsyncCallback<string>): void--><!--Device-sms-function getImsShortMessageFormat(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | Indicates the callback for getting format, 3gpp, 3gpp2 or unknown. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getImsShortMessageFormat((err: BusinessError, data: string) => {
      console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getImsShortMessageFormat

```TypeScript
function getImsShortMessageFormat(): Promise<string>
```

Gets SMS format supported on IMS. SMS over IMS format is either 3GPP or 3GPP2.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-function getImsShortMessageFormat(): Promise<string>--><!--Device-sms-function getImsShortMessageFormat(): Promise<string>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Returns format, 3gpp, 3gpp2 or unknown. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getImsShortMessageFormat().then((data: string) => {
    console.info(`getImsShortMessageFormat success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getImsShortMessageFormat failed, promise: err->${JSON.stringify(err)}`);
});
```

