# ScanFilter

Describes the criteria for filtering scanning results can be set.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ble-interface ScanFilter--><!--Device-ble-interface ScanFilter-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { ble } from 'ble';
```

## irk

```TypeScript
irk?: Uint8Array
```

Identity Resolving Key of BLE peripheral device. [irk](#irk) needs to be used with [address](arkts-connectivity-ble-scanfilter-i.md#address).

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanFilter-irk?: Uint8Array--><!--Device-ScanFilter-irk?: Uint8Array-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

