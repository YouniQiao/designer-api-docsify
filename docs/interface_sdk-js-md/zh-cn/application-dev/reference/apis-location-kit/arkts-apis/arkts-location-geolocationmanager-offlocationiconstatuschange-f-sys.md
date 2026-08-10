# offLocationIconStatusChange（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offLocationIconStatusChange

```TypeScript
function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void
```

Unsubscribe location icon status changed.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-geoLocationManager-function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void--><!--Device-geoLocationManager-function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LocationIconStatus&gt; | 否 | Indicates the callback for reporting the location icon status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.offLocationIconStatusChange} due to limited device capabilities. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |

