# Location

Provides information about geographic locations.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-export interface Location--><!--Device-geoLocationManager-export interface Location-End-->

**System capability:** SystemCapability.Location.Location.Core

## accuracy

```TypeScript
accuracy: double
```

Indicates location accuracy, in meters.

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-accuracy: double--><!--Device-Location-accuracy: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## additionSize

```TypeScript
additionSize?: int
```

Indicates the amount of additional descriptive information.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-additionSize?: int--><!--Device-Location-additionSize?: int-End-->

**System capability:** SystemCapability.Location.Location.Core

## additions

```TypeScript
additions?: Array<string>
```

Indicates additional information.

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-additions?: Array<string>--><!--Device-Location-additions?: Array<string>-End-->

**System capability:** SystemCapability.Location.Location.Core

## additionsMap

```TypeScript
additionsMap?: Map<string, string>
```

Indicates additional information map.

**Type:** Map&lt;string, string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Location-additionsMap?: Map<string, string>--><!--Device-Location-additionsMap?: Map<string, string>-End-->

**System capability:** SystemCapability.Location.Location.Core

## altitude

```TypeScript
altitude: double
```

Indicates location altitude, in meters.

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-altitude: double--><!--Device-Location-altitude: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## altitudeAccuracy

```TypeScript
altitudeAccuracy?: double
```

Indicates vertical position accuracy in meters.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Location-altitudeAccuracy?: double--><!--Device-Location-altitudeAccuracy?: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## direction

```TypeScript
direction: double
```

Indicates direction information.

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-direction: double--><!--Device-Location-direction: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## directionAccuracy

```TypeScript
directionAccuracy?: double
```

Indicates direction accuracy in degrees.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Location-directionAccuracy?: double--><!--Device-Location-directionAccuracy?: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## isFromMock

```TypeScript
isFromMock?: boolean
```

Indicates whether the location is mocked.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Location-isFromMock?: boolean--><!--Device-Location-isFromMock?: boolean-End-->

**System capability:** SystemCapability.Location.Location.Core

## latitude

```TypeScript
latitude: double
```

Indicates latitude information.A positive value indicates north latitude,and a negative value indicates south latitude.

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-latitude: double--><!--Device-Location-latitude: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## longitude

```TypeScript
longitude: double
```

Indicates Longitude information.A positive value indicates east longitude ,and a negative value indicates west longitude.

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-longitude: double--><!--Device-Location-longitude: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## poi

```TypeScript
poi?: PoiInfo
```

Indicates the poi information.

**Type:** PoiInfo

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Location-poi?: PoiInfo--><!--Device-Location-poi?: PoiInfo-End-->

**System capability:** SystemCapability.Location.Location.Core

## sourceType

```TypeScript
sourceType?: LocationSourceType
```

Indicates the source of the location.

**Type:** LocationSourceType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Location-sourceType?: LocationSourceType--><!--Device-Location-sourceType?: LocationSourceType-End-->

**System capability:** SystemCapability.Location.Location.Core

## speed

```TypeScript
speed: double
```

Indicates speed, in m/s.

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-speed: double--><!--Device-Location-speed: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## speedAccuracy

```TypeScript
speedAccuracy?: double
```

Indicates speed accuracy in meter per seconds.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Location-speedAccuracy?: double--><!--Device-Location-speedAccuracy?: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## timeSinceBoot

```TypeScript
timeSinceBoot: long
```

Indicates location timestamp since boot.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-timeSinceBoot: long--><!--Device-Location-timeSinceBoot: long-End-->

**System capability:** SystemCapability.Location.Location.Core

## timeStamp

```TypeScript
timeStamp: long
```

Indicates location timestamp in the UTC format.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-timeStamp: long--><!--Device-Location-timeStamp: long-End-->

**System capability:** SystemCapability.Location.Location.Core

## uncertaintyOfTimeSinceBoot

```TypeScript
uncertaintyOfTimeSinceBoot?: long
```

Time uncertainty Of timeSinceBoot in nanosecond.

**Type:** long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Location-uncertaintyOfTimeSinceBoot?: long--><!--Device-Location-uncertaintyOfTimeSinceBoot?: long-End-->

**System capability:** SystemCapability.Location.Location.Core

