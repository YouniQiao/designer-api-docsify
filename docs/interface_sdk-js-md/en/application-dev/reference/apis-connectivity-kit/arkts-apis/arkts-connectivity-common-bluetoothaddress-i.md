# BluetoothAddress

Describe the type of Bluetooth address.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

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

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-BluetoothAddress-address: string--><!--Device-BluetoothAddress-address: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## addressType

```TypeScript
addressType: BluetoothAddressType
```

The type of the Bluetooth address.

**Type:** [BluetoothAddressType](arkts-connectivity-common-bluetoothaddresstype-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-BluetoothAddress-addressType: BluetoothAddressType--><!--Device-BluetoothAddress-addressType: BluetoothAddressType-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## rawAddressType

```TypeScript
rawAddressType?: BluetoothRawAddressType
```

Address type defined by the Bluetooth Core Specification. It is used only when the [addressType](#addressType) is [REAL](arkts-connectivity-common-bluetoothaddresstype-e.md#REAL).

**Type:** [BluetoothRawAddressType](arkts-connectivity-common-bluetoothrawaddresstype-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-BluetoothAddress-rawAddressType?: BluetoothRawAddressType--><!--Device-BluetoothAddress-rawAddressType?: BluetoothRawAddressType-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

