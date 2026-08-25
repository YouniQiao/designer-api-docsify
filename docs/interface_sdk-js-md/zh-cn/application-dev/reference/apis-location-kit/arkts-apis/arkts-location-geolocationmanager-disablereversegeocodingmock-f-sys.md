# disableReverseGeocodingMock（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## disableReverseGeocodingMock

```TypeScript
function disableReverseGeocodingMock(): void
```

去使能逆地理编码模拟功能。

**起始版本：** 9

**需要权限：** 
- API版本20+：ohos.permission.MOCK_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
