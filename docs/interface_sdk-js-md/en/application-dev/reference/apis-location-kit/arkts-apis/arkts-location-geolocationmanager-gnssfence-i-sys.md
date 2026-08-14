# GnssFence (System API)

Indicates GNSS fence information.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

<!--Device-geoLocationManager-export interface GnssFence--><!--Device-geoLocationManager-export interface GnssFence-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { geoLocationManager } from 'geoLocationManager';
```

## circularFence

```TypeScript
circularFence?: Geofence
```

Indicates circular fence.

**Type:** Geofence

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GnssFence-circularFence?: Geofence--><!--Device-GnssFence-circularFence?: Geofence-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**System API:** This is a system API.

## gnssFenceType

```TypeScript
gnssFenceType: int
```

Indicates GNSS fence type. The value range of this field is as follows: [GnssFenceType](arkts-location-geolocationmanager-gnssfencetype-e-sys.md#GnssFenceType-(System-API)). The value range is all integers.

**Type:** int

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GnssFence-gnssFenceType: int--><!--Device-GnssFence-gnssFenceType: int-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**System API:** This is a system API.

## polygon

```TypeScript
polygon?: Array<Point>
```

Indicates polygonal fence.

**Type:** Array&lt;Point&gt;

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GnssFence-polygon?: Array<Point>--><!--Device-GnssFence-polygon?: Array<Point>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**System API:** This is a system API.

