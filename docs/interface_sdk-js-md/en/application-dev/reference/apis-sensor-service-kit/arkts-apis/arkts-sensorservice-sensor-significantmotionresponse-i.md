# SignificantMotionResponse

Describes the significant motion sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response).

**Inheritance/Implementation:** SignificantMotionResponse extends [Response](arkts-sensorservice-sensor-response-i.md#response)

**Since:** 23

<!--Device-sensor-interface SignificantMotionResponse--><!--Device-sensor-interface SignificantMotionResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## scalar

```TypeScript
scalar: double
```

Intensity of a motion. This parameter specifies whether a device has a significant motion on three physical axes (X, Y, and Z). The value **1** is reported when the device has a significant motion.

**Type:** double

**Since:** 23

<!--Device-SignificantMotionResponse-scalar: double--><!--Device-SignificantMotionResponse-scalar: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

