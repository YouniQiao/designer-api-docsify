# on

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## on('locationChange')

```TypeScript
function on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void
```

开启位置变化订阅，并发起定位请求。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** locationChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'locationChange' | 是 |
| request | [LocationRequest](arkts-location-geolocation-locationrequest-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | 是 |


## on('locationServiceState')

```TypeScript
function on(type: 'locationServiceState', callback: Callback<boolean>): void
```

订阅位置服务状态变化。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** locationEnabledChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'locationServiceState' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |


## on('cachedGnssLocationsReporting')

```TypeScript
function on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void
```

订阅缓存GNSS定位结果上报事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** cachedGnssLocationsChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cachedGnssLocationsReporting' | 是 |
| request | [CachedGnssLocationsRequest](arkts-location-geolocationmanager-cachedgnsslocationsrequest-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;Location&gt;&gt; | 是 |


## on('gnssStatusChange')

```TypeScript
function on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void
```

订阅GNSS卫星状态信息上报事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** satelliteStatusChange

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'gnssStatusChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | 是 |


## on('nmeaMessageChange')

```TypeScript
function on(type: 'nmeaMessageChange', callback: Callback<string>): void
```

订阅GNSS NMEA信息上报事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** nmeaMessage

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'nmeaMessageChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 |


## on('fenceStatusChange')

```TypeScript
function on(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void
```

添加一个围栏，并订阅地理围栏事件。使用callback异步回调。

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
