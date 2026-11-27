# createGattClientDevice

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## createGattClientDevice

```TypeScript
function createGattClientDevice(deviceId: string): GattClientDevice
```

create a Gatt client device instance.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ble-function createGattClientDevice(deviceId: string): GattClientDevice--><!--Device-ble-function createGattClientDevice(deviceId: string): GattClientDevice-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates device ID. For example, "11:22:33:AA:BB:FF". |

**Return value:**

| Type | Description |
| --- | --- |
| [GattClientDevice](arkts-connectivity-ble-gattclientdevice-i.md) | Returns a Gatt client device instance `GattClientDevice`. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |

**Examples**

```TypeScript
try {
    let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```


## createGattClientDevice

```TypeScript
function createGattClientDevice(deviceId: string, setting: GattSetting): GattClientDevice
```

create a Gatt client device instance with custom setting.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ble-function createGattClientDevice(deviceId: string, setting: GattSetting): GattClientDevice--><!--Device-ble-function createGattClientDevice(deviceId: string, setting: GattSetting): GattClientDevice-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates device ID. For example, "11:22:33:AA:BB:FF". |
| setting | [GattSetting](arkts-connectivity-ble-gattsetting-i.md) | Yes | Indicates Gatt setting for connection. |

**Return value:**

| Type | Description |
| --- | --- |
| [GattClientDevice](arkts-connectivity-ble-gattclientdevice-i.md) | Returns a Gatt client device instance `GattClientDevice`. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |

**Examples**

```TypeScript
import { connection } from '@kit.ConnectivityKit';
try {
    let setting: ble.GattSetting = {
        autoConnect: true,
        transport: connection.BluetoothTransport.TRANSPORT_LE
    };
    let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX', setting);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
