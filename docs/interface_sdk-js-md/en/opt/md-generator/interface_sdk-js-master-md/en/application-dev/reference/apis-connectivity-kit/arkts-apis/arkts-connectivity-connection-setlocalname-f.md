# setLocalName

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## setLocalName

```TypeScript
function setLocalName(name: string): void
```

Sets the Bluetooth friendly name of a device. It is used only by system applications for security. If a non-system application invokes the interface, exception 801 is thrown.

**Since:** 26.0.0

**Deprecated since:** 12

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function setLocalName(name: string): void--><!--Device-connection-function setLocalName(name: string): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.setLocalName('device_name');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
