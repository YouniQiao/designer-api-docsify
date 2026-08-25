# isWlanBssidMatched

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isWlanBssidMatched

```TypeScript
function isWlanBssidMatched(
      wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<boolean>
```

判断指定的BSSID是否存在于最新的WLAN扫描结果里。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wlanBssidArray | Array & lt;string & gt; | 是 |
| [rssiThreshold](arkts-location-geolocationmanager-bluetoothsearchrequestparams-i.md) | number | 是 |
| [needStartScan](arkts-location-geolocationmanager-locatingrequireddataconfig-i-sys.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301100](../errorcode-geoLocationManager.md#3301100-位置功能的开关未开启导致功能失败) |
| [3301800](../errorcode-geoLocationManager.md#3301800-启动wi-fi或蓝牙扫描失败) |
