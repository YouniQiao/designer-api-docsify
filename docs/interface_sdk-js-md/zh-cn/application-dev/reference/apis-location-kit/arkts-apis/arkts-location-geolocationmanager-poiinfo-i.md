# PoiInfo

Describes the POI information struct.

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface PoiInfo--><!--Device-geoLocationManager-export interface PoiInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## poiArray

```TypeScript
poiArray: Array<Poi>
```

Indicates POI information list.

**类型：** Array&lt;Poi&gt;

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PoiInfo-poiArray: Array<Poi>--><!--Device-PoiInfo-poiArray: Array<Poi>-End-->

**系统能力：** SystemCapability.Location.Location.Core

## timestamp

```TypeScript
timestamp: long
```

Indicates the timestamp when the POI information is obtained.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PoiInfo-timestamp: long--><!--Device-PoiInfo-timestamp: long-End-->

**系统能力：** SystemCapability.Location.Location.Core

