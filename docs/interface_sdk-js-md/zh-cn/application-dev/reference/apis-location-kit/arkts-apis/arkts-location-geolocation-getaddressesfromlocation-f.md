# getAddressesFromLocation

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## getAddressesFromLocation

```TypeScript
function getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void
```

调用逆地理编码服务，将坐标转换为地理描述，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Geocoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [ReverseGeoCodeRequest](arkts-location-geolocation-reversegeocoderequest-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;GeoAddress&gt;&gt; | 是 |


## getAddressesFromLocation

```TypeScript
function getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise<Array<GeoAddress>>
```

调用逆地理编码服务，将坐标转换为地理描述，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Geocoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [ReverseGeoCodeRequest](arkts-location-geolocation-reversegeocoderequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;GeoAddress & gt; & gt; |
