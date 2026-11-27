# getConnectedBLEDevices

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## getConnectedBLEDevices

```TypeScript
function getConnectedBLEDevices(): Array<string>
```

Obtains the list of devices in the connected status.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function getConnectedBLEDevices(): Array<string>--><!--Device-ble-function getConnectedBLEDevices(): Array<string>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Returns the list of device address. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
try {
    let result: Array<string> = ble.getConnectedBLEDevices();
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```


## getConnectedBLEDevices

```TypeScript
function getConnectedBLEDevices(profile: BleProfile): Array<string>
```

Obtains the list of devices in the connected status.

**Since:** 21

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function getConnectedBLEDevices(profile: BleProfile): Array<string>--><!--Device-ble-function getConnectedBLEDevices(profile: BleProfile): Array<string>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [BleProfile](arkts-connectivity-ble-bleprofile-e.md) | Yes | The profile in the BLE protocol. It is used to obtain the connected devices corresponding to the profile. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Returns the list of device address. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
try {
    let result: Array<string> = ble.getConnectedBLEDevices(ble.BleProfile.GATT_CLIENT);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
