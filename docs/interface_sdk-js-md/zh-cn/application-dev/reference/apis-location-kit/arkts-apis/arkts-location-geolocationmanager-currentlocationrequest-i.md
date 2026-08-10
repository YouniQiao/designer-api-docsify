# CurrentLocationRequest

Configuring parameters in current location requests.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface CurrentLocationRequest--><!--Device-geoLocationManager-export interface CurrentLocationRequest-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## maxAccuracy

```TypeScript
maxAccuracy?: double
```

Accuracy requirements for reporting locations.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CurrentLocationRequest-maxAccuracy?: double--><!--Device-CurrentLocationRequest-maxAccuracy?: double-End-->

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

<!--Device-CurrentLocationRequest-priority?: LocationRequestPriority--><!--Device-CurrentLocationRequest-priority?: LocationRequestPriority-End-->

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

<!--Device-CurrentLocationRequest-scenario?: LocationRequestScenario--><!--Device-CurrentLocationRequest-scenario?: LocationRequestScenario-End-->

**系统能力：** SystemCapability.Location.Location.Core

## timeoutMs

```TypeScript
timeoutMs?: int
```

Timeout interval of a single location request.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CurrentLocationRequest-timeoutMs?: int--><!--Device-CurrentLocationRequest-timeoutMs?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

