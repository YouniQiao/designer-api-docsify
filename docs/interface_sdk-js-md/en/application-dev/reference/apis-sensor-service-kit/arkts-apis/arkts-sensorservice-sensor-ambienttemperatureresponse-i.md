# AmbientTemperatureResponse

Describes the ambient temperature sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#Response).

**Inheritance/Implementation:** AmbientTemperatureResponse extends [Response](arkts-sensorservice-sensor-response-i.md#Response)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface AmbientTemperatureResponse extends Response--><!--Device-sensor-interface AmbientTemperatureResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## temperature

```TypeScript
temperature: double
```

Ambient temperature, in degree Celsius.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AmbientTemperatureResponse-temperature: double--><!--Device-AmbientTemperatureResponse-temperature: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

