# createGattClientDevice

## 导入模块

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## createGattClientDevice

```TypeScript
function createGattClientDevice(deviceId: string): GattClientDevice
```

创建一个可使用的GattClientDevice实例。

从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createGattClientDevice](arkts-connectivity-bluetoothmanager-ble-creategattclientdevice-f.md)

<!--Device-BLE-function createGattClientDevice(deviceId: string): GattClientDevice--><!--Device-BLE-function createGattClientDevice(deviceId: string): GattClientDevice-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| GattClientDevice | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**示例**

```TypeScript
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
```
