# getAddressesFromLocationName

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getAddressesFromLocationName

```TypeScript
function getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void
```

调用地理编码服务，将地理描述转换为具体坐标，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Location.Location.Geocoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [GeoCodeRequest](arkts-location-geolocationmanager-geocoderequest-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;GeoAddress&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [3301400](../errorcode-geoLocationManager.md#3301400-地理编码查询失败) |


## getAddressesFromLocationName

```TypeScript
function getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>
```

调用地理编码服务，将地理描述转换为具体坐标，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Location.Location.Geocoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [GeoCodeRequest](arkts-location-geolocationmanager-geocoderequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;GeoAddress & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [3301400](../errorcode-geoLocationManager.md#3301400-地理编码查询失败) |
