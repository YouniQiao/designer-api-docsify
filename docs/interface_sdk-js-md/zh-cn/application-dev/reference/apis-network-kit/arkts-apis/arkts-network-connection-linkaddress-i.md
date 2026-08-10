# LinkAddress

Defines network link information.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-connection-export interface LinkAddress--><!--Device-connection-export interface LinkAddress-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: NetAddress
```

Link address.

**类型：** [NetAddress](arkts-network-connection-netaddress-i.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-LinkAddress-address: NetAddress--><!--Device-LinkAddress-address: NetAddress-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## prefixLength

```TypeScript
prefixLength: int
```

The length of the link address prefix.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-LinkAddress-prefixLength: int--><!--Device-LinkAddress-prefixLength: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

