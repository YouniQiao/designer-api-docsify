# LightResponse

Describes the ambient light sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response).

**Inheritance/Implementation:** LightResponse extends [Response](arkts-sensorservice-sensor-response-i.md#response)

**Since:** 23

<!--Device-sensor-interface LightResponse--><!--Device-sensor-interface LightResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## colorTemperature

```TypeScript
colorTemperature?: double
```

Color temperature, in Kelvin. This parameter is optional. If this parameter is not supported, a fixed value ( customized by the sensor) is returned. If this parameter is supported, a normal value is returned.

**Type:** double

**Since:** 23

<!--Device-LightResponse-colorTemperature?: double--><!--Device-LightResponse-colorTemperature?: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## infraredLuminance

```TypeScript
infraredLuminance?: double
```

Infrared luminance, in cd/m?. This parameter is optional. If this parameter is not supported, a fixed value ( customized by the sensor) is returned. If this parameter is supported, a normal value is returned.

**Type:** double

**Since:** 23

<!--Device-LightResponse-infraredLuminance?: double--><!--Device-LightResponse-infraredLuminance?: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## intensity

```TypeScript
intensity: double
```

Illumination, in lux.

**Type:** double

**Since:** 23

<!--Device-LightResponse-intensity: double--><!--Device-LightResponse-intensity: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

