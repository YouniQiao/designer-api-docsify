# @ohos.nfc.controller

Provides methods to operate or manage NFC.

**Since:** 12

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
| [closeNfc](arkts-connectivity-nfccontroller-closenfc-f.md#closenfc) | Disables NFC. |
| [disableNfc](arkts-connectivity-nfccontroller-disablenfc-f.md#disablenfc) | Disables NFC.This API can be called only by system applications |
| [enableNfc](arkts-connectivity-nfccontroller-enablenfc-f.md#enablenfc) | Enables NFC.This API can be called only by system applications |
| [getNfcState](arkts-connectivity-nfccontroller-getnfcstate-f.md#getnfcstate) | Obtains the NFC status.<p>The NFC status can be any of the following: <ul><li>{@link #STATE_OFF}: Indicates that NFC is disabled. <li>{@link #STATE_TURNING_ON}: Indicates that NFC is being enabled.<li>{@link #STATE_ON}: Indicates that NFC is enabled. <li>{@link #STATE_TURNING_OFF}: Indicates that NFC is being disabled.</ul> |
| [isNfcAvailable](arkts-connectivity-nfccontroller-isnfcavailable-f.md#isnfcavailable) | Checks whether a device supports NFC. |
| [isNfcOpen](arkts-connectivity-nfccontroller-isnfcopen-f.md#isnfcopen) | Checks whether NFC is enabled. |
| [isNfcSupported](arkts-connectivity-nfccontroller-isnfcsupported-f.md#isnfcsupported) | Checks whether a device supports NFC. |
| [off](arkts-connectivity-nfccontroller-off-f.md#off) | unregister nfc state changed event. |
| [on](arkts-connectivity-nfccontroller-on-f.md#on) | register nfc state changed event. |
| [openNfc](arkts-connectivity-nfccontroller-opennfc-f.md#opennfc) | Enables NFC. |

### Enums

| Name | Description |
| --- | --- |
| [NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md) | NFC changed states. |

