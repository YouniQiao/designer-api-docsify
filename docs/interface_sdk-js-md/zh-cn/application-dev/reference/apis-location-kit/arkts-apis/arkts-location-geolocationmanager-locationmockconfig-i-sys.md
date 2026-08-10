# LocationMockConfig（系统接口）

Parameters for configuring the location simulation function.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface LocationMockConfig--><!--Device-geoLocationManager-export interface LocationMockConfig-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## locations

```TypeScript
locations: Array<Location>
```

Mock location array.

**类型：** Array&lt;Location&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-LocationMockConfig-locations: Array<Location>--><!--Device-LocationMockConfig-locations: Array<Location>-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## timeInterval

```TypeScript
timeInterval: int
```

Interval for reporting simulated locations.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-LocationMockConfig-timeInterval: int--><!--Device-LocationMockConfig-timeInterval: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

