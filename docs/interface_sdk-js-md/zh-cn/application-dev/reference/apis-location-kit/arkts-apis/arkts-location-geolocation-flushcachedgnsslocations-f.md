# flushCachedGnssLocations

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## flushCachedGnssLocations

```TypeScript
function flushCachedGnssLocations(callback: AsyncCallback<boolean>): void
```

读取并清空GNSS芯片所有缓存位置。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## flushCachedGnssLocations

```TypeScript
function flushCachedGnssLocations(): Promise<boolean>
```

读取并清空GNSS芯片所有缓存位置。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
