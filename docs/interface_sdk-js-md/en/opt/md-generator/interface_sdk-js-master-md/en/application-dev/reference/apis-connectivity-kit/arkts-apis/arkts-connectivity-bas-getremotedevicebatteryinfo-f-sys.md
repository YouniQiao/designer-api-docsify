# getRemoteDeviceBatteryInfo (System API)

## Modules to Import

```TypeScript
import { bas } from 'kits/@kit.ConnectivityKit';
```

## getRemoteDeviceBatteryInfo

```TypeScript
function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>
```

Get remote device battery information.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bas-function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>--><!--Device-bas-function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | [BluetoothAddress](arkts-connectivity-common-bluetoothaddress-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;BatteryInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 2901003 |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |
