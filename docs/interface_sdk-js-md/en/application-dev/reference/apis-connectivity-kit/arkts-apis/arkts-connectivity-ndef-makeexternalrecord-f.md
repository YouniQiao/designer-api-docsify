# makeExternalRecord

## Modules to Import

```TypeScript
import { tag } from 'tag';
```

## makeExternalRecord

```TypeScript
function makeExternalRecord(domainName: string, type: string, externalData: int[]): NdefRecord
```

Creates an NDEF record with external data.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ndef-function makeExternalRecord(domainName: string, type: string, externalData: int[]): NdefRecord--><!--Device-ndef-function makeExternalRecord(domainName: string, type: string, externalData: int[]): NdefRecord-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainName | string | Yes | Domain name of issuing organization for the external data. |
| type | string | Yes | Domain specific type of data for the external data. |
| externalData | int[] | Yes | Data payload of an NDEF record. |

**Return value:**

| Type | Description |
| --- | --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) | The instance of NdefRecord. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

