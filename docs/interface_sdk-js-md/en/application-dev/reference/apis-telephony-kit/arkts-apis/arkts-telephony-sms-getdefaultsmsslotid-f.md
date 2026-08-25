# getDefaultSmsSlotId

## Modules to Import

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## getDefaultSmsSlotId

```TypeScript
function getDefaultSmsSlotId(callback: AsyncCallback<number>): void
```

Obtains the default slot ID of the SIM card used to send SMS messages. This API uses an asynchronous callback to return the result.

**Since:** 7

**System capability:** SystemCapability.Telephony.SmsMms

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## getDefaultSmsSlotId

```TypeScript
function getDefaultSmsSlotId(): Promise<number>
```

Obtains the default slot ID of the SIM card used to send SMS messages. This API uses a promise to return the result.

**Since:** 7

**System capability:** SystemCapability.Telephony.SmsMms

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |
