# OsAccountInfo

表示系统账号信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-osAccount-interface OsAccountInfo--><!--Device-osAccount-interface OsAccountInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## isLoggedIn

```TypeScript
isLoggedIn?: boolean
```

是否登录。true表示已登录；false表示未登录。

此接口为系统接口，默认为false。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-isLoggedIn?: boolean--><!--Device-OsAccountInfo-isLoggedIn?: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## shortName

```TypeScript
shortName?: string
```

系统账号的短名称。

此接口为系统接口，默认为空。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-shortName?: string--><!--Device-OsAccountInfo-shortName?: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

