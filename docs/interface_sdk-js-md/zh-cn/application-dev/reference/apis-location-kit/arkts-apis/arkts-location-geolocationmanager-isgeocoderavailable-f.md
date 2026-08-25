# isGeocoderAvailable

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isGeocoderAvailable

```TypeScript
function isGeocoderAvailable(): boolean
```

判断地理编码与逆地理编码服务状态。

**起始版本：** 9

**系统能力：** SystemCapability.Location.Location.Geocoder

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
