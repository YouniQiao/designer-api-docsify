# Geofence (System API)

地理围栏的配置信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface Geofence--><!--Device-unnamed-export interface Geofence-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## coordinateSystemType

```TypeScript
coordinateSystemType:CoordinateSystemType
```

中心点坐标系类型。

**Type:** [CoordinateSystemType](../../apis-location-kit/arkts-apis/arkts-location-geolocationmanager-coordinatesystemtype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Geofence-coordinateSystemType:CoordinateSystemType--><!--Device-Geofence-coordinateSystemType:CoordinateSystemType-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## delayTime

```TypeScript
delayTime?:int
```

围栏延迟时间，单位：秒，进入围栏后触发围栏的延迟时间，取值范围：[0, 300]。默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Geofence-delayTime?:int--><!--Device-Geofence-delayTime?:int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## latitude

```TypeScript
latitude:double
```

地理围栏中心点纬度，取值范围：[-90, 90]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Geofence-latitude:double--><!--Device-Geofence-latitude:double-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## longitude

```TypeScript
longitude:double
```

地理围栏中心点经度，取值范围：[-180, 180]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Geofence-longitude:double--><!--Device-Geofence-longitude:double-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## monitorEvent

```TypeScript
monitorEvent:MonitorEvent
```

围栏触发条件类型。

**Type:** [MonitorEvent](arkts-notification-notificationmanager-monitorevent-t-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Geofence-monitorEvent:MonitorEvent--><!--Device-Geofence-monitorEvent:MonitorEvent-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## radius

```TypeScript
radius:double
```

围栏半径，单位：米，取值范围：[200, 2000]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Geofence-radius:double--><!--Device-Geofence-radius:double-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

