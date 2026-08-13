# makeApplicationRecord

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## makeApplicationRecord

```TypeScript
function makeApplicationRecord(bundleName: string): NdefRecord
```

Creates an NDEF Record with OpenHarmony application bundle name.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ndef-function makeApplicationRecord(bundleName: string): NdefRecord--><!--Device-ndef-function makeApplicationRecord(bundleName: string): NdefRecord-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | The bundle name of application to make. |

**Return value:**

| Type | Description |
| --- | --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) | The instance of NdefRecord. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

