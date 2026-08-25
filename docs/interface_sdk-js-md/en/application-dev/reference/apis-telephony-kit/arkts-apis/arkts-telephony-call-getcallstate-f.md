# getCallState

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## getCallState

```TypeScript
function getCallState(callback: AsyncCallback<CallState>): void
```

Obtains the call status. This API uses an asynchronous callback to return the result.

**Since:** 6

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CallState&gt; | Yes |


## getCallState

```TypeScript
function getCallState(): Promise<CallState>
```

Obtains the call status. This API uses a promise to return the result.

**Since:** 6

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;CallState & gt; |
