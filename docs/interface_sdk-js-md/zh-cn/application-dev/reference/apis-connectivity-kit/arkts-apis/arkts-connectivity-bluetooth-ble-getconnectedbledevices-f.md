# getConnectedBLEDevices

## 导入模块

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## getConnectedBLEDevices

```TypeScript
function getConnectedBLEDevices(): Array<string>
```

获取和当前设备连接的BLE设备。

从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getConnectedBLEDevices](arkts-connectivity-bluetoothmanager-ble-getconnectedbledevices-f.md)

**需要权限：** ohos.permission.USE_BLUETOOTH

<!--Device-BLE-function getConnectedBLEDevices(): Array<string>--><!--Device-BLE-function getConnectedBLEDevices(): Array<string>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 返回当前设备作为Server端时连接BLE设备地址集合。 |

**示例**

```TypeScript
let result : Array<string> = bluetooth.BLE.getConnectedBLEDevices();
```
