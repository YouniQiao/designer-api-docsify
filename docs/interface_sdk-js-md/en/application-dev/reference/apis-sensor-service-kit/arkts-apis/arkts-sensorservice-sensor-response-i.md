# Response

Describes the timestamp of the sensor data.

**Since:** 8

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

**Type:** SensorAccuracy

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Response-accuracy: SensorAccuracy--><!--Device-Response-accuracy: SensorAccuracy-End-->

**System capability:** SystemCapability.Sensors.Sensor

## timestamp

```TypeScript
timestamp: number
```

Timestamp when the sensor reports data. Time from device startup to data reporting, in nanoseconds.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Response-timestamp: long--><!--Device-Response-timestamp: long-End-->

**System capability:** SystemCapability.Sensors.Sensor

