# DeviceListener

Provides hot swap information about an input device.

**Since:** 23

<!--Device-inputDevice-interface DeviceListener--><!--Device-inputDevice-interface DeviceListener-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## Modules to Import

```TypeScript
import { inputDevice } from 'inputDevice';
```

## deviceId

```TypeScript
deviceId: int
```

Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change.

**Type:** int

**Since:** 23

<!--Device-DeviceListener-deviceId: int--><!--Device-DeviceListener-deviceId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## type

```TypeScript
type: ChangedType
```

Device change type, which indicates whether an input device is inserted or removed.

**Type:** [ChangedType](arkts-input-inputdevice-changedtype-t.md)

**Since:** 23

<!--Device-DeviceListener-type: ChangedType--><!--Device-DeviceListener-type: ChangedType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

