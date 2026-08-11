# WearDetectionResponse

Describes the wear detection sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** WearDetectionResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface WearDetectionResponse extends Response--><!--Device-sensor-interface WearDetectionResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## value

```TypeScript
value: double
```

Whether the device is being worn. The value **1** means that the device is being worn, and **0** means the opposite.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-WearDetectionResponse-value: double--><!--Device-WearDetectionResponse-value: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

