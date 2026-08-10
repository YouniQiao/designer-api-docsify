# onLocationChange

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## onLocationChange

```TypeScript
function onLocationChange(request: LocationRequest | ContinuousLocationRequest,
  callback: Callback<Location>): void
```

Subscribe location changed.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本23+：ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function onLocationChange(request: LocationRequest | ContinuousLocationRequest,  callback: Callback<Location>): void--><!--Device-geoLocationManager-function onLocationChange(request: LocationRequest | ContinuousLocationRequest,  callback: Callback<Location>): void-End-->

**系统能力：** 
- API版本23+：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [LocationRequest](arkts-location-geolocationmanager-locationrequest-i.md) \| ContinuousLocationRequest | 是 | Indicates the location request parameters.<br>**起始版本：** 23 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | 是 | Indicates the callback for reporting the location result.<br>**起始版本：** 23 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.<br>**适用版本：** 23+ |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.onLocationChange} due to limited device capabilities.<br>**适用版本：** 23+ |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**适用版本：** 23+ |
| 3301000 | The location service is unavailable.<br>**适用版本：** 23+ |
| 3301100 | The location switch is off.<br>**适用版本：** 23+ |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

// 方式一：使用LocationRequest作为入参
let requestInfo: geoLocationManager.LocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
  'scenario': geoLocationManager.LocationRequestScenario.UNSET,
  'timeInterval': 1,
  'distanceInterval': 0,
  'maxAccuracy': 0
};
let locationChange = (location: geoLocationManager.Location): void => {
  console.info('locationChange: data: ' + JSON.stringify(location));
};
try {
  geoLocationManager.onLocationChange(requestInfo, locationChange);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}

// 方式二：使用ContinuousLocationRequest作为入参
let request: geoLocationManager.ContinuousLocationRequest = {
  'interval': 1,
  'locationScenario': geoLocationManager.UserActivityScenario.NAVIGATION
};
let locationCallback = (location: geoLocationManager.Location): void => {
  console.info('locationCallback: data: ' + JSON.stringify(location));
};
try {
  geoLocationManager.onLocationChange(request, locationCallback);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

