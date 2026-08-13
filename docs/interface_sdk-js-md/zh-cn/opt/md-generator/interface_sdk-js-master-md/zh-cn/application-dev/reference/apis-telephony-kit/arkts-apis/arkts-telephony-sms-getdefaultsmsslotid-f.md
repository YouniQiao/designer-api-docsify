# getDefaultSmsSlotId

## getDefaultSmsSlotId

```TypeScript
function getDefaultSmsSlotId(callback: AsyncCallback<number>): void
```

获取发送短信的默认SIM卡槽ID。使用callback异步回调。

**起始版本：** 7

<!--Device-sms-function getDefaultSmsSlotId(callback: AsyncCallback<int>): void--><!--Device-sms-function getDefaultSmsSlotId(callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSlotId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getDefaultSmsSlotId

```TypeScript
function getDefaultSmsSlotId(): Promise<number>
```

获取发送短信的默认SIM卡槽ID。使用Promise异步回调。

**起始版本：** 7

<!--Device-sms-function getDefaultSmsSlotId(): Promise<int>--><!--Device-sms-function getDefaultSmsSlotId(): Promise<int>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSlotId().then((data: number) => {
    console.info(`getDefaultSmsSlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultSmsSlotId failed, promise: err->${JSON.stringify(err)}`);
});
```
