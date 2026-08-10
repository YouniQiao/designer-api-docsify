# DeviceClass

Describes the class of a bluetooth device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-connection-interface DeviceClass--><!--Device-connection-interface DeviceClass-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## classOfDevice

```TypeScript
classOfDevice: int
```

Class of the device.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceClass-classOfDevice: int--><!--Device-DeviceClass-classOfDevice: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## majorClass

```TypeScript
majorClass: MajorClass
```

Major classes of Bluetooth devices.

**Type:** [MajorClass](arkts-connectivity-bluetoothmanager-majorclass-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceClass-majorClass: MajorClass--><!--Device-DeviceClass-majorClass: MajorClass-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## majorMinorClass

```TypeScript
majorMinorClass: MajorMinorClass
```

Major and minor classes of Bluetooth devices.

**Type:** [MajorMinorClass](arkts-connectivity-bluetooth-majorminorclass-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceClass-majorMinorClass: MajorMinorClass--><!--Device-DeviceClass-majorMinorClass: MajorMinorClass-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

