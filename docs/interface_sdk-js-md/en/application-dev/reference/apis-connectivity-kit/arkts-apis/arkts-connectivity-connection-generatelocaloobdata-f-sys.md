# generateLocalOobData (System API)

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## generateLocalOobData

```TypeScript
function generateLocalOobData(transport: BluetoothTransport): Promise<OobData>
```

Generate out-of-band data of the local device.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [transport](arkts-connectivity-ble-gattsetting-i.md) | [BluetoothTransport](arkts-connectivity-connection-bluetoothtransport-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OobData](arkts-connectivity-connection-oobdata-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900003 |
| 2900099 |
