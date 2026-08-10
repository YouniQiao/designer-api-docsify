# getCurrentLocation

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## getCurrentLocation

```TypeScript
function getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void
```

Obtain current location

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCurrentLocation

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void--><!--Device-geolocation-function getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [CurrentLocationRequest](arkts-location-geolocationmanager-currentlocationrequest-i.md) | 是 | Indicates the location request parameters. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Location&gt; | 是 | Indicates the callback for reporting the location result. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
import BusinessError from "@ohos.base"
let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location) => {
    if (err) {
        console.info('locationChanger: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChanger: location=' + JSON.stringify(location));
    }
};
geolocation.getCurrentLocation(requestInfo, locationChange);
```


## getCurrentLocation

```TypeScript
function getCurrentLocation(callback: AsyncCallback<Location>): void
```

Obtain current location

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCurrentLocation

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function getCurrentLocation(callback: AsyncCallback<Location>): void--><!--Device-geolocation-function getCurrentLocation(callback: AsyncCallback<Location>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Location&gt; | 是 | Indicates the callback for reporting the location result. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
import BusinessError from "@ohos.base"
let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location):void => {
    if (err) {
        console.info('locationChanger: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChanger: location=' + JSON.stringify(location));
    }
};
geolocation.getCurrentLocation(locationChange);
```


## getCurrentLocation

```TypeScript
function getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>
```

Obtain current location

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCurrentLocation

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>--><!--Device-geolocation-function getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [CurrentLocationRequest](arkts-location-geolocationmanager-currentlocationrequest-i.md) | 否 | Indicates the location request parameters. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Location&gt; | The promise returned by the function. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
geolocation.getCurrentLocation(requestInfo).then((result) => {
    console.info('current location: ' + JSON.stringify(result));
});
```

