# RequestParam

Pagination query input parameters.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-netFirewall-interface RequestParam--><!--Device-netFirewall-interface RequestParam-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## orderField

```TypeScript
orderField: NetFirewallOrderField
```

Sort field.

**类型：** [NetFirewallOrderField](arkts-network-netfirewall-netfirewallorderfield-e.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-RequestParam-orderField: NetFirewallOrderField--><!--Device-RequestParam-orderField: NetFirewallOrderField-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## orderType

```TypeScript
orderType: NetFirewallOrderType
```

Sort Type: ascending or descending.

**类型：** [NetFirewallOrderType](arkts-network-netfirewall-netfirewallordertype-e.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-RequestParam-orderType: NetFirewallOrderType--><!--Device-RequestParam-orderType: NetFirewallOrderType-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## page

```TypeScript
page: number
```

Page number: indicates the page number to be queried. The start value is 1.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-RequestParam-page: number--><!--Device-RequestParam-page: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## pageSize

```TypeScript
pageSize: number
```

Page size: indicates the number of data records to be queried at a time. The maximum value is 50.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-RequestParam-pageSize: number--><!--Device-RequestParam-pageSize: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

