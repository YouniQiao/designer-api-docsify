# isCachedGnssServiceSupported

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isCachedGnssServiceSupported

```TypeScript
function isCachedGnssServiceSupported(): boolean
```

判断是否支持GNSS batching功能。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Location.Location.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
