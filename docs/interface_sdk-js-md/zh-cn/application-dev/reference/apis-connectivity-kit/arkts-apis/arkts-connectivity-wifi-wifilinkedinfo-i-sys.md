# WifiLinkedInfo

Wi-Fi connection information.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiLinkedInfo

<!--Device-wifi-interface WifiLinkedInfo--><!--Device-wifi-interface WifiLinkedInfo-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## chload

```TypeScript
chload: number
```

The load value of this Wi-Fi connection. A greater value indicates a higher load.

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiLinkedInfo.chload

<!--Device-WifiLinkedInfo-chload: number--><!--Device-WifiLinkedInfo-chload: number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## networkId

```TypeScript
networkId: number
```

The ID(uniquely identifies) of a Wi-Fi connection.

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiLinkedInfo.networkId

<!--Device-WifiLinkedInfo-networkId: number--><!--Device-WifiLinkedInfo-networkId: number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## snr

```TypeScript
snr: number
```

The signal-to-noise ratio (SNR) of this Wi-Fi connection.

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiLinkedInfo.snr

<!--Device-WifiLinkedInfo-snr: number--><!--Device-WifiLinkedInfo-snr: number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## suppState

```TypeScript
suppState: SuppState
```

The state of the supplicant of this Wi-Fi connection.

**类型：** [SuppState](arkts-connectivity-wifi-suppstate-e-sys.md)

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiLinkedInfo.suppState

<!--Device-WifiLinkedInfo-suppState: SuppState--><!--Device-WifiLinkedInfo-suppState: SuppState-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

