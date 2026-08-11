# createNdefMessageByData

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## createNdefMessageByData

```TypeScript
function createNdefMessageByData(data: int[]): NdefMessage
```

Creates an NDEF message with raw bytes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ndef-function createNdefMessageByData(data: int[]): NdefMessage--><!--Device-ndef-function createNdefMessageByData(data: int[]): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | int[] | Yes | The raw bytes to parse NDEF message. |

**Return value:**

| Type | Description |
| --- | --- |
| [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | The instance of NdefMessage. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

