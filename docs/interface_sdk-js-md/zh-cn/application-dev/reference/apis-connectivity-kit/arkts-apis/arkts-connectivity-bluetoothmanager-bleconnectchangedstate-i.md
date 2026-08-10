# BLEConnectChangedState

Describes the Gatt profile connection state.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.BLEConnectionChangeState

<!--Device-bluetoothManager-interface BLEConnectChangedState--><!--Device-bluetoothManager-interface BLEConnectChangedState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## deviceId

```TypeScript
deviceId: string
```

Indicates the peer device address

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.BLEConnectionChangeState#deviceId

<!--Device-BLEConnectChangedState-deviceId: string--><!--Device-BLEConnectChangedState-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: ProfileConnectionState
```

Connection state of the Gatt profile

**类型：** [ProfileConnectionState](arkts-connectivity-baseprofile-profileconnectionstate-t.md)

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.BLEConnectionChangeState#state

<!--Device-BLEConnectChangedState-state: ProfileConnectionState--><!--Device-BLEConnectChangedState-state: ProfileConnectionState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

