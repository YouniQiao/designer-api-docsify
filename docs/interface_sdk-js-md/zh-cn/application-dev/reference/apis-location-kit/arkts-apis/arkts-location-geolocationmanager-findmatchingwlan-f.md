# findMatchingWlan

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## findMatchingWlan

```TypeScript
function findMatchingWlan(
      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>
```

Check whether the WLAN scan results match the WLAN BSSID list,return information about the WLAN device that is successfully matched.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-geoLocationManager-function findMatchingWlan(      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>--><!--Device-geoLocationManager-function findMatchingWlan(      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wlanBssidArray | Array&lt;string&gt; | 是 | Indicates the list of WLAN BSSIDs that need to be matched. |
| rssiThreshold | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the WLAN RSSI threshold, only matches WLAN BSSIDs with RSSI greater than this threshold. |
| needStartScan | boolean | 是 | Indicates whether a WLAN scan needs to be initiated. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;MatchingWlanInfo&gt;&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.findMatchingWlan} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 3301800 | Failed to start WLAN scanning. |
| 3301100 | The location switch is off. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let wlanBssidArray: Array<string> = ["02:1b:32:23:ea:91", "02:1b:32:23:ea:93"];
  let rssiThreshold: number = -70;
  let needStartScan: boolean = true;
  geoLocationManager.findMatchingWlan(wlanBssidArray, rssiThreshold, needStartScan).then((res) => {
    console.info("WLAN BSSID Matched Result: " + JSON.stringify(res));
  })
} catch (error) {
  console.error("findMatchingWlan: errCode " + error.code + ", errMessage " + error.message);
}
```

