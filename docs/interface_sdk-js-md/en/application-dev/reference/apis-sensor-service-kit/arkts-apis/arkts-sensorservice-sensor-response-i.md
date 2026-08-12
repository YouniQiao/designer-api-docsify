# Response

Describes the timestamp of the sensor data.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface Response--><!--Device-sensor-interface Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## accuracy

```TypeScript
accuracy: SensorAccuracy
```

Accuracy of the sensor data.

**Type:** [SensorAccuracy](arkts-sensorservice-sensor-sensoraccuracy-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Response-accuracy: SensorAccuracy--><!--Device-Response-accuracy: SensorAccuracy-End-->

**System capability:** SystemCapability.Sensors.Sensor

## timestamp

```TypeScript
timestamp: long
```

Timestamp when the sensor reports data. Time from device startup to data reporting, in nanoseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Response-timestamp: long--><!--Device-Response-timestamp: long-End-->

**System capability:** SystemCapability.Sensors.Sensor

