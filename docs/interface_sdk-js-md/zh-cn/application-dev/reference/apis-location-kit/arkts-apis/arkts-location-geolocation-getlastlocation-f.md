# getLastLocation

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## getLastLocation

```TypeScript
function getLastLocation(callback: AsyncCallback<Location>): void
```

获取上一次位置，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Location&gt; | 是 |


## getLastLocation

```TypeScript
function getLastLocation(): Promise<Location>
```

获取上一次位置，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Location & gt; |
