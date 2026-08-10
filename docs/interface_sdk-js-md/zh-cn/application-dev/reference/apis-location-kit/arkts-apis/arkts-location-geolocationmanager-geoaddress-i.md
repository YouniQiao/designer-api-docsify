# GeoAddress

Data struct describes geographic locations.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface GeoAddress--><!--Device-geoLocationManager-export interface GeoAddress-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## addressUrl

```TypeScript
addressUrl?: string
```

Indicates website URL.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-addressUrl?: string--><!--Device-GeoAddress-addressUrl?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## administrativeArea

```TypeScript
administrativeArea?: string
```

Indicates administrative region name.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-administrativeArea?: string--><!--Device-GeoAddress-administrativeArea?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## countryCode

```TypeScript
countryCode?: string
```

Indicates country code.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-countryCode?: string--><!--Device-GeoAddress-countryCode?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## countryName

```TypeScript
countryName?: string
```

Indicates country name.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-countryName?: string--><!--Device-GeoAddress-countryName?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## descriptions

```TypeScript
descriptions?: Array<string>
```

Indicates additional information.

**类型：** Array&lt;string&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-descriptions?: Array<string>--><!--Device-GeoAddress-descriptions?: Array<string>-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## descriptionsSize

```TypeScript
descriptionsSize?: int
```

Indicates the amount of additional descriptive information.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-descriptionsSize?: int--><!--Device-GeoAddress-descriptionsSize?: int-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## latitude

```TypeScript
latitude?: double
```

Indicates latitude information.A positive value indicates north latitude,and a negative value indicates south latitude.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-latitude?: double--><!--Device-GeoAddress-latitude?: double-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## locale

```TypeScript
locale?: string
```

Indicates language used for the location description.zh indicates Chinese, and en indicates English.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-locale?: string--><!--Device-GeoAddress-locale?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## locality

```TypeScript
locality?: string
```

Indicates locality information.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-locality?: string--><!--Device-GeoAddress-locality?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## longitude

```TypeScript
longitude?: double
```

Indicates longitude information.A positive value indicates east longitude ,and a negative value indicates west longitude.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-longitude?: double--><!--Device-GeoAddress-longitude?: double-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## phoneNumber

```TypeScript
phoneNumber?: string
```

Indicates phone number.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-phoneNumber?: string--><!--Device-GeoAddress-phoneNumber?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## placeName

```TypeScript
placeName?: string
```

Indicates detailed address information.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-placeName?: string--><!--Device-GeoAddress-placeName?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## postalCode

```TypeScript
postalCode?: string
```

Indicates postal code.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-postalCode?: string--><!--Device-GeoAddress-postalCode?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## premises

```TypeScript
premises?: string
```

Indicates house information.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-premises?: string--><!--Device-GeoAddress-premises?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## roadName

```TypeScript
roadName?: string
```

Indicates road name.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-roadName?: string--><!--Device-GeoAddress-roadName?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## subAdministrativeArea

```TypeScript
subAdministrativeArea?: string
```

Indicates sub-administrative region name.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-subAdministrativeArea?: string--><!--Device-GeoAddress-subAdministrativeArea?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## subLocality

```TypeScript
subLocality?: string
```

Indicates sub-locality information.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-subLocality?: string--><!--Device-GeoAddress-subLocality?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## subRoadName

```TypeScript
subRoadName?: string
```

Indicates auxiliary road information.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoAddress-subRoadName?: string--><!--Device-GeoAddress-subRoadName?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

