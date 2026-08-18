# isFeatureSupported

## 导入模块

```TypeScript
```

## isFeatureSupported

```TypeScript
function isFeatureSupported(featureId: number): boolean
```

判断设备是否支持相关WLAN特性。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isFeatureSupported](arkts-connectivity-wifimanager-isfeaturesupported-f.md#isfeaturesupported)

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function isFeatureSupported(featureId: number): boolean--><!--Device-wifi-function isFeatureSupported(featureId: number): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| featureId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import wifi from '@ohos.wifi';

try {
  let featureId = 0;
  let ret = wifi.isFeatureSupported(featureId);
  console.info("isFeatureSupported:" + ret);
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
