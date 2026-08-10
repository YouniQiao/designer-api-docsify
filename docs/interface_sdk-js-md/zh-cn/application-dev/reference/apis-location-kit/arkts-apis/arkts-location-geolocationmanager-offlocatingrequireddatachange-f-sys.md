# offLocatingRequiredDataChange（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offLocatingRequiredDataChange

```TypeScript
function offLocatingRequiredDataChange(callback?: Callback<Array<LocatingRequiredData>>): void
```

Stop WiFi/BT scanning and unsubscribe from WiFi/BT scanning information changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offLocatingRequiredDataChange(callback?: Callback<Array<LocatingRequiredData>>): void--><!--Device-geoLocationManager-function offLocatingRequiredDataChange(callback?: Callback<Array<LocatingRequiredData>>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;LocatingRequiredData&gt;&gt; | 否 | Indicates the callback for reporting WiFi/BT scan info. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.offLocatingRequiredDataChange} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

