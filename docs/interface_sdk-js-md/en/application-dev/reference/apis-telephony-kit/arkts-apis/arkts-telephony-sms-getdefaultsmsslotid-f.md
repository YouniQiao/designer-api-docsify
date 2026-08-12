# getDefaultSmsSlotId

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## getDefaultSmsSlotId

```TypeScript
function getDefaultSmsSlotId(callback: AsyncCallback<int>): void
```

Obtains the default SIM card for sending SMS messages.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-sms-function getDefaultSmsSlotId(callback: AsyncCallback<int>): void--><!--Device-sms-function getDefaultSmsSlotId(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Indicates the callback for getting the default SIM card for sending SMS messages. Returns {@code 0} if the default SIM card for sending SMS messages is in card slot 1; Returns {@code 1} if the default SIM card for sending SMS messages is in card slot 2. |

## Examples

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSlotId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getDefaultSmsSlotId

```TypeScript
function getDefaultSmsSlotId(): Promise<int>
```

Obtains the default SIM card for sending SMS messages.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-sms-function getDefaultSmsSlotId(): Promise<int>--><!--Device-sms-function getDefaultSmsSlotId(): Promise<int>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Returns { |

## Examples

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSlotId().then((data: number) => {
    console.info(`getDefaultSmsSlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultSmsSlotId failed, promise: err->${JSON.stringify(err)}`);
});
```

