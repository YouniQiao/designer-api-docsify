# @ohos.net.eap

Provides interfaces to manage ethernet.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace eap--><!--Device-unnamed-declare namespace eap-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## 导入模块

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [logOffEthEap](arkts-network-eap-logoffetheap-f.md#logoffetheap) | Check whether the specified network is active. |
| [regCustomEapHandler](arkts-network-eap-regcustomeaphandler-f.md#regcustomeaphandler) | Customize eap packets by callback |
| [replyCustomEapData](arkts-network-eap-replycustomeapdata-f.md#replycustomeapdata) | send Customized eap packets to system |
| [startEthEap](arkts-network-eap-startetheap-f.md#startetheap) | Set the specified network interface parameters. |
| [unregCustomEapHandler](arkts-network-eap-unregcustomeaphandler-f.md#unregcustomeaphandler) | unreg the callback of eap packet customization. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [EapData](arkts-network-eap-eapdata-i.md) | Describes the EAP information. |
| [EthEapProfile](arkts-network-eap-etheapprofile-i.md) | Eth EAP profile. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [CustomResult](arkts-network-eap-customresult-e.md) | custom 802.1x result. |
| [EapMethod](arkts-network-eap-eapmethod-e.md) | 802.1x EAP method. |
| [Phase2Method](arkts-network-eap-phase2method-e.md) | 802.1x phase 2 method. |

