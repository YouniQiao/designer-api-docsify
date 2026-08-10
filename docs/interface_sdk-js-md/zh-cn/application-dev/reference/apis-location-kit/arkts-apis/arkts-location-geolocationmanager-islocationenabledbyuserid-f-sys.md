# isLocationEnabledByUserId（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isLocationEnabledByUserId

```TypeScript
function isLocationEnabledByUserId(userId: int): boolean
```

Obtaining the location switch status of a specified user.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-function isLocationEnabledByUserId(userId: int): boolean--><!--Device-geoLocationManager-function isLocationEnabledByUserId(userId: int): boolean-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the ID of a specified user. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.isLocationEnabledByUserId} due to limited device capabilities. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  // 查询指定系统账号的位置开关状态，如：处于ID为101的账号下，可以查询ID为100的账号的位置开关状态
  let userId: number = 100;
  let locationEnabled = geoLocationManager.isLocationEnabledByUserId(userId);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

