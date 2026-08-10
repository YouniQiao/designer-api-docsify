# LocationRequest

Configuring parameters in location requests.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface LocationRequest--><!--Device-geoLocationManager-export interface LocationRequest-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## distanceInterval

```TypeScript
distanceInterval?: double
```

Location report distance interval.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocationRequest-distanceInterval?: double--><!--Device-LocationRequest-distanceInterval?: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## maxAccuracy

```TypeScript
maxAccuracy?: double
```

Accuracy requirements for reporting locations.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocationRequest-maxAccuracy?: double--><!--Device-LocationRequest-maxAccuracy?: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## priority

```TypeScript
priority?: LocationRequestPriority
```

Priority of the location request.

**类型：** [LocationRequestPriority](arkts-location-geolocation-locationrequestpriority-e.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocationRequest-priority?: LocationRequestPriority--><!--Device-LocationRequest-priority?: LocationRequestPriority-End-->

**系统能力：** SystemCapability.Location.Location.Core

## scenario

```TypeScript
scenario?: LocationRequestScenario
```

User scenario of the location request.

**类型：** [LocationRequestScenario](arkts-location-geolocationmanager-locationrequestscenario-e.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocationRequest-scenario?: LocationRequestScenario--><!--Device-LocationRequest-scenario?: LocationRequestScenario-End-->

**系统能力：** SystemCapability.Location.Location.Core

## timeInterval

```TypeScript
timeInterval?: int
```

Location report interval.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocationRequest-timeInterval?: int--><!--Device-LocationRequest-timeInterval?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

