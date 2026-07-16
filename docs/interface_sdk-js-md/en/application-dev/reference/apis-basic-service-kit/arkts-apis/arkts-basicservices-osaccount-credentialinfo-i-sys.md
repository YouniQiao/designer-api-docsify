# CredentialInfo (System API)

Defines the credential information.

**Since:** 8

<!--Device-osAccount-interface CredentialInfo--><!--Device-osAccount-interface CredentialInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## accountId

```TypeScript
accountId?: number
```

OS account ID, which is **undefined** by default.

**Type:** number

**Since:** 12

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

<!--Device-CredentialInfo-additionalInfo?: string--><!--Device-CredentialInfo-additionalInfo?: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## credSubType

```TypeScript
credSubType: AuthSubType
```

Authentication credential subtype.

**Type:** AuthSubType

**Since:** 8

<!--Device-CredentialInfo-credSubType: AuthSubType--><!--Device-CredentialInfo-credSubType: AuthSubType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## credType

```TypeScript
credType: AuthType
```

Authentication credential type.

**Type:** AuthType

**Since:** 8

<!--Device-CredentialInfo-credType: AuthType--><!--Device-CredentialInfo-credType: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## token

```TypeScript
token: Uint8Array
```

Authentication token, which is left blank by default.

**Type:** Uint8Array

**Since:** 8

<!--Device-CredentialInfo-token: Uint8Array--><!--Device-CredentialInfo-token: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

