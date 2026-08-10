# AuthTokenInfo

表示Auth令牌信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-appAccount-interface AuthTokenInfo--><!--Device-appAccount-interface AuthTokenInfo-End-->

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

<!--Device-AuthTokenInfo-account?: AppAccountInfo--><!--Device-AuthTokenInfo-account?: AppAccountInfo-End-->

**System capability:** SystemCapability.Account.AppAccount

## authType

```TypeScript
authType: string
```

令牌的鉴权类型。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AuthTokenInfo-authType: string--><!--Device-AuthTokenInfo-authType: string-End-->

**System capability:** SystemCapability.Account.AppAccount

## token

```TypeScript
token: string
```

令牌的取值。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AuthTokenInfo-token: string--><!--Device-AuthTokenInfo-token: string-End-->

**System capability:** SystemCapability.Account.AppAccount

