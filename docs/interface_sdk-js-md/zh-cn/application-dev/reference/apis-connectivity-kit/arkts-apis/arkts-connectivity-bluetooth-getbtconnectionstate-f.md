# getBtConnectionState

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getBtConnectionState

```TypeScript
function getBtConnectionState(): ProfileConnectionState
```

Get the local device connection state to any profile of any remote device.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.getBtConnectionState

**需要权限：** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getBtConnectionState(): ProfileConnectionState--><!--Device-bluetooth-function getBtConnectionState(): ProfileConnectionState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](arkts-connectivity-baseprofile-profileconnectionstate-t.md) | One of { |

## 示例

```TypeScript
let connectionState : bluetooth.ProfileConnectionState = bluetooth.getBtConnectionState();
```

