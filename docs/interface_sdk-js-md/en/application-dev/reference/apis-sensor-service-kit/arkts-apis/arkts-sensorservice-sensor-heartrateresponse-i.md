# HeartRateResponse

Describes the heart rate sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** HeartRateResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface HeartRateResponse extends Response--><!--Device-sensor-interface HeartRateResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## heartRate

```TypeScript
heartRate: double
```

Heart rate, in beats per minute (bpm).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-HeartRateResponse-heartRate: double--><!--Device-HeartRateResponse-heartRate: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

