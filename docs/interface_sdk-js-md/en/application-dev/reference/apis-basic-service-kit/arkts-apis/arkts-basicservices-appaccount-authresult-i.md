# AuthResult

Defines the authentication result.

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

Information about the account to which the token belongs. By default, no value is passed in.

**Type:** [AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AuthResult-account?: AppAccountInfo--><!--Device-AuthResult-account?: AppAccountInfo-End-->

**System capability:** SystemCapability.Account.AppAccount

## tokenInfo

```TypeScript
tokenInfo?: AuthTokenInfo
```

Token information. By default, no value is passed in.

**Type:** [AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AuthResult-tokenInfo?: AuthTokenInfo--><!--Device-AuthResult-tokenInfo?: AuthTokenInfo-End-->

**System capability:** SystemCapability.Account.AppAccount

