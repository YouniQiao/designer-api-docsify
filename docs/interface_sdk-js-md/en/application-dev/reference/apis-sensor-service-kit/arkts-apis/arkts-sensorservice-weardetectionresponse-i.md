# WearDetectionResponse

Describes the wear detection sensor data. It extends from [Response](arkts-sensorservice-response-i.md).

**Inheritance/Implementation:** WearDetectionResponse extends [Response](arkts-sensorservice-response-i.md)

**Since:** 8

<!--Device-sensor-interface WearDetectionResponse extends Response--><!--Device-sensor-interface WearDetectionResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## value

```TypeScript
value: number
```

Whether the device is being worn. The value **1** means that the device is being worn, and **0** means the opposite.

**Type:** number

**Since:** 8

<!--Device-WearDetectionResponse-value: double--><!--Device-WearDetectionResponse-value: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

