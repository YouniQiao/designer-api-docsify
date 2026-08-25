# getDistanceBetweenLocations

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getDistanceBetweenLocations

```TypeScript
function getDistanceBetweenLocations(location1: Location, location2: Location): number
```

获取两个位置之间的直线距离。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| location1 | [Location](arkts-location-geolocationmanager-location-i.md) | 是 |
| location2 | [Location](arkts-location-geolocationmanager-location-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |
