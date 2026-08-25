# setMockedLocations（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## setMockedLocations

```TypeScript
function setMockedLocations(config: LocationMockConfig): void
```

设置模拟的位置信息，后面会以该接口中携带的时间间隔上报模拟位置。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本20+：ohos.permission.MOCK_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [LocationMockConfig](arkts-location-geolocationmanager-locationmockconfig-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [3301100](../errorcode-geoLocationManager.md#3301100-位置功能的开关未开启导致功能失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let locations: Array<geoLocationManager.Location> = [
  {
    "latitude": 30.12,
    "longitude": 120.11,
    "altitude": 123,
    "accuracy": 1,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 1000000000,
    "additionSize": 0,
    "isFromMock": true
  },
  {
    "latitude": 31.13,
    "longitude": 121.11,
    "altitude": 123,
    "accuracy": 2,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 2000000000,
    "additionSize": 0,
    "isFromMock": true
  },
  {
    "latitude": 32.14,
    "longitude": 122.11,
    "altitude": 123,
    "accuracy": 3,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 3000000000,
    "additionSize": 0,
    "isFromMock": true
  },
  {
    "latitude": 33.15,
    "longitude": 123.11,
    "altitude": 123,
    "accuracy": 4,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 4000000000,
    "additionSize": 0,
    "isFromMock": true
  },
  {
    "latitude": 34.16,
    "longitude": 124.11,
    "altitude": 123,
    "accuracy": 5,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 5000000000,
    "additionSize": 0,
    "isFromMock": true
  }
];
let config: geoLocationManager.LocationMockConfig = { "timeInterval": 5, "locations": locations };
try {
  geoLocationManager.enableLocationMock();
  geoLocationManager.setMockedLocations(config);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
