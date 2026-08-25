# setReverseGeocodingMockInfo（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## setReverseGeocodingMockInfo

```TypeScript
function setReverseGeocodingMockInfo(mockInfos: Array<ReverseGeocodingMockInfo>): void
```

设置逆地理编码模拟功能的配置信息，包含了位置和地名的对应关系，后续进行逆地理编码查询时如果位置信息位于配置信息中，就返回对应的地名。 该接口需要在调用geoLocationManager.enableReverseGeocodingMock之后才能调用。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本20+：ohos.permission.MOCK_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mockInfos | Array&lt;[ReverseGeocodingMockInfo](arkts-location-geolocationmanager-reversegeocodingmockinfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let mockInfos: Array<geoLocationManager.ReverseGeocodingMockInfo> = [
  {
    "location": {
      "locale": "zh",
      "latitude": 30.12,
      "longitude": 120.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 30.12,
      "longitude": 120.11,
      "isFromMock": true
    }
  },
  {
    "location": {
      "locale": "zh",
      "latitude": 31.12,
      "longitude": 121.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 31.12,
      "longitude": 121.11,
      "isFromMock": true
    }
  },
  {
    "location": {
      "locale": "zh",
      "latitude": 32.12,
      "longitude": 122.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 32.12,
      "longitude": 122.11,
      "isFromMock": true
    }
  },
  {
    "location": {
      "locale": "zh",
      "latitude": 33.12,
      "longitude": 123.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 33.12,
      "longitude": 123.11,
      "isFromMock": true
    }
  },
  {
    "location": {
      "locale": "zh",
      "latitude": 34.12,
      "longitude": 124.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 34.12,
      "longitude": 124.11,
      "isFromMock": true
    }
  },
];
try {
  geoLocationManager.enableReverseGeocodingMock();
  geoLocationManager.setReverseGeocodingMockInfo(mockInfos);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
