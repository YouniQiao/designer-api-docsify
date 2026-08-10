# SarResponse (System API)

吸收比率传感器数据，继承于[Response](arkts-sensorservice-sensor-response-i.md)。用于表示吸收比率传感器上报的响应数据，包含电磁波吸收率信息。

**Inheritance/Implementation:** SarResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-sensor-interface SarResponse extends Response--><!--Device-sensor-interface SarResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## absorptionRatio

```TypeScript
absorptionRatio: double
```

表示具体的吸收率。单位：W/kg。取值范围：取值为实际上报物理量，由硬件传感器决定。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SarResponse-absorptionRatio: double--><!--Device-SarResponse-absorptionRatio: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

