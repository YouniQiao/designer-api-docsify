# AuthResultInfo

Represents the authentication result.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [UserAuthResult](arkts-userauthentication-userauthresult-i.md#userauthresult)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from '@ohos.userIAM.userAuth';
```

## lockoutDuration

```TypeScript
lockoutDuration?: number
```

Lock duration of the authentication operation, in ms.

**Type:** number

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [lockoutDuration](arkts-userauthentication-authlockstate-i.md#lockoutduration)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## remainAttempts

```TypeScript
remainAttempts?: number
```

Number of remaining authentication attempts.

**Type:** number

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [remainingAuthAttempts](arkts-userauthentication-authlockstate-i.md#remainingauthattempts)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## result

```TypeScript
result: number
```

Authentication result.

**Type:** number

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [result](arkts-userauthentication-userauthresult-i.md#result)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## token

```TypeScript
token?: Uint8Array
```

Token that has passed the user identity authentication.

**Type:** Uint8Array

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [token](arkts-userauthentication-userauthresult-i.md#token)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

