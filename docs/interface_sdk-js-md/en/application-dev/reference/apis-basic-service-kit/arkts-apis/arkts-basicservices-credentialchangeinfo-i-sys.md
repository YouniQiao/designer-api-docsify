# CredentialChangeInfo (System API)

Defines the credential change information.

**Since:** 23

<!--Device-osAccount-interface CredentialChangeInfo--><!--Device-osAccount-interface CredentialChangeInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## accountId

```TypeScript
accountId: number
```

OS account ID.

**Type:** number

**Since:** 23

<!--Device-CredentialChangeInfo-accountId: int--><!--Device-CredentialChangeInfo-accountId: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## addedCredentialId

```TypeScript
addedCredentialId?: Uint8Array
```

Credential ID. An ID is returned when a credential is added or updated. which is **undefined** by default.

**Type:** Uint8Array

**Since:** 23

<!--Device-CredentialChangeInfo-addedCredentialId?: Uint8Array--><!--Device-CredentialChangeInfo-addedCredentialId?: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## changeType

```TypeScript
changeType: CredentialChangeType
```

Credential change type.

**Type:** CredentialChangeType

**Since:** 23

<!--Device-CredentialChangeInfo-changeType: CredentialChangeType--><!--Device-CredentialChangeInfo-changeType: CredentialChangeType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## credentialType

```TypeScript
credentialType: AuthType
```

Credential type.

**Type:** AuthType

**Since:** 23

<!--Device-CredentialChangeInfo-credentialType: AuthType--><!--Device-CredentialChangeInfo-credentialType: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## deletedCredentialId

```TypeScript
deletedCredentialId?: Uint8Array
```

Credential ID. An ID is returned when a credential is deleted or updated. which is **undefined** by default.

**Type:** Uint8Array

**Since:** 23

<!--Device-CredentialChangeInfo-deletedCredentialId?: Uint8Array--><!--Device-CredentialChangeInfo-deletedCredentialId?: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## isSilent

```TypeScript
isSilent: boolean
```

Whether the change is silent. A silent change is automatically initiated by the system in the background.

**Type:** boolean

**Since:** 23

<!--Device-CredentialChangeInfo-isSilent: boolean--><!--Device-CredentialChangeInfo-isSilent: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

