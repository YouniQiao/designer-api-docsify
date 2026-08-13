# createNdefMessage

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## createNdefMessage

```TypeScript
function createNdefMessage(data: int[]): NdefMessage
```

Creates an NDEF message with raw bytes.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ndef-function createNdefMessage(data: int[]): NdefMessage--><!--Device-ndef-function createNdefMessage(data: int[]): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | int[] | Yes | The raw bytes to parse NDEF message. |

**Return value:**

| Type | Description |
| --- | --- |
| NdefMessage | The instance of NdefMessage. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |


## createNdefMessage

```TypeScript
function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage
```

Creates an NDEF message with record list.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ndef-function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage--><!--Device-ndef-function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ndefRecords | [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md)[] | Yes | The NDEF records to parse NDEF message. |

**Return value:**

| Type | Description |
| --- | --- |
| NdefMessage | The instance of NdefMessage. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

