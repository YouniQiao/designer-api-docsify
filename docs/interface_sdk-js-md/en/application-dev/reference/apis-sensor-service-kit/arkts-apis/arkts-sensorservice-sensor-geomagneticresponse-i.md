# GeomagneticResponse

设置地磁响应对象，用于描述指定地理位置的地磁场信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface GeomagneticResponse--><!--Device-sensor-interface GeomagneticResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## deflectionAngle

```TypeScript
deflectionAngle: double
```

磁偏角，即地磁北方向与正北方向在水平面上的角度。单位：degree（度）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GeomagneticResponse-deflectionAngle: double--><!--Device-GeomagneticResponse-deflectionAngle: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## geomagneticDip

```TypeScript
geomagneticDip: double
```

磁倾角，即地球磁场线与水平面的夹角。单位：degree（度）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GeomagneticResponse-geomagneticDip: double--><!--Device-GeomagneticResponse-geomagneticDip: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## levelIntensity

```TypeScript
levelIntensity: double
```

水平磁场强度，即地磁场在水平面上的总强度。单位：nT（纳特斯拉）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GeomagneticResponse-levelIntensity: double--><!--Device-GeomagneticResponse-levelIntensity: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## totalIntensity

```TypeScript
totalIntensity: double
```

总磁场强度，即地磁场三维空间的总强度。单位：nT（纳特斯拉）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GeomagneticResponse-totalIntensity: double--><!--Device-GeomagneticResponse-totalIntensity: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## x

```TypeScript
x: double
```

地磁场X方向分量（北分量）。单位：nT（纳特斯拉）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GeomagneticResponse-x: double--><!--Device-GeomagneticResponse-x: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## y

```TypeScript
y: double
```

地磁场Y方向分量（东分量）。单位：nT（纳特斯拉）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GeomagneticResponse-y: double--><!--Device-GeomagneticResponse-y: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## z

```TypeScript
z: double
```

地磁场Z方向分量（垂直分量）。单位：nT（纳特斯拉）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-GeomagneticResponse-z: double--><!--Device-GeomagneticResponse-z: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

