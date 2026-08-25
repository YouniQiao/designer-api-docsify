# findMatchingWlan

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## findMatchingWlan

```TypeScript
function findMatchingWlan(
      wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>
```

使用WLAN扫描结果与输入的WLAN BSSID列表进行匹配，匹配成功时返回对应的WLAN设备信息，匹配失败时返回空数组(数组长度为0)。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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
| Promise&lt;Array&lt;[MatchingWlanInfo](arkts-location-geolocationmanager-matchingwlaninfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301100](../errorcode-geoLocationManager.md#3301100-位置功能的开关未开启导致功能失败) |
| [3301800](../errorcode-geoLocationManager.md#3301800-启动wi-fi或蓝牙扫描失败) |
