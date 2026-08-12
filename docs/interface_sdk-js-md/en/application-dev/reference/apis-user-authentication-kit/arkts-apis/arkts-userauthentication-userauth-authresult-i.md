# AuthResult

Represents the authentication result object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [AuthResultInfo](arkts-userauthentication-userauth-authresultinfo-i.md#AuthResultInfo)

<!--Device-userAuth-interface AuthResult--><!--Device-userAuth-interface AuthResult-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## freezingTime

```TypeScript
freezingTime?: number
```

Time for which the authentication operation is frozen. The unit is milliseconds.

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [lockoutDuration](arkts-userauthentication-userauth-authresultinfo-i.md#lockoutDuration)

<!--Device-AuthResult-freezingTime?: number--><!--Device-AuthResult-freezingTime?: number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## remainTimes

```TypeScript
remainTimes?: number
```

Number of remaining authentication operations.

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [remainAttempts](arkts-userauthentication-userauth-authresultinfo-i.md#remainAttempts)

<!--Device-AuthResult-remainTimes?: number--><!--Device-AuthResult-remainTimes?: number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## token

```TypeScript
token?: Uint8Array
```

Authentication token information.

**Type:** Uint8Array

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [token](arkts-userauthentication-userauth-authresultinfo-i.md#token)

<!--Device-AuthResult-token?: Uint8Array--><!--Device-AuthResult-token?: Uint8Array-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

