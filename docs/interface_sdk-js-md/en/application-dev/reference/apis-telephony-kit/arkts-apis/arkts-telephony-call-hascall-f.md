# hasCall

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## hasCall

```TypeScript
function hasCall(callback: AsyncCallback<boolean>): void
```

Checks whether a call is in progress. This API uses an asynchronous callback to return the result.

**Since:** 6

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## hasCall

```TypeScript
function hasCall(): Promise<boolean>
```

Checks whether a call is in progress. This API uses a promise to return the result.

**Since:** 6

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
