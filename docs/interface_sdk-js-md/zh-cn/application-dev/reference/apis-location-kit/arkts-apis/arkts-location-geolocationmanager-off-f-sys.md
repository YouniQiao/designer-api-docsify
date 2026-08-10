# off（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## off('locatingRequiredDataChange')

```TypeScript
function off(type: 'locatingRequiredDataChange', callback?: Callback<Array<LocatingRequiredData>>): void
```

Stop WiFi/BT scanning and unsubscribe from WiFi/BT scanning information changes.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function off(type: 'locatingRequiredDataChange', callback?: Callback<Array<LocatingRequiredData>>): void--><!--Device-geoLocationManager-function off(type: 'locatingRequiredDataChange', callback?: Callback<Array<LocatingRequiredData>>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'locatingRequiredDataChange' | 是 | Indicates the location service event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;LocatingRequiredData&gt;&gt; | 否 | Indicates the callback for reporting WiFi/BT scan info. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.off(' locatingRequiredDataChange')} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let callback = (code: Array<geoLocationManager.LocatingRequiredData>): void => {
  console.info('locatingRequiredDataChange: ' + JSON.stringify(code));
}
let config: geoLocationManager.LocatingRequiredDataConfig = { 'type': 1, 'needStartScan': true, 'scanInterval': 10000 };
try {
  geoLocationManager.on('locatingRequiredDataChange', config, callback);
  geoLocationManager.off('locatingRequiredDataChange', callback);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```


## off('locationIconStatusChange')

```TypeScript
function off(type: 'locationIconStatusChange', callback?: Callback<LocationIconStatus>): void
```

Unsubscribe location icon status changed.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-geoLocationManager-function off(type: 'locationIconStatusChange', callback?: Callback<LocationIconStatus>): void--><!--Device-geoLocationManager-function off(type: 'locationIconStatusChange', callback?: Callback<LocationIconStatus>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'locationIconStatusChange' | 是 | Indicates the location service event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LocationIconStatus&gt; | 否 | Indicates the callback for reporting the location icon status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.off(' locationIconStatusChange')} due to limited device capabilities. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let callback = (code: geoLocationManager.LocationIconStatus): void => {
  console.info('LocationIconStatus: ' + JSON.stringify(code));
}
try {
  geoLocationManager.on('locationIconStatusChange', callback);
  geoLocationManager.off('locationIconStatusChange', callback);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

