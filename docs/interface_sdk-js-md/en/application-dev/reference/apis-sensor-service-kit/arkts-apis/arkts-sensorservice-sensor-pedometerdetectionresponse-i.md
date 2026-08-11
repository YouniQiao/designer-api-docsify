# PedometerDetectionResponse

Describes the pedometer detection sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** PedometerDetectionResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface PedometerDetectionResponse extends Response--><!--Device-sensor-interface PedometerDetectionResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## scalar

```TypeScript
scalar: double
```

Pedometer detection. This parameter specifies whether a user takes a step. The value **0** means that the user does not take a step, and **1** means that the user takes a step.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-PedometerDetectionResponse-scalar: double--><!--Device-PedometerDetectionResponse-scalar: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

