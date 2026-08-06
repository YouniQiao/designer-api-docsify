# on

## on('nfcStateChange')

```TypeScript
function on(type: 'nfcStateChange', callback: Callback<NfcState>): void
```

register nfc state changed event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-nfcController-function on(type: 'nfcStateChange', callback: Callback<NfcState>): void--><!--Device-nfcController-function on(type: 'nfcStateChange', callback: Callback<NfcState>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'nfcStateChange' | Yes | The type to register. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;NfcState&gt; | Yes | Callback used to listen to the nfc state changed event. |

