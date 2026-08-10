# GattSetting

Describes the setting for Gatt Connection.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-ble-interface GattSetting--><!--Device-ble-interface GattSetting-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## autoConnect

```TypeScript
autoConnect?: boolean
```

Indicates whether to automatically connect to the remote device, default is {@code false}

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-GattSetting-autoConnect?: boolean--><!--Device-GattSetting-autoConnect?: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## transport

```TypeScript
transport?: BluetoothTransport
```

Transport of the connection, default is {@code TRANSPORT_LE}

**类型：** [BluetoothTransport](arkts-connectivity-ble-bluetoothtransport-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-GattSetting-transport?: BluetoothTransport--><!--Device-GattSetting-transport?: BluetoothTransport-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

