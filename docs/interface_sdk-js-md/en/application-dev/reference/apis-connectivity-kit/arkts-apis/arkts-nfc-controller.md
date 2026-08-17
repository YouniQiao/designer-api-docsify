# @ohos.nfc.controller

Provides methods to operate or manage NFC.

**Since:** 23

<!--Device-unnamed-declare namespace nfcController--><!--Device-unnamed-declare namespace nfcController-End-->

**System capability:** SystemCapability.Communication.NFC.Core

## Modules to Import

```TypeScript
import { nfcController } from 'nfcController';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [closeNfc](arkts-connectivity-nfccontroller-closenfc-f.md#closenfc) | Disables NFC. |
| [disableNfc](arkts-connectivity-nfccontroller-disablenfc-f.md#disablenfc) | Disables NFC. This API can be called only by system applications |
| [enableNfc](arkts-connectivity-nfccontroller-enablenfc-f.md#enablenfc) | Enables NFC. This API can be called only by system applications |
| [getNfcState](arkts-connectivity-nfccontroller-getnfcstate-f.md#getnfcstate) | Obtains the NFC status. &lt;p&gt;The NFC status can be any of the following: &lt;ul&gt;&lt;li&gt;STATE_OFF: Indicates that NFC is disabled. &lt;li&gt;STATE_TURNING_ON: Indicates that NFC is being enabled. &lt;li&gt;STATE_ON: Indicates that NFC is enabled. &lt;li&gt;STATE_TURNING_OFF: Indicates that NFC is being disabled.&lt;/ul&gt; |
| [isNfcAvailable](arkts-connectivity-nfccontroller-isnfcavailable-f.md#isnfcavailable) | Checks whether a device supports NFC. |
| [isNfcOpen](arkts-connectivity-nfccontroller-isnfcopen-f.md#isnfcopen) | Checks whether NFC is enabled. |
| [isNfcSupported](arkts-connectivity-nfccontroller-isnfcsupported-f.md#isnfcsupported) | Checks whether a device supports NFC. |
| [offNfcStateChange](arkts-connectivity-nfccontroller-offnfcstatechange-f.md#offnfcstatechange) | unregister nfc state changed event. |
| [off_nfcStateChange](arkts-connectivity-nfccontroller-offnfcstatechange-f.md#offnfcstatechange) | unregister nfc state changed event. |
| [onNfcStateChange](arkts-connectivity-nfccontroller-onnfcstatechange-f.md#onnfcstatechange) | register nfc state changed event. |
| [on_nfcStateChange](arkts-connectivity-nfccontroller-onnfcstatechange-f.md#onnfcstatechange) | register nfc state changed event. |
| [openNfc](arkts-connectivity-nfccontroller-opennfc-f.md#opennfc) | Enables NFC. |

### Enums

| Name | Description |
| --- | --- |
| [NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md) | NFC changed states. |

