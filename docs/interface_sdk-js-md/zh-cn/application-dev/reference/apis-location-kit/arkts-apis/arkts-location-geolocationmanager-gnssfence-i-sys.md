# GnssFence（系统接口）

Indicates GNSS fence information.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

<!--Device-geoLocationManager-export interface GnssFence--><!--Device-geoLocationManager-export interface GnssFence-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## circularFence

```TypeScript
circularFence?: Geofence
```

Indicates circular fence.

**类型：** [Geofence](arkts-location-geolocation-geofence-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GnssFence-circularFence?: Geofence--><!--Device-GnssFence-circularFence?: Geofence-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## gnssFenceType

```TypeScript
gnssFenceType: int
```

Indicates GNSS fence type.The value range of this field is as follows: [GnssFenceType](arkts-location-geolocationmanager-gnssfencetype-e-sys.md).The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GnssFence-gnssFenceType: int--><!--Device-GnssFence-gnssFenceType: int-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## polygon

```TypeScript
polygon?: Array<Point>
```

Indicates polygonal fence.

**类型：** Array&lt;Point&gt;

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GnssFence-polygon?: Array<Point>--><!--Device-GnssFence-polygon?: Array<Point>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

