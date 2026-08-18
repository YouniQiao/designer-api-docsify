# getDnsAscii

## Modules to Import

```TypeScript
```

## getDnsAscii

```TypeScript
function getDnsAscii(host: string, flag?: ConversionProcess): string
```

Convert a string from Unicode to ASCII Compatible Encoding (ACE), as defined by the ToASCII operation of RFC 3490.

**Since:** 26.0.0

<!--Device-connection-function getDnsAscii(host: string, flag?: ConversionProcess): string--><!--Device-connection-function getDnsAscii(host: string, flag?: ConversionProcess): string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| host | string | Yes |
| flag | [ConversionProcess](arkts-network-connection-conversionprocess-e.md) | No | Indicates process flag, can be 0 or any logical OR of possible flags. can be ALLOW_UNASSIGNED \|

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
