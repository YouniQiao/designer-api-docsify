# @ohos.wifiManagerExt

Provides extended methods to operate or manage Wi-Fi.

&lt;p&gt;The APIs involved in this file are non-general APIs.These extended APIs are only used by some product types, such as routers. Common products should not use these APIs.&lt;/p&gt;

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-unnamed-declare namespace wifiManagerExt--><!--Device-unnamed-declare namespace wifiManagerExt-End-->

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

## 导入模块

```TypeScript
import { wifiManagerExt } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [disableHotspot](arkts-connectivity-wifimanagerext-disablehotspot-f.md#disablehotspot) | Disable Wi-Fi hotspot function.If Wi-Fi is enabled after the Wi-Fi hotspot is disabled, Wi-Fi may be re-enabled. |
| [enableHotspot](arkts-connectivity-wifimanagerext-enablehotspot-f.md#enablehotspot) | Enable Wi-Fi hotspot function.This method is asynchronous. After the Wi-Fi hotspot is enabled, Wi-Fi may be disabled. |
| [getPowerMode](arkts-connectivity-wifimanagerext-getpowermode-f.md#getpowermode) | Obtains the current Wi-Fi power mode. |
| [getPowerMode](arkts-connectivity-wifimanagerext-getpowermode-f.md#getpowermode-1) | Obtains the current Wi-Fi power mode. |
| [getSupportedPowerMode](arkts-connectivity-wifimanagerext-getsupportedpowermode-f.md#getsupportedpowermode) | Obtains the supported power Mode. |
| [getSupportedPowerMode](arkts-connectivity-wifimanagerext-getsupportedpowermode-f.md#getsupportedpowermode-1) | Obtains the supported power Mode. |
| [setPowerMode](arkts-connectivity-wifimanagerext-setpowermode-f.md#setpowermode) | Set the current Wi-Fi power mode. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [PowerMode](arkts-connectivity-wifimanagerext-powermode-e.md) | The power Mode enumeration. |

