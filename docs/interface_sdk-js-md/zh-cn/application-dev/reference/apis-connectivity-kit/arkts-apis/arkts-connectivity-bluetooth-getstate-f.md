# getState

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getState

```TypeScript
function getState(): BluetoothState
```

Obtains the Bluetooth status of a device.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.getState

**需要权限：** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getState(): BluetoothState--><!--Device-bluetooth-function getState(): BluetoothState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BluetoothState](arkts-connectivity-bluetoothmanager-bluetoothstate-e.md) | Returns the Bluetooth status, which can be { |

## 示例

```TypeScript
let state : bluetooth.BluetoothState = bluetooth.getState();
```

