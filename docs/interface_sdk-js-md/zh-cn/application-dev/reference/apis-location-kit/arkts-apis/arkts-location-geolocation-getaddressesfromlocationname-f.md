# getAddressesFromLocationName

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## getAddressesFromLocationName

```TypeScript
function getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void
```

调用地理编码服务，将地理描述转换为具体坐标，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Geocoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [GeoCodeRequest](arkts-location-geolocationmanager-geocoderequest-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;GeoAddress&gt;&gt; | 是 |


## getAddressesFromLocationName

```TypeScript
function getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>
```

调用地理编码服务，将地理描述转换为具体坐标，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Geocoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [GeoCodeRequest](arkts-location-geolocationmanager-geocoderequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;GeoAddress & gt; & gt; |
