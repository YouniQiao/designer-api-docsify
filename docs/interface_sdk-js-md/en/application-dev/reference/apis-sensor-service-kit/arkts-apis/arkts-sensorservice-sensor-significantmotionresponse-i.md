# SignificantMotionResponse

Describes the significant motion sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#Response).

**Inheritance/Implementation:** SignificantMotionResponse extends [Response](arkts-sensorservice-sensor-response-i.md#Response)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface SignificantMotionResponse extends Response--><!--Device-sensor-interface SignificantMotionResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## scalar

```TypeScript
scalar: double
```

Intensity of a motion. This parameter specifies whether a device has a significant motion on three physical axes(X, Y, and Z). The value **1** is reported when the device has a significant motion.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SignificantMotionResponse-scalar: double--><!--Device-SignificantMotionResponse-scalar: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

