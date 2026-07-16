# BluetoothAddress

Describe the type of Bluetooth address.

**Since:** 21

<!--Device-common-export interface BluetoothAddress--><!--Device-common-export interface BluetoothAddress-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { common } from '@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

The string of the Bluetooth address.

**Type:** string

**Since:** 21

<!--Device-BluetoothAddress-address: string--><!--Device-BluetoothAddress-address: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## addressType

```TypeScript
addressType: BluetoothAddressType
```

The type of the Bluetooth address.

**Type:** BluetoothAddressType

**Since:** 21

<!--Device-BluetoothAddress-addressType: BluetoothAddressType--><!--Device-BluetoothAddress-addressType: BluetoothAddressType-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## rawAddressType

```TypeScript
rawAddressType?: BluetoothRawAddressType
```

Address type defined by the Bluetooth Core Specification.It is used only when the {@link BluetoothAddress#addressType} is {@link BluetoothAddressType#REAL}.

**Type:** BluetoothRawAddressType

**Since:** 23

<!--Device-BluetoothAddress-rawAddressType?: BluetoothRawAddressType--><!--Device-BluetoothAddress-rawAddressType?: BluetoothRawAddressType-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

