# GetLocationOption

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.CurrentLocationRequest

**需要权限：** ohos.permission.LOCATION

<!--Device-unnamed-export interface GetLocationOption--><!--Device-unnamed-export interface GetLocationOption-End-->

**系统能力：** SystemCapability.Location.Location.Lite

## 导入模块

```TypeScript
import { GetLocationTypeOption, SubscribeLocationOption, GeolocationResponse, GetLocationTypeResponse, GetLocationOption } from 'kits/@kit.LocationKit';
```

## complete

```TypeScript
complete?: () => void
```

Called when the execution is completed.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCurrentLocation#callback

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-GetLocationOption-complete?: () => void--><!--Device-GetLocationOption-complete?: () => void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Called when the location types fail to be obtained

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCurrentLocation#callback

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-GetLocationOption-fail?: (data: string, code: number) => void--><!--Device-GetLocationOption-fail?: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 |  |
| code | number | 是 |  |

## success

```TypeScript
success?: (data: GeolocationResponse) => void
```

Called when the geographic location is obtained.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCurrentLocation#callback

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-GetLocationOption-success?: (data: GeolocationResponse) => void--><!--Device-GetLocationOption-success?: (data: GeolocationResponse) => void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [GeolocationResponse](arkts-location-system-geolocation-geolocationresponse-i.md) | 是 |  |

## coordType

```TypeScript
coordType?: string
```

Coordinate system type. Available types can be obtained using getSupportedCoordTypes.The default type is wgs84.

**类型：** string

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-GetLocationOption-coordType?: string--><!--Device-GetLocationOption-coordType?: string-End-->

**系统能力：** SystemCapability.Location.Location.Lite

## timeout

```TypeScript
timeout?: number
```

Timeout duration, in milliseconds.For the rich device, the default value is 30000.For the lite wearable device, the default value is 180000.The timeout duration is necessary in case no result is returned if the request to obtain the geographic location is rejected for the lack of the required permission, weak positioning signal, or incorrect location settings. After the timeout duration expires, the fail function will be called.The value is a 32-digit positive integer.If the value set is less than or equal to 0, the default value will be used.

**类型：** number

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.CurrentLocationRequest#timeoutMs

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-GetLocationOption-timeout?: number--><!--Device-GetLocationOption-timeout?: number-End-->

**系统能力：** SystemCapability.Location.Location.Lite

