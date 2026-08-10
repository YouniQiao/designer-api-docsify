# BluetoothAddress

Describe the type of Bluetooth address.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

<!--Device-common-export interface BluetoothAddress--><!--Device-common-export interface BluetoothAddress-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { common } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

The string of the Bluetooth address.

**类型：** string

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

<!--Device-BluetoothAddress-address: string--><!--Device-BluetoothAddress-address: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## addressType

```TypeScript
addressType: BluetoothAddressType
```

The type of the Bluetooth address.

**类型：** [BluetoothAddressType](arkts-connectivity-common-bluetoothaddresstype-e.md)

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

<!--Device-BluetoothAddress-addressType: BluetoothAddressType--><!--Device-BluetoothAddress-addressType: BluetoothAddressType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## rawAddressType

```TypeScript
rawAddressType?: BluetoothRawAddressType
```

Address type defined by the Bluetooth Core Specification.It is used only when the {@link BluetoothAddress#addressType} is {@link BluetoothAddressType#REAL}.

**类型：** [BluetoothRawAddressType](arkts-connectivity-common-bluetoothrawaddresstype-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-BluetoothAddress-rawAddressType?: BluetoothRawAddressType--><!--Device-BluetoothAddress-rawAddressType?: BluetoothRawAddressType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

