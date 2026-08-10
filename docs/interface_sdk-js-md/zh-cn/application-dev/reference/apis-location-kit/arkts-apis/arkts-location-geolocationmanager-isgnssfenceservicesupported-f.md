# isGnssFenceServiceSupported

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isGnssFenceServiceSupported

```TypeScript
function isGnssFenceServiceSupported(): boolean
```

Check whether the GNSS fence service is supported.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-geoLocationManager-function isGnssFenceServiceSupported(): boolean--><!--Device-geoLocationManager-function isGnssFenceServiceSupported(): boolean-End-->

**系统能力：** SystemCapability.Location.Location.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 3301000 | The location service is unavailable. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
try {
    let gnssFenceServiceSupported = geoLocationManager.isGnssFenceServiceSupported();
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

