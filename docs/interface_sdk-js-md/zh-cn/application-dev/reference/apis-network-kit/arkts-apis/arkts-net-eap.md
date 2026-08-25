# @ohos.net.eap(扩展认证)

该模块提供了第三方客户端接入802.1X认证（一种基于端口的网络接入控制协议）流程的机制，支撑客户端的定制认证等功能。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Communication.NetManager.Eap

## 导入模块

```TypeScript
import { eap } from '@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [logOffEthEap(扩展认证)](arkts-network-eap-logoffetheap-f.md) |
| [regCustomEapHandler(扩展认证)](arkts-network-eap-regcustomeaphandler-f.md) |
| [replyCustomEapData(扩展认证)](arkts-network-eap-replycustomeapdata-f.md) |
| [startEthEap(扩展认证)](arkts-network-eap-startetheap-f.md) |
| [unregCustomEapHandler(扩展认证)](arkts-network-eap-unregcustomeaphandler-f.md) |

### 接口

| 名称 |
| --- |
| [EapData(扩展认证)](arkts-network-eap-eapdata-i.md) |
| [EthEapProfile(扩展认证)](arkts-network-eap-etheapprofile-i.md) |

### 枚举

| 名称 |
| --- |
| [CustomResult(扩展认证)](arkts-network-eap-customresult-e.md) |
| [EapMethod(扩展认证)](arkts-network-eap-eapmethod-e.md) |
| [Phase2Method(扩展认证)](arkts-network-eap-phase2method-e.md) |
