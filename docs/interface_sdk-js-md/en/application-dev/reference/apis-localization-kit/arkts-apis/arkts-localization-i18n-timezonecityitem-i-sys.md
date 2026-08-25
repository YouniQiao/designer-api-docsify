# TimeZoneCityItem (System API)

Represents a time zone and city combination item.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## cityDisplayName

```TypeScript
cityDisplayName: string
```

City display name in the system locale.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## cityId

```TypeScript
cityId: string
```

City ID, for example, "Shanghai".

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## latitude

```TypeScript
latitude: double
```

Latitude info of time zone city in decimal degrees (°).

**Type:** number

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## longitude

```TypeScript
longitude: double
```

Longitude info of time zone city in decimal degrees (°).

**Type:** number

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## offset

```TypeScript
offset: int
```

Offset of the time zone ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## rawOffset

```TypeScript
rawOffset?: int
```

Fixed offset of the time zone ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## zoneDisplayName

```TypeScript
zoneDisplayName: string
```

Time zone display name in the system locale.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## zoneId

```TypeScript
zoneId: string
```

Time zone ID, for example, "Asia/Shanghai".

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.
