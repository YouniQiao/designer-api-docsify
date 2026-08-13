# makeTextRecord

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## makeTextRecord

```TypeScript
function makeTextRecord(text: string, locale: string): NdefRecord
```

Creates an NDEF record with text data.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ndef-function makeTextRecord(text: string, locale: string): NdefRecord--><!--Device-ndef-function makeTextRecord(text: string, locale: string): NdefRecord-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Text data for new an NDEF record. |
| locale | string | Yes | Language code for the NDEF record. if locale is null, use default locale. |

**Return value:**

| Type | Description |
| --- | --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) | The instance of NdefRecord. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

