# onNfcStateChange

## Modules to Import

```TypeScript
import { nfcController } from '@kit.ConnectivityKit';
```

## onNfcStateChange

```TypeScript
function onNfcStateChange(callback: Callback<NfcState>): void
```

register nfc state changed event.

**Since:** 23

<!--Device-nfcController-function onNfcStateChange(callback: Callback<NfcState>): void--><!--Device-nfcController-function onNfcStateChange(callback: Callback<NfcState>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md)&gt; | Yes | Callback used to listen to the nfc state changed event. |

