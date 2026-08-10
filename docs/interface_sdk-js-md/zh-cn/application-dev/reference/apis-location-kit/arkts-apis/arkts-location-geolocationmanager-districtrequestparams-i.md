# DistrictRequestParams

Indicates request parameters for obtaining the district information.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

<!--Device-geoLocationManager-export interface DistrictRequestParams--><!--Device-geoLocationManager-export interface DistrictRequestParams-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## locale

```TypeScript
locale?: string
```

Indicates the language area information.ISO 639 alpha-2 or alpha-3 language code.Example: "zh" (Chinese), "en" (English).The default value is obtained from the language settings of the device (settings/system/Language & region/Language).

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-DistrictRequestParams-locale?: string--><!--Device-DistrictRequestParams-locale?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## timeoutMs

```TypeScript
timeoutMs?: int
```

Indicates the timeout period.The default value is 5000 ms.The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-DistrictRequestParams-timeoutMs?: int--><!--Device-DistrictRequestParams-timeoutMs?: int-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

