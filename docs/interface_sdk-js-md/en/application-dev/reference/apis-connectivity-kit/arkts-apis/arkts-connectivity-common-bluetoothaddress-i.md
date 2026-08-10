# BluetoothAddress

Describe the type of Bluetooth address.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 26.0.0.

<!--Device-common-export interface BluetoothAddress--><!--Device-common-export interface BluetoothAddress-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { common } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

The string of the Bluetooth address.

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 26.0.0.

<!--Device-BluetoothAddress-address: string--><!--Device-BluetoothAddress-address: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## addressType

```TypeScript
addressType: BluetoothAddressType
```

The type of the Bluetooth address.

**Type:** [BluetoothAddressType](arkts-connectivity-common-bluetoothaddresstype-e.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 26.0.0.

<!--Device-BluetoothAddress-addressType: BluetoothAddressType--><!--Device-BluetoothAddress-addressType: BluetoothAddressType-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## rawAddressType

```TypeScript
rawAddressType?: BluetoothRawAddressType
```

Address type defined by the Bluetooth Core Specification.It is used only when the {@link BluetoothAddress#addressType} is {@link BluetoothAddressType#REAL}.

**Type:** [BluetoothRawAddressType](arkts-connectivity-common-bluetoothrawaddresstype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

<!--Device-BluetoothAddress-rawAddressType?: BluetoothRawAddressType--><!--Device-BluetoothAddress-rawAddressType?: BluetoothRawAddressType-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

