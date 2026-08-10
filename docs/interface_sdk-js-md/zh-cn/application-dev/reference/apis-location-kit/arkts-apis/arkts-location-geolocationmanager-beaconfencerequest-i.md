# BeaconFenceRequest

Configuring parameters in BeaconFence request.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.1.0。

<!--Device-geoLocationManager-export interface BeaconFenceRequest--><!--Device-geoLocationManager-export interface BeaconFenceRequest-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## beacon

```TypeScript
beacon: BeaconFence
```

Beacon fence information.

**类型：** [BeaconFence](arkts-location-geolocationmanager-beaconfence-i.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.1.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-BeaconFenceRequest-beacon: BeaconFence--><!--Device-BeaconFenceRequest-beacon: BeaconFence-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## fenceExtensionAbilityName

```TypeScript
fenceExtensionAbilityName?: string
```

Indicates the name of FenceExtensionAbility.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.1.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-BeaconFenceRequest-fenceExtensionAbilityName?: string--><!--Device-BeaconFenceRequest-fenceExtensionAbilityName?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

## transitionCallback

```TypeScript
transitionCallback?: Callback<GeofenceTransition>
```

Indicates the callback for reporting the BeaconFence transition status.

**类型：** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GeofenceTransition&gt;

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.1.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-BeaconFenceRequest-transitionCallback?: Callback<GeofenceTransition>--><!--Device-BeaconFenceRequest-transitionCallback?: Callback<GeofenceTransition>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

