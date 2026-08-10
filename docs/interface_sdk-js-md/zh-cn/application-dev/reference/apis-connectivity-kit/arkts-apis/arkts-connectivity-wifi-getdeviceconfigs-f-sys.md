# getDeviceConfigs（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getDeviceConfigs

```TypeScript
function getDeviceConfigs(): Array<WifiDeviceConfig>
```

Obtains the list of all existing Wi-Fi configurations.

&lt;p&gt;You can obtain only the Wi-Fi configurations you created on your own application.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.getDeviceConfigs

**需要权限：** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION and ohos.permission.GET_WIFI_CONFIG

<!--Device-wifi-function getDeviceConfigs(): Array<WifiDeviceConfig>--><!--Device-wifi-function getDeviceConfigs(): Array<WifiDeviceConfig>-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;WifiDeviceConfig&gt; | sReturns the list of all existing Wi-Fi configurations you created on your application. |

## 示例

```TypeScript
import wifi from '@ohos.wifi';

try {
    let configs = wifi.getDeviceConfigs();
    console.info("configs:" + JSON.stringify(configs));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

