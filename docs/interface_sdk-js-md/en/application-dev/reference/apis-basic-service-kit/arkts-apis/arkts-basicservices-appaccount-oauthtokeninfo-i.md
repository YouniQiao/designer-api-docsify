# OAuthTokenInfo

表示OAuth令牌信息。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃。建议使用[AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)

<!--Device-appAccount-interface OAuthTokenInfo--><!--Device-appAccount-interface OAuthTokenInfo-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## authType

```TypeScript
authType: string
```

令牌的鉴权类型。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.AuthTokenInfo.authType](arkts-basicservices-appaccount-authtokeninfo-i.md#authtype)

<!--Device-OAuthTokenInfo-authType: string--><!--Device-OAuthTokenInfo-authType: string-End-->

**System capability:** SystemCapability.Account.AppAccount

## token

```TypeScript
token: string
```

令牌的取值。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.AuthTokenInfo.token](arkts-basicservices-appaccount-authtokeninfo-i.md#token)

<!--Device-OAuthTokenInfo-token: string--><!--Device-OAuthTokenInfo-token: string-End-->

**System capability:** SystemCapability.Account.AppAccount

