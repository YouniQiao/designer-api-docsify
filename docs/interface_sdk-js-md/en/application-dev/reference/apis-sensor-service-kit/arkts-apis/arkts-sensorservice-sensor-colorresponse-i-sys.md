# ColorResponse (System API)

Describes the color sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** ColorResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 10

<!--Device-sensor-interface ColorResponse extends Response--><!--Device-sensor-interface ColorResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## colorTemperature

```TypeScript
colorTemperature: number
```

Color temperature, in Kelvin.

**Type:** number

**Since:** 10

<!--Device-ColorResponse-colorTemperature: double--><!--Device-ColorResponse-colorTemperature: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

## lightIntensity

```TypeScript
lightIntensity: number
```

Intensity of light, in lux.

**Type:** number

**Since:** 10

<!--Device-ColorResponse-lightIntensity: double--><!--Device-ColorResponse-lightIntensity: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

