# isFusionFenceSupported（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isFusionFenceSupported

```TypeScript
function isFusionFenceSupported(): boolean
```

Check whether the fusion fence service is supported.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-geoLocationManager-function isFusionFenceSupported(): boolean--><!--Device-geoLocationManager-function isFusionFenceSupported(): boolean-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let isFusionFenceSupported = geoLocationManager.isFusionFenceSupported();
} catch (err) {
  console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

