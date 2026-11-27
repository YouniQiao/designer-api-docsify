# stopBLEScan

## 导入模块

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## stopBLEScan

```TypeScript
function stopBLEScan(): void
```

停止BLE扫描流程。

从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [stopBLEScan](arkts-connectivity-bluetoothmanager-ble-stopblescan-f.md)

**需要权限：** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-BLE-function stopBLEScan(): void--><!--Device-BLE-function stopBLEScan(): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**示例**

```TypeScript
bluetooth.BLE.stopBLEScan();
```
