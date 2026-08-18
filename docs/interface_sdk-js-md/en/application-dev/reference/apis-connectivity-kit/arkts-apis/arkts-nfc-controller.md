# @ohos.nfc.controller

Provides methods to operate or manage NFC.

**Since:** 23

<!--Device-unnamed-declare namespace nfcController--><!--Device-unnamed-declare namespace nfcController-End-->

**System capability:** SystemCapability.Communication.NFC.Core

## Modules to Import

```TypeScript
import { nfcController } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [closeNfc](arkts-connectivity-nfccontroller-closenfc-f.md) | Disables NFC. |
| [disableNfc](arkts-connectivity-nfccontroller-disablenfc-f.md) | Disables NFC. This API can be called only by system applications |
| [enableNfc](arkts-connectivity-nfccontroller-enablenfc-f.md) | Enables NFC. This API can be called only by system applications |
| [getNfcState](arkts-connectivity-nfccontroller-getnfcstate-f.md) | Obtains the NFC status. &lt;p&gt;The NFC status can be any of the following: &lt;ul&gt;&lt;li&gt;STATE_OFF: Indicates that NFC is disabled. &lt;li&gt;STATE_TURNING_ON: Indicates that NFC is being enabled. &lt;li&gt;STATE_ON: Indicates that NFC is enabled. &lt;li&gt;STATE_TURNING_OFF: Indicates that NFC is being disabled.&lt;/ul&gt; |
| [isNfcAvailable](arkts-connectivity-nfccontroller-isnfcavailable-f.md) | Checks whether a device supports NFC. |
| [isNfcOpen](arkts-connectivity-nfccontroller-isnfcopen-f.md) | Checks whether NFC is enabled. |
| [isNfcSupported](arkts-connectivity-nfccontroller-isnfcsupported-f.md) | Checks whether a device supports NFC. |
| [offNfcStateChange](arkts-connectivity-nfccontroller-offnfcstatechange-f.md) | unregister nfc state changed event. |
| off_nfcStateChange | unregister nfc state changed event. |
| [onNfcStateChange](arkts-connectivity-nfccontroller-onnfcstatechange-f.md) | register nfc state changed event. |
| on_nfcStateChange | register nfc state changed event. |
| [openNfc](arkts-connectivity-nfccontroller-opennfc-f.md) | Enables NFC. |

### Enums

| Name | Description |
| --- | --- |
| [NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md) | NFC changed states. |

