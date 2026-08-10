# FusionPressureResponse

融合压力传感器数据，继承于[Response](arkts-sensorservice-sensor-response-i.md)。

**Inheritance/Implementation:** FusionPressureResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-sensor-interface FusionPressureResponse extends Response--><!--Device-sensor-interface FusionPressureResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## fusionPressure

```TypeScript
fusionPressure: double
```

融合压力值，表示施加在融合压力传感器上的压力值百分比。单位：%（百分比）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-FusionPressureResponse-fusionPressure: double--><!--Device-FusionPressureResponse-fusionPressure: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

