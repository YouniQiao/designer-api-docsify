# getLocalName

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## getLocalName

```TypeScript
function getLocalName(): string
```

Obtains the Bluetooth local name of a device.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getLocalName(): string--><!--Device-connection-function getLocalName(): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let localName: string = connection.getLocalName();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
