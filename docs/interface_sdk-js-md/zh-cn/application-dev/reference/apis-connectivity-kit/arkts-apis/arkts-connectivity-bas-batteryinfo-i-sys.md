# BatteryInfo（系统接口）

Describe the contents of the battery information.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-bas-interface BatteryInfo--><!--Device-bas-interface BatteryInfo-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { bas } from 'kits/@kit.ConnectivityKit';
```

## batteryLevel

```TypeScript
batteryLevel: int
```

battery value of the device. {@code -1} means no power information.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-batteryLevel: int--><!--Device-BatteryInfo-batteryLevel: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## deviceId

```TypeScript
deviceId: BluetoothAddress
```

Identify of the discovery device.

**类型：** [BluetoothAddress](arkts-connectivity-ble-bluetoothaddress-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-deviceId: BluetoothAddress--><!--Device-BatteryInfo-deviceId: BluetoothAddress-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

