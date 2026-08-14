# Response

Describes the timestamp of the sensor data.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-interface Response--><!--Device-sensor-interface Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## accuracy

```TypeScript
accuracy: SensorAccuracy
```

Accuracy of the sensor data.

**Type:** [SensorAccuracy](arkts-sensorservice-sensor-sensoraccuracy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Response-accuracy: SensorAccuracy--><!--Device-Response-accuracy: SensorAccuracy-End-->

**System capability:** SystemCapability.Sensors.Sensor

## timestamp

```TypeScript
timestamp: long
```

Timestamp when the sensor reports data. Time from device startup to data reporting, in nanoseconds.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Response-timestamp: long--><!--Device-Response-timestamp: long-End-->

**System capability:** SystemCapability.Sensors.Sensor

