# getDnsUnicode

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getDnsUnicode

```TypeScript
function getDnsUnicode(host: string, flag?: ConversionProcess): string
```

Convert a string from ASCII Compatible Encoding (ACE) to Unicode, as defined by the ToUnicode operation of RFC 3490.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

<!--Device-connection-function getDnsUnicode(host: string, flag?: ConversionProcess): string--><!--Device-connection-function getDnsUnicode(host: string, flag?: ConversionProcess): string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| host | string | Yes | Indicates the domain name of the ASCII type. |
| flag | [ConversionProcess](arkts-network-connection-conversionprocess-e.md) | No | Indicates process flag, can be 0 or any logical OR of possible flags. can be ALLOW_UNASSIGNED \| USE_STD3_ASCII_RULES to set all flag. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the converted string. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let result = connection.getDnsUnicode("www.xn--fsq092h.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info(result);  // Expected result: www.example.com
let result = connection.getDnsUnicode("www.example.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info(result);  // Expected result: www.example.com
```

