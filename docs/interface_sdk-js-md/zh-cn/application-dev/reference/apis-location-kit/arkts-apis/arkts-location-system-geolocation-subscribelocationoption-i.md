# SubscribeLocationOption

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.LocationRequest

**需要权限：** ohos.permission.LOCATION

<!--Device-unnamed-export interface SubscribeLocationOption--><!--Device-unnamed-export interface SubscribeLocationOption-End-->

**系统能力：** SystemCapability.Location.Location.Lite

## 导入模块

```TypeScript
import { GetLocationTypeOption, SubscribeLocationOption, GeolocationResponse, GetLocationTypeResponse, GetLocationOption } from 'kits/@kit.LocationKit';
```

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Called when the listening fails.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-SubscribeLocationOption-fail?: (data: string, code: number) => void--><!--Device-SubscribeLocationOption-fail?: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 |  |
| code | number | 是 |  |

## success

```TypeScript
success: (data: GeolocationResponse) => void
```

Called whenever the geographical location changes.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-SubscribeLocationOption-success: (data: GeolocationResponse) => void--><!--Device-SubscribeLocationOption-success: (data: GeolocationResponse) => void-End-->

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

<!--Device-SubscribeLocationOption-coordType?: string--><!--Device-SubscribeLocationOption-coordType?: string-End-->

**系统能力：** SystemCapability.Location.Location.Lite

