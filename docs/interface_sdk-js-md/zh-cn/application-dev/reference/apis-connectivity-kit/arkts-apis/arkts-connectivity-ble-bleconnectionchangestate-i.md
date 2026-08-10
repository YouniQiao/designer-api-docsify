# BLEConnectionChangeState

Describes the Gatt profile connection state.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ble-interface BLEConnectionChangeState--><!--Device-ble-interface BLEConnectionChangeState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## deviceId

```TypeScript
deviceId: string
```

Indicates the peer device address

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BLEConnectionChangeState-deviceId: string--><!--Device-BLEConnectionChangeState-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## reason

```TypeScript
reason?: GattDisconnectReason
```

Reason of the disconnection of the gatt connection.

**类型：** [GattDisconnectReason](arkts-connectivity-ble-gattdisconnectreason-e.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-BLEConnectionChangeState-reason?: GattDisconnectReason--><!--Device-BLEConnectionChangeState-reason?: GattDisconnectReason-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## reasonMessage

```TypeScript
reasonMessage?: string
```

Reason message of the disconnection of the gatt connection.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-BLEConnectionChangeState-reasonMessage?: string--><!--Device-BLEConnectionChangeState-reasonMessage?: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: ProfileConnectionState
```

Connection state of the Gatt profile

**类型：** [ProfileConnectionState](arkts-connectivity-baseprofile-profileconnectionstate-t.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BLEConnectionChangeState-state: ProfileConnectionState--><!--Device-BLEConnectionChangeState-state: ProfileConnectionState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

