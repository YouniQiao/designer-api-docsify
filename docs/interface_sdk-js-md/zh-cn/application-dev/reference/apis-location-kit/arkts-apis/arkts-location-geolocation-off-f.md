# off

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## off('locationChange')

```TypeScript
function off(type: 'locationChange', callback?: Callback<Location>): void
```

关闭位置变化订阅，并删除对应的定位请求。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** locationChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'locationChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | 否 |


## off('locationServiceState')

```TypeScript
function off(type: 'locationServiceState', callback?: Callback<boolean>): void
```

取消订阅位置服务状态变化。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** locationEnabledChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'locationServiceState' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |


## off('cachedGnssLocationsReporting')

```TypeScript
function off(type: 'cachedGnssLocationsReporting', callback?: Callback<Array<Location>>): void
```

取消订阅缓存GNSS定位结果上报事件。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** cachedGnssLocationsChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cachedGnssLocationsReporting' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;Location&gt;&gt; | 否 |


## off('gnssStatusChange')

```TypeScript
function off(type: 'gnssStatusChange', callback?: Callback<SatelliteStatusInfo>): void
```

取消订阅GNSS卫星状态信息上报事件。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** satelliteStatusChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'gnssStatusChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | 否 |


## off('nmeaMessageChange')

```TypeScript
function off(type: 'nmeaMessageChange', callback?: Callback<string>): void
```

取消订阅GNSS NMEA信息上报事件。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** nmeaMessage

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'nmeaMessageChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |


## off('fenceStatusChange')

```TypeScript
function off(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void
```

删除一个围栏，并取消订阅该围栏事件。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** gnssFenceStatusChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Geofence

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'fenceStatusChange' | 是 |
| request | [GeofenceRequest](arkts-location-geolocationmanager-geofencerequest-i.md) | 是 |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | 是 |
