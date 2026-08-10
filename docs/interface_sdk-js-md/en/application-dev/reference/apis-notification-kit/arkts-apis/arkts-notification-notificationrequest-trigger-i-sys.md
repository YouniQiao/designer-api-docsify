# Trigger (System API)

触发条件的具体信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface Trigger--><!--Device-unnamed-export interface Trigger-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## condition

```TypeScript
condition:Geofence
```

条件具体描述。

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

条件触发实况的展示时间，单位：秒，取值范围：[15, 1800]，默认值为900。

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

条件类型。

**Type:** [TriggerType](arkts-notification-notificationmanager-triggertype-t-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Trigger-type:TriggerType--><!--Device-Trigger-type:TriggerType-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

