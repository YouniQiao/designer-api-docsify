# getNfcState

## Modules to Import

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## getNfcState

```TypeScript
function getNfcState(): NfcState
```

Obtains the NFC status.&lt;p&gt;The NFC status can be any of the following: &lt;ul&gt;&lt;li&gt;{@link #STATE_OFF}: Indicates that NFC is disabled. &lt;li&gt;{@link #STATE_TURNING_ON}: Indicates that NFC is being enabled.&lt;li&gt;{@link #STATE_ON}: Indicates that NFC is enabled. &lt;li&gt;{@link #STATE_TURNING_OFF}: Indicates that NFC is being disabled.&lt;/ul&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-nfcController-function getNfcState(): NfcState--><!--Device-nfcController-function getNfcState(): NfcState-End-->

**System capability:** SystemCapability.Communication.NFC.Core

**Return value:**

| Type | Description |
| --- | --- |
| [NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md) | Returns the NFC status. |

