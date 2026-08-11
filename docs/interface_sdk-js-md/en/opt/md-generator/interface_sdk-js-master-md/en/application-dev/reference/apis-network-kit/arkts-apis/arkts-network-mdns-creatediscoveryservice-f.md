# createDiscoveryService

## Modules to Import

```TypeScript
import { mdns } from 'kits/@kit.NetworkKit';
```

## createDiscoveryService

```TypeScript
function createDiscoveryService(context: Context, serviceType: string): DiscoveryService
```

Create an mDNS based discovery service with context and serviceType.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-mdns-function createDiscoveryService(context: Context, serviceType: string): DiscoveryService--><!--Device-mdns-function createDiscoveryService(context: Context, serviceType: string): DiscoveryService-End-->

**System capability:** SystemCapability.Communication.NetManager.MDNS

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| serviceType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DiscoveryService](arkts-network-mdns-discoveryservice-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

Stage model:

```TypeScript
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let serviceType = "_print._tcp";
let discoveryService : Object = mdns.createDiscoveryService(context, serviceType);
```
