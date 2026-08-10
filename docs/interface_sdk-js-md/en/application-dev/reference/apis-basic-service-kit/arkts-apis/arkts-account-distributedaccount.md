# @ohos.account.distributedAccount

本模块提供管理分布式账号的一些基础功能，主要包括查询和更新账号登录状态。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace distributedAccount--><!--Device-unnamed-declare namespace distributedAccount-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { distributedAccount } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getDistributedAccountAbility](arkts-basicservices-distributedaccount-getdistributedaccountability-f.md#getdistributedaccountability) | 获取分布式账号单实例对象。 |

### Interfaces

| Name | Description |
| --- | --- |
| [DistributedAccountAbility](arkts-basicservices-distributedaccount-distributedaccountability-i.md) | 提供查询和更新分布式账号登录状态方法（需要先获取分布式账号的单实例对象）。 |
| [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | 提供操作系统账号的分布式信息。 |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [DistributedAccountAbility](arkts-basicservices-distributedaccount-distributedaccountability-i-sys.md) | 提供查询和更新分布式账号登录状态方法（需要先获取分布式账号的单实例对象）。 |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [DistributedAccountStatus](arkts-basicservices-distributedaccount-distributedaccountstatus-e.md) | 表示分布式账号状态枚举。 |

