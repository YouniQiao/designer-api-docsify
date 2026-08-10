# SatelliteStatusInfo

Satellite status information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-export interface SatelliteStatusInfo--><!--Device-geoLocationManager-export interface SatelliteStatusInfo-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## altitudes

```TypeScript
altitudes: Array<double>
```

Satellite altitude array.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SatelliteStatusInfo-altitudes: Array<double>--><!--Device-SatelliteStatusInfo-altitudes: Array<double>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## azimuths

```TypeScript
azimuths: Array<double>
```

Satellite azimuth array.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SatelliteStatusInfo-azimuths: Array<double>--><!--Device-SatelliteStatusInfo-azimuths: Array<double>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## carrierFrequencies

```TypeScript
carrierFrequencies: Array<double>
```

Satellite carrier frequency array.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SatelliteStatusInfo-carrierFrequencies: Array<double>--><!--Device-SatelliteStatusInfo-carrierFrequencies: Array<double>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## carrierToNoiseDensitys

```TypeScript
carrierToNoiseDensitys: Array<double>
```

Carrier to noise density array.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SatelliteStatusInfo-carrierToNoiseDensitys: Array<double>--><!--Device-SatelliteStatusInfo-carrierToNoiseDensitys: Array<double>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## satelliteAdditionalInfo

```TypeScript
satelliteAdditionalInfo?: Array<int>
```

Satellite additional information array.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SatelliteStatusInfo-satelliteAdditionalInfo?: Array<int>--><!--Device-SatelliteStatusInfo-satelliteAdditionalInfo?: Array<int>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## satelliteConstellation

```TypeScript
satelliteConstellation?: Array<SatelliteConstellationCategory>
```

Satellite constellation type array.

**Type:** Array&lt;SatelliteConstellationCategory&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SatelliteStatusInfo-satelliteConstellation?: Array<SatelliteConstellationCategory>--><!--Device-SatelliteStatusInfo-satelliteConstellation?: Array<SatelliteConstellationCategory>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## satelliteIds

```TypeScript
satelliteIds: Array<int>
```

Satellite ID array.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SatelliteStatusInfo-satelliteIds: Array<int>--><!--Device-SatelliteStatusInfo-satelliteIds: Array<int>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## satellitesNumber

```TypeScript
satellitesNumber: int
```

Number of satellites.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SatelliteStatusInfo-satellitesNumber: int--><!--Device-SatelliteStatusInfo-satellitesNumber: int-End-->

**System capability:** SystemCapability.Location.Location.Gnss

