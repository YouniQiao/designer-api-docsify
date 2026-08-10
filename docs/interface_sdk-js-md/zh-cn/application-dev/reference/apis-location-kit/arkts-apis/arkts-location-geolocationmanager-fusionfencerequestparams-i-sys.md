# FusionFenceRequestParams（系统接口）

Indicates fusion fence request params.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

<!--Device-geoLocationManager-export interface FusionFenceRequestParams--><!--Device-geoLocationManager-export interface FusionFenceRequestParams-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## cellFences

```TypeScript
cellFences?: Array<CellFence>
```

Indicates CELL fence array.

**类型：** Array&lt;CellFence&gt;

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-cellFences?: Array<CellFence>--><!--Device-FusionFenceRequestParams-cellFences?: Array<CellFence>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## expirationMs

```TypeScript
expirationMs: double
```

Indicates expiration of the circular fence.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-expirationMs: double--><!--Device-FusionFenceRequestParams-expirationMs: double-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## fenceTransitionCallback

```TypeScript
fenceTransitionCallback: Callback<FusionFenceTransition>
```

Indicates the callback for reporting the fence transition status.

**类型：** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FusionFenceTransition&gt;

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-fenceTransitionCallback: Callback<FusionFenceTransition>--><!--Device-FusionFenceRequestParams-fenceTransitionCallback: Callback<FusionFenceTransition>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## fenceType

```TypeScript
fenceType: int
```

Indicates fusion fence type.This field is in bitmap format. Multiple types of fences can be transferred.The definition of each bit is as follows: [FusionFenceType](arkts-location-geolocationmanager-fusionfencetype-e-sys.md).The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-fenceType: int--><!--Device-FusionFenceRequestParams-fenceType: int-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## gnssFences

```TypeScript
gnssFences?: Array<GnssFence>
```

Indicates GNSS fence array.

**类型：** Array&lt;GnssFence&gt;

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-gnssFences?: Array<GnssFence>--><!--Device-FusionFenceRequestParams-gnssFences?: Array<GnssFence>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## identifier

```TypeScript
identifier: string
```

Identifier of the fusion fence.The string format should be a valid unique identifier (e.g., GUID or specific alphanumeric pattern).

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-identifier: string--><!--Device-FusionFenceRequestParams-identifier: string-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## loiterTimeMs

```TypeScript
loiterTimeMs: int
```

Indicates time for which a device is dwelling in the geofence, in milliseconds.If the device dwelling time reaches the value specified by this parameter,a GEOFENCE_TRANSITION_EVENT_DWELL event is reported.The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-loiterTimeMs: int--><!--Device-FusionFenceRequestParams-loiterTimeMs: int-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## monitorTransitionEvents

```TypeScript
monitorTransitionEvents: int
```

Indicates geofence transition status monitored.This field is in bitmap format.The definition of each bit is as follows {@link geoLocationManager.GeofenceTransitionEvent}.The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-monitorTransitionEvents: int--><!--Device-FusionFenceRequestParams-monitorTransitionEvents: int-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## poiLocation

```TypeScript
poiLocation: Point
```

Indicates the location of POI.

**类型：** [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-poiLocation: Point--><!--Device-FusionFenceRequestParams-poiLocation: Point-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## poiType

```TypeScript
poiType?: string
```

Indicates the type of POI.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-poiType?: string--><!--Device-FusionFenceRequestParams-poiType?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## scene

```TypeScript
scene: FusionFenceScene
```

Indicates fusion fence scene.

**类型：** [FusionFenceScene](arkts-location-geolocationmanager-fusionfencescene-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-scene: FusionFenceScene--><!--Device-FusionFenceRequestParams-scene: FusionFenceScene-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## wifiFences

```TypeScript
wifiFences?: Array<WifiFence>
```

Indicates Wi-Fi fence array.

**类型：** Array&lt;WifiFence&gt;

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FusionFenceRequestParams-wifiFences?: Array<WifiFence>--><!--Device-FusionFenceRequestParams-wifiFences?: Array<WifiFence>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

