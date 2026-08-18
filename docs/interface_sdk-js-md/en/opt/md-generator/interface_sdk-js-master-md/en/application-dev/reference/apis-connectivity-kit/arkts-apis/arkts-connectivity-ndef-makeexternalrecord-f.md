# makeExternalRecord

## Modules to Import

```TypeScript
```

## makeExternalRecord

```TypeScript
function makeExternalRecord(domainName: string, type: string, externalData: number[]): NdefRecord
```

Creates an NDEF record with external data.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ndef-function makeExternalRecord(domainName: string, type: string, externalData: int[]): NdefRecord--><!--Device-ndef-function makeExternalRecord(domainName: string, type: string, externalData: int[]): NdefRecord-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domainName | string | Yes |
| type | string | Yes |
| externalData | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
