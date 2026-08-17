# offNfcStateChange

## Modules to Import

```TypeScript
import { nfcController } from 'nfcController';
```

## offNfcStateChange

```TypeScript
function offNfcStateChange(callback?: Callback<NfcState>): void
```

unregister nfc state changed event.

**Since:** 23

<!--Device-nfcController-function offNfcStateChange(callback?: Callback<NfcState>): void--><!--Device-nfcController-function offNfcStateChange(callback?: Callback<NfcState>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md)&gt; | No | Callback used to listen to the nfc state changed event. |

