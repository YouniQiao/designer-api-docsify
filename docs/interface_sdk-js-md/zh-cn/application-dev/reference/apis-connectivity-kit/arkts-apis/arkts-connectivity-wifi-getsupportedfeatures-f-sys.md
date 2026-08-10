# getSupportedFeatures（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getSupportedFeatures

```TypeScript
function getSupportedFeatures(): number
```

Obtains the features supported by this device.

&lt;p&gt;To check whether this device supports a specified feature.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.getSupportedFeatures

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getSupportedFeatures(): number--><!--Device-wifi-function getSupportedFeatures(): number-End-->

**系统能力：** SystemCapability.Communication.WiFi.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Returns the features supported by this device. |

