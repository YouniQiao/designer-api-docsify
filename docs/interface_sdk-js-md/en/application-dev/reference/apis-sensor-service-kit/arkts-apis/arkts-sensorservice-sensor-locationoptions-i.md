# LocationOptions

指示地理位置，用于传入经纬度和海拔信息以计算地磁场。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface LocationOptions--><!--Device-sensor-interface LocationOptions-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## altitude

```TypeScript
altitude: double
```

海拔高度。单位：m（米）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-LocationOptions-altitude: double--><!--Device-LocationOptions-altitude: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## latitude

```TypeScript
latitude: double
```

纬度。取值范围：[-90, 90]。单位：degree（度）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-LocationOptions-latitude: double--><!--Device-LocationOptions-latitude: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## longitude

```TypeScript
longitude: double
```

经度。取值范围：[-180, 180]。单位：degree（度）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-LocationOptions-longitude: double--><!--Device-LocationOptions-longitude: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

