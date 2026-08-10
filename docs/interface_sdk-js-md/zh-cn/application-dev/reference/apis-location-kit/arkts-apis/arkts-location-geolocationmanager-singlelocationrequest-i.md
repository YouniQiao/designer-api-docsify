# SingleLocationRequest

Configuring parameters in single location requests.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface SingleLocationRequest--><!--Device-geoLocationManager-export interface SingleLocationRequest-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## locatingPriority

```TypeScript
locatingPriority: LocatingPriority
```

Priority of the location request.

**类型：** [LocatingPriority](arkts-location-geolocationmanager-locatingpriority-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-SingleLocationRequest-locatingPriority: LocatingPriority--><!--Device-SingleLocationRequest-locatingPriority: LocatingPriority-End-->

**系统能力：** SystemCapability.Location.Location.Core

## locatingTimeoutMs

```TypeScript
locatingTimeoutMs: int
```

Timeout of a single location request, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-SingleLocationRequest-locatingTimeoutMs: int--><!--Device-SingleLocationRequest-locatingTimeoutMs: int-End-->

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

<!--Device-SingleLocationRequest-needPoi?: boolean--><!--Device-SingleLocationRequest-needPoi?: boolean-End-->

**系统能力：** SystemCapability.Location.Location.Core

