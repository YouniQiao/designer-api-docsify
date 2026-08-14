# CredentialInfo (System API)

Defines the credential information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-osAccount-interface CredentialInfo--><!--Device-osAccount-interface CredentialInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'osAccount';
```

## accountId

```TypeScript
accountId?: int
```

OS account ID, which is **undefined** by default.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CredentialInfo-accountId?: int--><!--Device-CredentialInfo-accountId?: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## additionalInfo

```TypeScript
additionalInfo?: string
```

Additional information about the credential, which is an empty string by default.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CredentialInfo-additionalInfo?: string--><!--Device-CredentialInfo-additionalInfo?: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## credSubType

```TypeScript
credSubType: AuthSubType
```

Authentication credential subtype.

**Type:** [AuthSubType](arkts-basicservices-osaccount-authsubtype-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CredentialInfo-credSubType: AuthSubType--><!--Device-CredentialInfo-credSubType: AuthSubType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## credType

```TypeScript
credType: AuthType
```

Authentication credential type.

**Type:** AuthType

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CredentialInfo-credType: AuthType--><!--Device-CredentialInfo-credType: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## token

```TypeScript
token: Uint8Array
```

Authentication token, which is left blank by default.

**Type:** Uint8Array

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CredentialInfo-token: Uint8Array--><!--Device-CredentialInfo-token: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

