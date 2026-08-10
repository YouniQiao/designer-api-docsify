# Geolocation

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager

<!--Device-unnamed-export default class Geolocation--><!--Device-unnamed-export default class Geolocation-End-->

**系统能力：** SystemCapability.Location.Location.Lite

## 导入模块

```TypeScript
import { GetLocationTypeOption, SubscribeLocationOption, GeolocationResponse, GetLocationTypeResponse, GetLocationOption } from 'kits/@kit.LocationKit';
```

## getLocation

```TypeScript
static getLocation(options?: GetLocationOption): void
```

Obtains the geographic location.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCurrentLocation

**需要权限：** ohos.permission.LOCATION

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Geolocation-static getLocation(options?: GetLocationOption): void--><!--Device-Geolocation-static getLocation(options?: GetLocationOption): void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetLocationOption](arkts-location-system-geolocation-getlocationoption-i.md) | 否 |  |

## getLocationType

```TypeScript
static getLocationType(options?: GetLocationTypeOption): void
```

Obtains the location types supported by the system.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Geolocation-static getLocationType(options?: GetLocationTypeOption): void--><!--Device-Geolocation-static getLocationType(options?: GetLocationTypeOption): void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetLocationTypeOption](arkts-location-system-geolocation-getlocationtypeoption-i.md) | 否 |  |

## getSupportedCoordTypes

```TypeScript
static getSupportedCoordTypes(): Array<string>
```

Obtains the supported coordinate system types.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Geolocation-static getSupportedCoordTypes(): Array<string>--><!--Device-Geolocation-static getSupportedCoordTypes(): Array<string>-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; |  |

## subscribe

```TypeScript
static subscribe(options: SubscribeLocationOption): void
```

Listens to the geographical location. If this method is called multiple times, the last call takes effect.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.on#event:locationChange

**需要权限：** ohos.permission.LOCATION

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Geolocation-static subscribe(options: SubscribeLocationOption): void--><!--Device-Geolocation-static subscribe(options: SubscribeLocationOption): void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeLocationOption](arkts-location-system-geolocation-subscribelocationoption-i.md) | 是 |  |

## unsubscribe

```TypeScript
static unsubscribe(): void
```

Cancels listening to the geographical location.

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.off#event:locationChange

**需要权限：** ohos.permission.LOCATION

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Geolocation-static unsubscribe(): void--><!--Device-Geolocation-static unsubscribe(): void-End-->

**系统能力：** SystemCapability.Location.Location.Lite

