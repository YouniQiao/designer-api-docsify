# AuthResult

表示认证结果信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-appAccount-interface AuthResult--><!--Device-appAccount-interface AuthResult-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## account

```TypeScript
account?: AppAccountInfo
```

令牌所属的账号信息，默认为空。

**Type:** [AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AuthResult-account?: AppAccountInfo--><!--Device-AuthResult-account?: AppAccountInfo-End-->

**System capability:** SystemCapability.Account.AppAccount

## tokenInfo

```TypeScript
tokenInfo?: AuthTokenInfo
```

令牌信息，默认为空。

**Type:** [AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AuthResult-tokenInfo?: AuthTokenInfo--><!--Device-AuthResult-tokenInfo?: AuthTokenInfo-End-->

**System capability:** SystemCapability.Account.AppAccount

