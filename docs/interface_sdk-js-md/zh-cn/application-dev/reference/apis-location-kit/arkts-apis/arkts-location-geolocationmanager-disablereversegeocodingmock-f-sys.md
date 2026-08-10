# disableReverseGeocodingMock（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## disableReverseGeocodingMock

```TypeScript
function disableReverseGeocodingMock(): void
```

Disable the reverse geocoding simulation function.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本20+：ohos.permission.MOCK_LOCATION

<!--Device-geoLocationManager-function disableReverseGeocodingMock(): void--><!--Device-geoLocationManager-function disableReverseGeocodingMock(): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${ geoLocationManager.disableReverseGeocodingMock} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**适用版本：** 20+ |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.disableReverseGeocodingMock();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

