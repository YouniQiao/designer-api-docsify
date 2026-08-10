# DeviceListener

描述输入设备热插拔的信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputDevice-interface DeviceListener--><!--Device-inputDevice-interface DeviceListener-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## deviceId

```TypeScript
deviceId: int
```

输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DeviceListener-deviceId: int--><!--Device-DeviceListener-deviceId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## type

```TypeScript
type: ChangedType
```

输入设备插入或者移除。

**Type:** [ChangedType](arkts-input-inputdevice-changedtype-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DeviceListener-type: ChangedType--><!--Device-DeviceListener-type: ChangedType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

