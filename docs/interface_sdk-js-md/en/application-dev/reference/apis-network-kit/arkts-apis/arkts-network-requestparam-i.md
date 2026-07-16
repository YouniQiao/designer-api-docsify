# RequestParam

Pagination query input parameters.

**Since:** 15

<!--Device-netFirewall-interface RequestParam--><!--Device-netFirewall-interface RequestParam-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## Modules to Import

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
```

## orderField

```TypeScript
orderField: NetFirewallOrderField
```

Sort field.

**Type:** NetFirewallOrderField

**Since:** 15

<!--Device-RequestParam-orderField: NetFirewallOrderField--><!--Device-RequestParam-orderField: NetFirewallOrderField-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## orderType

```TypeScript
orderType: NetFirewallOrderType
```

Sort Type: ascending or descending.

**Type:** NetFirewallOrderType

**Since:** 15

<!--Device-RequestParam-orderType: NetFirewallOrderType--><!--Device-RequestParam-orderType: NetFirewallOrderType-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## page

```TypeScript
page: number
```

Page number: indicates the page number to be queried. The start value is 1.

**Type:** number

**Since:** 15

<!--Device-RequestParam-page: number--><!--Device-RequestParam-page: number-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## pageSize

```TypeScript
pageSize: number
```

Page size: indicates the number of data records to be queried at a time. The maximum value is 50.

**Type:** number

**Since:** 15

<!--Device-RequestParam-pageSize: number--><!--Device-RequestParam-pageSize: number-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

