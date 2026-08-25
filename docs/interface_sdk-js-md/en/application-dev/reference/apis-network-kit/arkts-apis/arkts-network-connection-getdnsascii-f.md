# getDnsAscii

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getDnsAscii

```TypeScript
function getDnsAscii(host: string, flag?: ConversionProcess): string
```

Converts the host name from Unicode to ASCII and controls the conversion behavior through the optional conversion process parameter (**conversionProcess**).

> **NOTE：**&gt;
> If **conversionProcess** is set to **NO_CONFIGURATION**, only the domain names corresponding to the Unicode
> characters that have been officially allocated can be converted.

> When **conversionProcess** is set to **ALLOW_UNASSIGNED**, domain names that contain Unicode characters that have
> not been assigned meanings can be converted.

> If **conversionProcess** is set to **USE_STD3_ASCII_RULES**, the generated ASCII domain name is forcibly checked
> based on the STD-3 ASCII rule (RFC 1123 standard) during the conversion.

> Digits and English letters in the input parameters are not transcoded.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| host | string | Yes |
| flag | [ConversionProcess](arkts-network-connection-conversionprocess-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';

let result = connection.getDnsAscii("www.example.com," connection.ConversionProcess.NO_CONFIGURATION);
console.info(result);  // Expected result: www.xn--fsq092h.com
let result = connection.getDnsAscii("www.example.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info(result);  // Expected result: www.example.com
```
