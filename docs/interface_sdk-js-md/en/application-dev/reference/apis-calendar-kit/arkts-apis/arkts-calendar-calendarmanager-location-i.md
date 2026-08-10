# Location

日程地点。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-calendarManager-interface Location--><!--Device-calendarManager-interface Location-End-->

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## latitude

```TypeScript
latitude?: number
```

地点纬度。取值范围[-90, 90]，默认为undefined。超过取值范围地图将无法正常显示。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-latitude?: number--><!--Device-Location-latitude?: number-End-->

**System capability:** SystemCapability.Applications.CalendarData

## location

```TypeScript
location?: string
```

日程地点。不填时，默认为undefined。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-location?: string--><!--Device-Location-location?: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## longitude

```TypeScript
longitude?: number
```

地点经度。取值范围[-180, 180]，默认为undefined。超过取值范围地图将无法正常显示。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Location-longitude?: number--><!--Device-Location-longitude?: number-End-->

**System capability:** SystemCapability.Applications.CalendarData

