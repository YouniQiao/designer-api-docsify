# getDistributedAccountAbility

## Modules to Import

```TypeScript
import { distributedAccount } from 'kits/@kit.BasicServicesKit';
```

## getDistributedAccountAbility

```TypeScript
function getDistributedAccountAbility(): DistributedAccountAbility
```

Obtains a **DistributedAccountAbility** instance.

**Since:** 7

<!--Device-distributedAccount-function getDistributedAccountAbility(): DistributedAccountAbility--><!--Device-distributedAccount-function getDistributedAccountAbility(): DistributedAccountAbility-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DistributedAccountAbility](arkts-basicservices-distributedaccount-distributedaccountability-i.md) |

## Examples

```TypeScript
// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
```
