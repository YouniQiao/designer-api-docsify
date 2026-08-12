# convertUuid

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## convertUuid

```TypeScript
function convertUuid(uuid: string): string
```

Convert 2-byte and 4-byte UUID strings to the 16-byte UUID string standard used in Bluetooth.

**Since:** 22

<!--Device-access-function convertUuid(uuid: string): string--><!--Device-access-function convertUuid(uuid: string): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let inputUuid: string = '1801';
    let convertedUuid: string = access.convertUuid(inputUuid);
    console.info("convertedUuid: " + convertedUuid);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
