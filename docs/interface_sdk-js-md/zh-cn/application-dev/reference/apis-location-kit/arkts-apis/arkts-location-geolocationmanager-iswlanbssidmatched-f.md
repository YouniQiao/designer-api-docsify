# isWlanBssidMatched

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isWlanBssidMatched

```TypeScript
function isWlanBssidMatched(
      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<boolean>
```

Check whether the WLAN scan results match the WLAN BSSID list.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-geoLocationManager-function isWlanBssidMatched(      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<boolean>--><!--Device-geoLocationManager-function isWlanBssidMatched(      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<boolean>-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wlanBssidArray | Array&lt;string&gt; | 是 | Indicates the list of WLAN BSSIDs that need to be matched. |
| rssiThreshold | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the WLAN RSSI threshold, only matching WLAN BSSID with RSSI greater than this threshold. |
| needStartScan | boolean | 是 | Indicate whether a WLAN scan needs to be initiated. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.isWlanBssidMatched} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 3301800 | Failed to start WiFi scanning. |
| 3301100 | The location switch is off. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let wlanBssidArray: Array<string> = ["02:1b:32:23:ea:91", "02:1b:32:23:ea:93"];
  let rssiThreshold: number = -70;
  let needStartScan: boolean = true;
  geoLocationManager.isWlanBssidMatched(wlanBssidArray, rssiThreshold, needStartScan).then((res) => {
    console.info("Wlan Bssid Matched Result:" + res);
  })
} catch (error) {
  console.error("isWlanBssidMatched: errCode" + error.code + ", errMessage" + error.message);
}
```

