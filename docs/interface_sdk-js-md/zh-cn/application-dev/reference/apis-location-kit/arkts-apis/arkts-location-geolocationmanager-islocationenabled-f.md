# isLocationEnabled

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isLocationEnabled

```TypeScript
function isLocationEnabled(): boolean
```

判断位置服务是否已经开启。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Location.Location.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
