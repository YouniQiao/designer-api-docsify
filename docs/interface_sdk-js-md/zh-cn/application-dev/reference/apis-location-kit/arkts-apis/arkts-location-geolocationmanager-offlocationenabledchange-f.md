# offLocationEnabledChange

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offLocationEnabledChange

```TypeScript
function offLocationEnabledChange(callback?: Callback<boolean>): void
```

Unsubscribe location switch changed.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-geoLocationManager-function offLocationEnabledChange(callback?: Callback<boolean>): void--><!--Device-geoLocationManager-function offLocationEnabledChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 | Indicates the callback for reporting the location switch status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.offLocationEnabledChange} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

