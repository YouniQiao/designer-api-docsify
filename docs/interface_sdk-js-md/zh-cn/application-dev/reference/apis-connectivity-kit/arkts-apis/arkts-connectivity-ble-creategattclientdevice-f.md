# createGattClientDevice

## 导入模块

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## createGattClientDevice

```TypeScript
function createGattClientDevice(deviceId: string): GattClientDevice
```

创建[GattClientDevice](arkts-connectivity-ble-gattclientdevice-i.md)实例，表示GATT连接中的client端。

该接口仅支持BLE传输类型，若需自定义传输类型[BluetoothTransport](arkts-connectivity-connection-bluetoothtransport-e.md)，可使用[createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md)。通过该实例可以操作client端行为，如调用[connect](arkts-connectivity-ble-gattserver-i.md#connect)向对端设备发起连接，调用[getServices](arkts-connectivity-ble-gattclientdevice-i.md#getservices-1)获取对端设备支持的所有服务能力。创建该实例所需要的设备地址表示server端设备。可以通过[ble.startBLEScan](arkts-connectivity-ble-startblescan-f.md)或[BleScanner](arkts-connectivity-ble-blescanner-i.md)的[startScan](arkts-connectivity-ble-blescanner-i.md#startscan)接口获取server端设备地址，且需保证server端设备的BLE广播是可连接的。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ble-function createGattClientDevice(deviceId: string): GattClientDevice--><!--Device-ble-function createGattClientDevice(deviceId: string): GattClientDevice-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattClientDevice](arkts-connectivity-ble-gattclientdevice-i.md) | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-函数参数数量或参数类型不匹配) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |

**示例**

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

创建[GattClientDevice](arkts-connectivity-ble-gattclientdevice-i.md)实例，表示GATT连接中的client端，可通过[GattSetting](arkts-connectivity-ble-gattsetting-i.md)设置GATT连接参数。

通过该实例可以操作client端行为，如调用[connect](arkts-connectivity-ble-gattserver-i.md#connect)向对端设备发起连接，调用[getServices](arkts-connectivity-ble-gattclientdevice-i.md#getservices-1)获取对端设备支持的所有服务能力。创建该实例所需要的设备地址表示server端设备。可以通过[ble.startBLEScan](arkts-connectivity-ble-startblescan-f.md)或[BleScanner](arkts-connectivity-ble-blescanner-i.md)的[startScan](arkts-connectivity-ble-blescanner-i.md#startscan)接口获取server端设备地址，且需保证server端设备的BLE广播是可连接的。通过[GattSetting](arkts-connectivity-ble-gattsetting-i.md)设置连接的传输类型transport时，若不清楚设备的传输类型[BluetoothTransport](arkts-connectivity-connection-bluetoothtransport-e.md)，默认为[TRANSPORT_LE](arkts-connectivity-connection-bluetoothtransport-e.md)，但不能设置为[TRANSPORT_UNKNOWN](arkts-connectivity-connection-bluetoothtransport-e.md)（未知的设备传输方式），否则无法成功创建[GattClientDevice](arkts-connectivity-ble-gattclientdevice-i.md)实例。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务中使用。

<!--Device-ble-function createGattClientDevice(deviceId: string, setting: GattSetting): GattClientDevice--><!--Device-ble-function createGattClientDevice(deviceId: string, setting: GattSetting): GattClientDevice-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备的MAC地址，例如："XX:XX:XX:XX:XX:XX"。 |
| setting | [GattSetting](arkts-connectivity-ble-gattsetting-i.md) | 是 | GATT连接设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattClientDevice](arkts-connectivity-ble-gattclientdevice-i.md) | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |

**示例**

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
