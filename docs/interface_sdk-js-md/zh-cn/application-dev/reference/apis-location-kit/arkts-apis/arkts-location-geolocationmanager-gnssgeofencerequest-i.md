# GnssGeofenceRequest

Configuring parameters in GNSS geofence requests.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface GnssGeofenceRequest--><!--Device-geoLocationManager-export interface GnssGeofenceRequest-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## fenceExtensionAbilityName

```TypeScript
fenceExtensionAbilityName?: string
```

Indicates the name of FenceExtensionAbility.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-GnssGeofenceRequest-fenceExtensionAbilityName?: string--><!--Device-GnssGeofenceRequest-fenceExtensionAbilityName?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## geofence

```TypeScript
geofence: Geofence
```

Circular fence information.

**类型：** [Geofence](arkts-location-geolocation-geofence-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-GnssGeofenceRequest-geofence: Geofence--><!--Device-GnssGeofenceRequest-geofence: Geofence-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## geofenceTransitionCallback

```TypeScript
geofenceTransitionCallback: AsyncCallback<GeofenceTransition>
```

Indicates the callback for reporting the geofence transition status.

**类型：** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;GeofenceTransition&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-GnssGeofenceRequest-geofenceTransitionCallback: AsyncCallback<GeofenceTransition>--><!--Device-GnssGeofenceRequest-geofenceTransitionCallback: AsyncCallback<GeofenceTransition>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## loiterTimeMs

```TypeScript
loiterTimeMs?: int
```

Indicates time for which a device is dwelling in the geofence, in milliseconds.If the device dwelling time reaches the value specified by this parameter,a GEOFENCE_TRANSITION_EVENT_DWELL event is reported.The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-GnssGeofenceRequest-loiterTimeMs?: int--><!--Device-GnssGeofenceRequest-loiterTimeMs?: int-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## monitorTransitionEvents

```TypeScript
monitorTransitionEvents: Array<GeofenceTransitionEvent>
```

Indicates geofence transition status monitored.

**类型：** Array&lt;GeofenceTransitionEvent&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-GnssGeofenceRequest-monitorTransitionEvents: Array<GeofenceTransitionEvent>--><!--Device-GnssGeofenceRequest-monitorTransitionEvents: Array<GeofenceTransitionEvent>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## notifications

```TypeScript
notifications?: Array<NotificationRequest>
```

Indicates the geofence notifications to publish.

**类型：** Array&lt;[NotificationRequest](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationrequest-i.md)&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-GnssGeofenceRequest-notifications?: Array<NotificationRequest>--><!--Device-GnssGeofenceRequest-notifications?: Array<NotificationRequest>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

