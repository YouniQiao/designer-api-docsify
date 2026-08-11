# off

## Modules to Import

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## off('nfcStateChange')

```TypeScript
function off(type: 'nfcStateChange', callback?: Callback<NfcState>): void
```

unregister nfc state changed event.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-nfcController-function off(type: 'nfcStateChange', callback?: Callback<NfcState>): void--><!--Device-nfcController-function off(type: 'nfcStateChange', callback?: Callback<NfcState>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'nfcStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NfcState&gt; | No |
