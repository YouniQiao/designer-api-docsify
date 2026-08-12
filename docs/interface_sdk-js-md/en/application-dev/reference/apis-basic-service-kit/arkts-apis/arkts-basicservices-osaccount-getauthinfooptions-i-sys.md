# GetAuthInfoOptions (System API)

Represents a set of optional parameters for  
[GetAuthInfo](arkts-basicservices-osaccount-useridentitymanager-c-sys.md#getAuthInfo-3).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-osAccount-interface GetAuthInfoOptions--><!--Device-osAccount-interface GetAuthInfoOptions-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## accountId

```TypeScript
accountId?: int
```

OS account ID, which is **undefined** by default.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GetAuthInfoOptions-accountId?: int--><!--Device-GetAuthInfoOptions-accountId?: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authType

```TypeScript
authType?: AuthType
```

Authentication type, which is **undefined** by default.

**Type:** AuthType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GetAuthInfoOptions-authType?: AuthType--><!--Device-GetAuthInfoOptions-authType?: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

