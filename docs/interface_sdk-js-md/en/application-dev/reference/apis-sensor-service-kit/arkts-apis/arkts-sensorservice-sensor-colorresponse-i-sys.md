# ColorResponse (System API)

颜色传感器数据，继承于[Response](arkts-sensorservice-sensor-response-i.md)。用于表示颜色传感器上报的响应数据，包含光照强度和色温信息。

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

表示色温。单位：开尔文（K）。取值范围：取值为实际上报物理量，由硬件传感器决定。典型值：暖白光约2700-3000K，正白光约4000-5000K，冷白光约6500K以上。

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

表示光的强度。单位：勒克斯（lux）。取值范围：取值为实际上报物理量，由硬件传感器决定。典型室内环境光强度约为300-500 lux，户外阳光可达10000 lux以上。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ColorResponse-lightIntensity: double--><!--Device-ColorResponse-lightIntensity: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

