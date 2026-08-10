# offLocationChange

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offLocationChange

```TypeScript
function offLocationChange(callback?: Callback<Location>): void
```

Unsubscribe location changed.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本23 - 24：ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offLocationChange(callback?: Callback<Location>): void--><!--Device-geoLocationManager-function offLocationChange(callback?: Callback<Location>): void-End-->

**系统能力：** 
- API版本23+：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | 否 | Indicates the callback for reporting the location result.<br>**起始版本：** 23 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.offLocationChange} due to limited device capabilities.<br>**适用版本：** 23+ |
| 201 | Permission verification failed. The application does not have the permission required to call the API. Introduced in API 9 and will not be threw above API 24.<br>**适用版本：** 23 - 24 |
| 3301000 | The location service is unavailable.<br>**适用版本：** 23+ |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

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
  geoLocationManager.offLocationChange(locationChange);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

