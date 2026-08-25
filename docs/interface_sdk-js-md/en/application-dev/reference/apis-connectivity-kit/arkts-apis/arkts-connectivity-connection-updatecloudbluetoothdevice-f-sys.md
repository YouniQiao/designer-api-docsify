# updateCloudBluetoothDevice (System API)

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## updateCloudBluetoothDevice

```TypeScript
function updateCloudBluetoothDevice(trustedPairedDevices: TrustedPairedDevices): Promise<void>
```

update cloud devices.

**Since:** 15

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [trustedPairedDevices](arkts-connectivity-connection-trustedpaireddevices-i-sys.md) | [TrustedPairedDevices](arkts-connectivity-connection-trustedpaireddevices-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900001 |
| 2900003 |
| 2900099 |
