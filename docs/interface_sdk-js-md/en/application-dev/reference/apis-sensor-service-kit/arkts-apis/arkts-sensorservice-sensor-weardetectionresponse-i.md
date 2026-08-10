# WearDetectionResponse

佩戴检测传感器数据，继承于[Response](arkts-sensorservice-sensor-response-i.md)。

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

设备佩戴状态。取值范围：0（未佩戴）或1（已佩戴）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-WearDetectionResponse-value: double--><!--Device-WearDetectionResponse-value: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

