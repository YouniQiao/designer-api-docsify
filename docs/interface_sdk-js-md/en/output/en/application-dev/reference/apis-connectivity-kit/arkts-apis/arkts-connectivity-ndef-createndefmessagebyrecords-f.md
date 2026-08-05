# createNdefMessageByRecords

## createNdefMessageByRecords

```TypeScript
function createNdefMessageByRecords(ndefRecords: NdefRecord[]): NdefMessage
```

Creates an NDEF message with record list.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ndef-function createNdefMessageByRecords(ndefRecords: NdefRecord[]): NdefMessage--><!--Device-ndef-function createNdefMessageByRecords(ndefRecords: NdefRecord[]): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ndefRecords | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | The NDEF records to parse NDEF message. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The instance of NdefMessage. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |

