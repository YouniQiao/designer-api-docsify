# AuthResultInfo

表示认证结果信息，用于描述认证结果。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [userAuth.UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md)

<!--Device-userAuth-interface AuthResultInfo--><!--Device-userAuth-interface AuthResultInfo-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## lockoutDuration

```TypeScript
lockoutDuration?: number
```

认证操作的锁定时长，时间单位为毫秒ms。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [userAuth.AuthLockState.lockoutDuration](arkts-userauthentication-userauth-authlockstate-i.md#lockoutduration)

<!--Device-AuthResultInfo-lockoutDuration?: number--><!--Device-AuthResultInfo-lockoutDuration?: number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## remainAttempts

```TypeScript
remainAttempts?: number
```

剩余的认证尝试次数。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [userAuth.AuthLockState.remainingAuthAttempts](arkts-userauthentication-userauth-authlockstate-i.md#remainingauthattempts)

<!--Device-AuthResultInfo-remainAttempts?: number--><!--Device-AuthResultInfo-remainAttempts?: number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## result

```TypeScript
result: number
```

认证结果。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [userAuth.UserAuthResult.result](arkts-userauthentication-userauth-userauthresult-i.md#result)

<!--Device-AuthResultInfo-result: number--><!--Device-AuthResultInfo-result: number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## token

```TypeScript
token?: Uint8Array
```

用户身份认证通过的凭证。

**Type:** Uint8Array

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [userAuth.UserAuthResult.token](arkts-userauthentication-userauth-userauthresult-i.md#token)

<!--Device-AuthResultInfo-token?: Uint8Array--><!--Device-AuthResultInfo-token?: Uint8Array-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

