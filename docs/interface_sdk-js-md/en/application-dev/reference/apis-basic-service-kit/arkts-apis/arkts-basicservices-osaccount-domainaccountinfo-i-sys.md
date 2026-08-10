# DomainAccountInfo

表示域账号信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface DomainAccountInfo--><!--Device-osAccount-interface DomainAccountInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## accountId

```TypeScript
accountId?: string
```

域账号标识。

此接口为系统接口，默认为undefined。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DomainAccountInfo-accountId?: string--><!--Device-DomainAccountInfo-accountId?: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## isAuthenticated

```TypeScript
isAuthenticated?: boolean
```

指示域账号是否已认证。true表示指定的域账号已认证；false表示指定的域账号未认证。

此接口为系统接口，默认为false。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DomainAccountInfo-isAuthenticated?: boolean--><!--Device-DomainAccountInfo-isAuthenticated?: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

