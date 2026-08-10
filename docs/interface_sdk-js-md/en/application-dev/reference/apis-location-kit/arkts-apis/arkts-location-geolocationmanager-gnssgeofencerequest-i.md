# GnssGeofenceRequest

Configuring parameters in GNSS geofence requests.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-export interface GnssGeofenceRequest--><!--Device-geoLocationManager-export interface GnssGeofenceRequest-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## fenceExtensionAbilityName

```TypeScript
fenceExtensionAbilityName?: string
```

Indicates the name of FenceExtensionAbility.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-GnssGeofenceRequest-fenceExtensionAbilityName?: string--><!--Device-GnssGeofenceRequest-fenceExtensionAbilityName?: string-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## geofence

```TypeScript
geofence: Geofence
```

Circular fence information.

**Type:** [Geofence](arkts-location-geolocation-geofence-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GnssGeofenceRequest-geofence: Geofence--><!--Device-GnssGeofenceRequest-geofence: Geofence-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## geofenceTransitionCallback

```TypeScript
geofenceTransitionCallback: AsyncCallback<GeofenceTransition>
```

Indicates the callback for reporting the geofence transition status.

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;GeofenceTransition&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GnssGeofenceRequest-geofenceTransitionCallback: AsyncCallback<GeofenceTransition>--><!--Device-GnssGeofenceRequest-geofenceTransitionCallback: AsyncCallback<GeofenceTransition>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## loiterTimeMs

```TypeScript
loiterTimeMs?: int
```

Indicates time for which a device is dwelling in the geofence, in milliseconds.If the device dwelling time reaches the value specified by this parameter,a GEOFENCE_TRANSITION_EVENT_DWELL event is reported.The value should be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-GnssGeofenceRequest-loiterTimeMs?: int--><!--Device-GnssGeofenceRequest-loiterTimeMs?: int-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## monitorTransitionEvents

```TypeScript
monitorTransitionEvents: Array<GeofenceTransitionEvent>
```

Indicates geofence transition status monitored.

**Type:** Array&lt;GeofenceTransitionEvent&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GnssGeofenceRequest-monitorTransitionEvents: Array<GeofenceTransitionEvent>--><!--Device-GnssGeofenceRequest-monitorTransitionEvents: Array<GeofenceTransitionEvent>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## notifications

```TypeScript
notifications?: Array<NotificationRequest>
```

Indicates the geofence notifications to publish.

**Type:** Array&lt;[NotificationRequest](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationrequest-i.md)&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GnssGeofenceRequest-notifications?: Array<NotificationRequest>--><!--Device-GnssGeofenceRequest-notifications?: Array<NotificationRequest>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

