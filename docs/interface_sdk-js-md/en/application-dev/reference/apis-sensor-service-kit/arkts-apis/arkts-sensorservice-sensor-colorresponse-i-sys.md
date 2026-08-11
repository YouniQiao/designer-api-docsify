# ColorResponse (System API)

Describes the color sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** ColorResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-sensor-interface ColorResponse extends Response--><!--Device-sensor-interface ColorResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## colorTemperature

```TypeScript
colorTemperature: double
```

Color temperature, in Kelvin.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ColorResponse-colorTemperature: double--><!--Device-ColorResponse-colorTemperature: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

## lightIntensity

```TypeScript
lightIntensity: double
```

Intensity of light, in lux.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ColorResponse-lightIntensity: double--><!--Device-ColorResponse-lightIntensity: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

