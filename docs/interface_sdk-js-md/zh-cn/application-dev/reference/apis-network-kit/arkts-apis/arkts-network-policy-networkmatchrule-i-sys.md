# NetworkMatchRule（系统接口）

The matching rules of network quota policies.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-policy-export interface NetworkMatchRule--><!--Device-policy-export interface NetworkMatchRule-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## identity

```TypeScript
identity: string
```

To specify the identity of network, such as different WLAN.

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetworkMatchRule-identity: string--><!--Device-NetworkMatchRule-identity: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## netType

```TypeScript
netType: NetBearType
```

netType see {@link NetBearType}.

**类型：** [NetBearType](arkts-network-connection-netbeartype-e.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetworkMatchRule-netType: NetBearType--><!--Device-NetworkMatchRule-netType: NetBearType-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## simId

```TypeScript
simId: string
```

The ID of the target card, valid when netType is BEARER_CELLULAR.

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetworkMatchRule-simId: string--><!--Device-NetworkMatchRule-simId: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

