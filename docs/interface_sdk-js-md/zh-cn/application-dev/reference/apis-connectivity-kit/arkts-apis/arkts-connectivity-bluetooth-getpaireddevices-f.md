# getPairedDevices

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getPairedDevices

```TypeScript
function getPairedDevices(): Array<string>
```

Obtains the list of Bluetooth devices that have been paired with the current device.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.getPairedDevices

**需要权限：** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getPairedDevices(): Array<string>--><!--Device-bluetooth-function getPairedDevices(): Array<string>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | Returns a list of paired Bluetooth devices's address. |

## 示例

```TypeScript
let devices : Array<string> = bluetooth.getPairedDevices();
```

