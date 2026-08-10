# WifiDeviceConfig

Wi-Fi device configuration information.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiDeviceConfig

<!--Device-wifi-interface WifiDeviceConfig--><!--Device-wifi-interface WifiDeviceConfig-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## bssid

```TypeScript
bssid: string
```

Wi-Fi bssid(MAC): the length is 6

**类型：** string

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiDeviceConfig.bssid

<!--Device-WifiDeviceConfig-bssid: string--><!--Device-WifiDeviceConfig-bssid: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## isHiddenSsid

```TypeScript
isHiddenSsid: boolean
```

Hide SSID or not, false(default): not hide

**类型：** boolean

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiDeviceConfig.isHiddenSsid

<!--Device-WifiDeviceConfig-isHiddenSsid: boolean--><!--Device-WifiDeviceConfig-isHiddenSsid: boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## preSharedKey

```TypeScript
preSharedKey: string
```

Wi-Fi key: maximum length is 64

**类型：** string

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiDeviceConfig.preSharedKey

<!--Device-WifiDeviceConfig-preSharedKey: string--><!--Device-WifiDeviceConfig-preSharedKey: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## securityType

```TypeScript
securityType: WifiSecurityType
```

Security type: reference definition of WifiSecurityType

**类型：** [WifiSecurityType](../../apis-mdm-kit/arkts-apis/arkts-mdm-wifimanager-wifisecuritytype-e.md)

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiDeviceConfig.securityType

<!--Device-WifiDeviceConfig-securityType: WifiSecurityType--><!--Device-WifiDeviceConfig-securityType: WifiSecurityType-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## ssid

```TypeScript
ssid: string
```

Wi-Fi SSID: the maximum length is 32

**类型：** string

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiDeviceConfig.ssid

<!--Device-WifiDeviceConfig-ssid: string--><!--Device-WifiDeviceConfig-ssid: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

