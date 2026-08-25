# @ohos.secureElement(安全单元的通道管理)

本模块主要用于操作及管理安全单元（SecureElement，简称SE），电子设备上可能存在的安全单元有eSE（Embedded SE）和SIM卡。文档中出现的SE服务为SEService实例，参见 [createService](arkts-connectivity-omapi-createservice-f.md)。对于文档中出现以下类型说明：  
| 类型 | 说明 | | ------- | ---------------------------------------------- | | [Reader](arkts-connectivity-omapi-reader-i.md) | 此类的实例表示该设备支持的SE，如果支持eSE、SIM和SIM2，则返回3个实例，其中SIM2从API version 22开始支持。 | | [Session](../../apis-camera-kit/arkts-apis/arkts-camera-camera-session-i.md) | 此类的实例表示在某个SE Reader实例上创建连接会话。 | | [Channel](arkts-connectivity-omapi-channel-i.md) |

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Communication.SecureElement

## 导入模块

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createService(安全单元的通道管理)](arkts-connectivity-omapi-createservice-f.md) |
| [newSEService(安全单元的通道管理)](arkts-connectivity-omapi-newseservice-f.md#newseserviceservicestate) |
| [off(安全单元的通道管理)](arkts-connectivity-omapi-off-f.md#offstatechanged) |
| [on(安全单元的通道管理)](arkts-connectivity-omapi-on-f.md#onstatechanged) |

### 接口

| 名称 |
| --- |
| [Channel(安全单元的通道管理)](arkts-connectivity-omapi-channel-i.md) |
| [Reader(安全单元的通道管理)](arkts-connectivity-omapi-reader-i.md) |
| [SEService(安全单元的通道管理)](arkts-connectivity-omapi-seservice-i.md) |
| [Session(安全单元的通道管理)](arkts-connectivity-omapi-session-i.md) |

### 枚举

| 名称 |
| --- |
| [ServiceState(安全单元的通道管理)](arkts-connectivity-omapi-servicestate-e.md) |
