# pairDevice

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## pairDevice

```TypeScript
function pairDevice(deviceId: string): void
```

Starts pairing with a remote Bluetooth device. On API 10 and above, the permission required by this interface is changed from DISCOVER_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairDevice)

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetoothManager-function pairDevice(deviceId: string): void--><!--Device-bluetoothManager-function pairDevice(deviceId: string): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

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
import { BusinessError } from '@ohos.base';
try {
    // The address can be scanned.
    bluetoothManager.pairDevice("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```
