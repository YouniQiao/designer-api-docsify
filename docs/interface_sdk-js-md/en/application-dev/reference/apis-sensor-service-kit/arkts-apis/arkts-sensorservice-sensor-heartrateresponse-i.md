# HeartRateResponse

心率传感器数据，继承于[Response](arkts-sensorservice-sensor-response-i.md)。

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

用户的心率数值。单位：bpm（beats per minute，每分钟心跳次数）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-HeartRateResponse-heartRate: double--><!--Device-HeartRateResponse-heartRate: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

