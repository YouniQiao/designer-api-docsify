# SignificantMotionResponse

Describes the significant motion sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#Response).

**Inheritance/Implementation:** SignificantMotionResponse extends [Response](arkts-sensorservice-sensor-response-i.md#Response)

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-interface SignificantMotionResponse--><!--Device-sensor-interface SignificantMotionResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## scalar

```TypeScript
scalar: number
```

Intensity of a motion. This parameter specifies whether a device has a significant motion on three physical axes (X, Y, and Z). The value **1** is reported when the device has a significant motion.

**Type:** number

**Since:** 23

**Deprecated since:** -1

<!--Device-SignificantMotionResponse-scalar: double--><!--Device-SignificantMotionResponse-scalar: double-End-->

**System capability:** SystemCapability.Sensors.Sensor
