# DistrictRequestParams

Indicates request parameters for obtaining the district information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**System capability:** SystemCapability.Location.Location.Geocoder

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## locale

```TypeScript
locale?: string
```

Indicates the language area information. ISO 639 alpha-2 or alpha-3 language code. Example: "zh" (Chinese), "en" (English). The default value is obtained from the language settings of the device (settings/system/Language & region /Language).

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Location.Location.Geocoder

## timeoutMs

```TypeScript
timeoutMs?: int
```

Indicates the timeout period. The default value is 5000 ms. The value range is all integers.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Location.Location.Geocoder
