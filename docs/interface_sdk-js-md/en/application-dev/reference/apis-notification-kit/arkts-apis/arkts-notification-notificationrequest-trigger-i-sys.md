# Trigger (System API)

Defines the details for triggering a geofence.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface Trigger--><!--Device-unnamed-export interface Trigger-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## condition

```TypeScript
condition:Geofence
```

Details about a geofence.

**Type:** [Geofence](../../apis-location-kit/arkts-apis/arkts-location-geolocation-geofence-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Trigger-condition:Geofence--><!--Device-Trigger-condition:Geofence-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## displayTime

```TypeScript
displayTime?:int
```

Display time of a live view, in seconds. The value ranges from 15 to 1800. The default value is **900**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Trigger-displayTime?:int--><!--Device-Trigger-displayTime?:int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## type

```TypeScript
type:TriggerType
```

Trigger type.

**Type:** [TriggerType](arkts-notification-notificationmanager-triggertype-t-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Trigger-type:TriggerType--><!--Device-Trigger-type:TriggerType-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

