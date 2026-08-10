# GeofenceTransition

Geofence transition status.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface GeofenceTransition--><!--Device-geoLocationManager-export interface GeofenceTransition-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## beaconFence

```TypeScript
beaconFence?: BeaconFence
```

Indicate the beaconFence which transitionEvent occurs.

**类型：** [BeaconFence](arkts-location-geolocationmanager-beaconfence-i.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-GeofenceTransition-beaconFence?: BeaconFence--><!--Device-GeofenceTransition-beaconFence?: BeaconFence-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## geofenceId

```TypeScript
geofenceId: int
```

ID of the geofence.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-GeofenceTransition-geofenceId: int--><!--Device-GeofenceTransition-geofenceId: int-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## transitionEvent

```TypeScript
transitionEvent: GeofenceTransitionEvent
```

Indicates the geofence transition status.

**类型：** [GeofenceTransitionEvent](arkts-location-geolocationmanager-geofencetransitionevent-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-GeofenceTransition-transitionEvent: GeofenceTransitionEvent--><!--Device-GeofenceTransition-transitionEvent: GeofenceTransitionEvent-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

