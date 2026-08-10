# GetLocationTypeOption

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

<!--Device-unnamed-export interface GetLocationTypeOption--><!--Device-unnamed-export interface GetLocationTypeOption-End-->

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

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-GetLocationTypeOption-complete?: () => void--><!--Device-GetLocationTypeOption-complete?: () => void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Called when the location types fail to be obtained.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-GetLocationTypeOption-fail?: (data: string, code: number) => void--><!--Device-GetLocationTypeOption-fail?: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 |  |
| code | number | 是 |  |

## success

```TypeScript
success?: (data: GetLocationTypeResponse) => void
```

Called when the location types are obtained.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-GetLocationTypeOption-success?: (data: GetLocationTypeResponse) => void--><!--Device-GetLocationTypeOption-success?: (data: GetLocationTypeResponse) => void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [GetLocationTypeResponse](arkts-location-system-geolocation-getlocationtyperesponse-i.md) | 是 |  |

