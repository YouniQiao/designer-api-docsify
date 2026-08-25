# getLocationIconStatus（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getLocationIconStatus

```TypeScript
function getLocationIconStatus(): LocationIconStatus
```

获取当前的定位图标状态。

**起始版本：** 12

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [LocationIconStatus](arkts-location-geolocationmanager-locationiconstatus-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
