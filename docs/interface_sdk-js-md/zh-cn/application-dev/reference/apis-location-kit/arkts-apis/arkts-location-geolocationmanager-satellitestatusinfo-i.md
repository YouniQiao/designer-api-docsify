# SatelliteStatusInfo

Satellite status information.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface SatelliteStatusInfo--><!--Device-geoLocationManager-export interface SatelliteStatusInfo-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## altitudes

```TypeScript
altitudes: Array<double>
```

Satellite altitude array.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-SatelliteStatusInfo-altitudes: Array<double>--><!--Device-SatelliteStatusInfo-altitudes: Array<double>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## azimuths

```TypeScript
azimuths: Array<double>
```

Satellite azimuth array.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-SatelliteStatusInfo-azimuths: Array<double>--><!--Device-SatelliteStatusInfo-azimuths: Array<double>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## carrierFrequencies

```TypeScript
carrierFrequencies: Array<double>
```

Satellite carrier frequency array.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-SatelliteStatusInfo-carrierFrequencies: Array<double>--><!--Device-SatelliteStatusInfo-carrierFrequencies: Array<double>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## carrierToNoiseDensitys

```TypeScript
carrierToNoiseDensitys: Array<double>
```

Carrier to noise density array.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-SatelliteStatusInfo-carrierToNoiseDensitys: Array<double>--><!--Device-SatelliteStatusInfo-carrierToNoiseDensitys: Array<double>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## satelliteAdditionalInfo

```TypeScript
satelliteAdditionalInfo?: Array<int>
```

Satellite additional information array.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-SatelliteStatusInfo-satelliteAdditionalInfo?: Array<int>--><!--Device-SatelliteStatusInfo-satelliteAdditionalInfo?: Array<int>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## satelliteConstellation

```TypeScript
satelliteConstellation?: Array<SatelliteConstellationCategory>
```

Satellite constellation type array.

**类型：** Array&lt;SatelliteConstellationCategory&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-SatelliteStatusInfo-satelliteConstellation?: Array<SatelliteConstellationCategory>--><!--Device-SatelliteStatusInfo-satelliteConstellation?: Array<SatelliteConstellationCategory>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## satelliteIds

```TypeScript
satelliteIds: Array<int>
```

Satellite ID array.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-SatelliteStatusInfo-satelliteIds: Array<int>--><!--Device-SatelliteStatusInfo-satelliteIds: Array<int>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## satellitesNumber

```TypeScript
satellitesNumber: int
```

Number of satellites.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-SatelliteStatusInfo-satellitesNumber: int--><!--Device-SatelliteStatusInfo-satellitesNumber: int-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

