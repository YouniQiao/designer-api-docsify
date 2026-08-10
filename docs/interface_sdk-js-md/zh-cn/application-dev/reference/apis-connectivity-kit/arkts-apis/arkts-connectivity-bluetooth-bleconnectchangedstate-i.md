# BLEConnectChangedState

Describes the Gatt profile connection state.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.BLEConnectChangedState

<!--Device-bluetooth-interface BLEConnectChangedState--><!--Device-bluetooth-interface BLEConnectChangedState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## deviceId

```TypeScript
deviceId: string
```

Indicates the peer device address

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.BLEConnectChangedState.deviceId

<!--Device-BLEConnectChangedState-deviceId: string--><!--Device-BLEConnectChangedState-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: ProfileConnectionState
```

Connection state of the Gatt profile

**类型：** [ProfileConnectionState](arkts-connectivity-baseprofile-profileconnectionstate-t.md)

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.BLEConnectChangedState.state

<!--Device-BLEConnectChangedState-state: ProfileConnectionState--><!--Device-BLEConnectChangedState-state: ProfileConnectionState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

