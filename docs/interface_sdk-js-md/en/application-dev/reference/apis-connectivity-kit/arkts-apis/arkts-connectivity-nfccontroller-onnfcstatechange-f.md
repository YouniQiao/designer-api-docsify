# onNfcStateChange

## Modules to Import

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## onNfcStateChange

```TypeScript
function onNfcStateChange(callback: Callback<NfcState>): void
```

register nfc state changed event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-nfcController-function onNfcStateChange(callback: Callback<NfcState>): void--><!--Device-nfcController-function onNfcStateChange(callback: Callback<NfcState>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NfcState&gt; | Yes | Callback used to listen to the nfc state changed event. |

