# BLE（蓝牙）

```TypeScript
namespace BLE
```

BLE模块提供了对蓝牙操作和管理的方法。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [ble/ble](arkts-connectivity-bluetooth-ble.md)

<!--Device-bluetoothManager-namespace BLE--><!--Device-bluetoothManager-namespace BLE-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [createGattClientDevice](arkts-connectivity-bluetoothmanager-ble-creategattclientdevice-f.md#creategattclientdevice-1) | 创建一个可使用的GattClientDevice实例。 |
| [createGattServer](arkts-connectivity-bluetoothmanager-ble-creategattserver-f.md#creategattserver-1) | 创建一个可使用的GattServer实例。 |
| [getConnectedBLEDevices](arkts-connectivity-bluetoothmanager-ble-getconnectedbledevices-f.md#getconnectedbledevices-1) | 获取和当前设备连接的BLE设备。 |
| [off('BLEDeviceFind')](arkts-connectivity-bluetoothmanager-ble-off-f.md#offbledevicefind) | 取消订阅BLE设备发现上报事件。 |
| [on('BLEDeviceFind')](arkts-connectivity-bluetoothmanager-ble-on-f.md#onbledevicefind) | 订阅BLE设备发现上报事件。 |
| [startBLEScan](arkts-connectivity-bluetoothmanager-ble-startblescan-f.md#startblescan-1) | 发起BLE扫描流程。 |
| [stopBLEScan](arkts-connectivity-bluetoothmanager-ble-stopblescan-f.md#stopblescan-1) | 停止BLE扫描流程。 |
