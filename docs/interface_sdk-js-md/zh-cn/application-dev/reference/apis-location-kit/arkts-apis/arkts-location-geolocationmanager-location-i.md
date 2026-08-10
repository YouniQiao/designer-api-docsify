# Location

Provides information about geographic locations.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface Location--><!--Device-geoLocationManager-export interface Location-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## accuracy

```TypeScript
accuracy: double
```

Indicates location accuracy, in meters.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-accuracy: double--><!--Device-Location-accuracy: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## additionSize

```TypeScript
additionSize?: int
```

Indicates the amount of additional descriptive information.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-additionSize?: int--><!--Device-Location-additionSize?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

## additions

```TypeScript
additions?: Array<string>
```

Indicates additional information.

**类型：** Array&lt;string&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-additions?: Array<string>--><!--Device-Location-additions?: Array<string>-End-->

**系统能力：** SystemCapability.Location.Location.Core

## additionsMap

```TypeScript
additionsMap?: Map<string, string>
```

Indicates additional information map.

**类型：** Map&lt;string, string&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Location-additionsMap?: Map<string, string>--><!--Device-Location-additionsMap?: Map<string, string>-End-->

**系统能力：** SystemCapability.Location.Location.Core

## altitude

```TypeScript
altitude: double
```

Indicates location altitude, in meters.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-altitude: double--><!--Device-Location-altitude: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## altitudeAccuracy

```TypeScript
altitudeAccuracy?: double
```

Indicates vertical position accuracy in meters.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Location-altitudeAccuracy?: double--><!--Device-Location-altitudeAccuracy?: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## direction

```TypeScript
direction: double
```

Indicates direction information.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-direction: double--><!--Device-Location-direction: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## directionAccuracy

```TypeScript
directionAccuracy?: double
```

Indicates direction accuracy in degrees.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Location-directionAccuracy?: double--><!--Device-Location-directionAccuracy?: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## isFromMock

```TypeScript
isFromMock?: boolean
```

Indicates whether the location is mocked.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Location-isFromMock?: boolean--><!--Device-Location-isFromMock?: boolean-End-->

**系统能力：** SystemCapability.Location.Location.Core

## latitude

```TypeScript
latitude: double
```

Indicates latitude information.A positive value indicates north latitude,and a negative value indicates south latitude.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-latitude: double--><!--Device-Location-latitude: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## longitude

```TypeScript
longitude: double
```

Indicates Longitude information.A positive value indicates east longitude ,and a negative value indicates west longitude.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-longitude: double--><!--Device-Location-longitude: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## poi

```TypeScript
poi?: PoiInfo
```

Indicates the poi information.

**类型：** [PoiInfo](arkts-location-geolocationmanager-poiinfo-i.md)

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Location-poi?: PoiInfo--><!--Device-Location-poi?: PoiInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

## sourceType

```TypeScript
sourceType?: LocationSourceType
```

Indicates the source of the location.

**类型：** [LocationSourceType](arkts-location-geolocationmanager-locationsourcetype-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Location-sourceType?: LocationSourceType--><!--Device-Location-sourceType?: LocationSourceType-End-->

**系统能力：** SystemCapability.Location.Location.Core

## speed

```TypeScript
speed: double
```

Indicates speed, in m/s.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-speed: double--><!--Device-Location-speed: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## speedAccuracy

```TypeScript
speedAccuracy?: double
```

Indicates speed accuracy in meter per seconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Location-speedAccuracy?: double--><!--Device-Location-speedAccuracy?: double-End-->

**系统能力：** SystemCapability.Location.Location.Core

## timeSinceBoot

```TypeScript
timeSinceBoot: long
```

Indicates location timestamp since boot.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-timeSinceBoot: long--><!--Device-Location-timeSinceBoot: long-End-->

**系统能力：** SystemCapability.Location.Location.Core

## timeStamp

```TypeScript
timeStamp: long
```

Indicates location timestamp in the UTC format.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Location-timeStamp: long--><!--Device-Location-timeStamp: long-End-->

**系统能力：** SystemCapability.Location.Location.Core

## uncertaintyOfTimeSinceBoot

```TypeScript
uncertaintyOfTimeSinceBoot?: long
```

Time uncertainty Of timeSinceBoot in nanosecond.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Location-uncertaintyOfTimeSinceBoot?: long--><!--Device-Location-uncertaintyOfTimeSinceBoot?: long-End-->

**系统能力：** SystemCapability.Location.Location.Core

