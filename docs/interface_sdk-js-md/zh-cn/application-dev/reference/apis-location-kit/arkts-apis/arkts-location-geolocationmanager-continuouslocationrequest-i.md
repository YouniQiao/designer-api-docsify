# ContinuousLocationRequest

Configuring parameters in continuous location requests.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface ContinuousLocationRequest--><!--Device-geoLocationManager-export interface ContinuousLocationRequest-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## interval

```TypeScript
interval: int
```

Location report interval, in seconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ContinuousLocationRequest-interval: int--><!--Device-ContinuousLocationRequest-interval: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

## locationScenario

```TypeScript
locationScenario: UserActivityScenario | PowerConsumptionScenario
```

Location scenario. You can select a user activity scenario or power consumption scenario.

**类型：** [UserActivityScenario](arkts-location-geolocationmanager-useractivityscenario-e.md) \| PowerConsumptionScenario

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ContinuousLocationRequest-locationScenario: UserActivityScenario | PowerConsumptionScenario--><!--Device-ContinuousLocationRequest-locationScenario: UserActivityScenario | PowerConsumptionScenario-End-->

**系统能力：** SystemCapability.Location.Location.Core

## needPoi

```TypeScript
needPoi?: boolean
```

Indicates whether to obtain POI information near the current location.

**类型：** boolean

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-ContinuousLocationRequest-needPoi?: boolean--><!--Device-ContinuousLocationRequest-needPoi?: boolean-End-->

**系统能力：** SystemCapability.Location.Location.Core

## sportsType

```TypeScript
sportsType?: SportsType
```

Indicates the type of sports.This parameter is valid only when locationScenario is set to UserActivityScenario.SPORT.

**类型：** [SportsType](arkts-location-geolocationmanager-sportstype-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ContinuousLocationRequest-sportsType?: SportsType--><!--Device-ContinuousLocationRequest-sportsType?: SportsType-End-->

**系统能力：** SystemCapability.Location.Location.Core

