# CredentialChangeInfo (System API)

表示凭据变更信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-osAccount-interface CredentialChangeInfo--><!--Device-osAccount-interface CredentialChangeInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## accountId

```TypeScript
accountId: int
```

表示系统账号标识。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CredentialChangeInfo-accountId: int--><!--Device-CredentialChangeInfo-accountId: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## addedCredentialId

```TypeScript
addedCredentialId?: Uint8Array
```

表示添加的凭据ID，添加凭据和更新凭据操作都会返回该ID。默认为undefined。

**Type:** Uint8Array

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CredentialChangeInfo-addedCredentialId?: Uint8Array--><!--Device-CredentialChangeInfo-addedCredentialId?: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## changeType

```TypeScript
changeType: CredentialChangeType
```

表示凭据变更的类型。

**Type:** [CredentialChangeType](arkts-basicservices-osaccount-credentialchangetype-e-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CredentialChangeInfo-changeType: CredentialChangeType--><!--Device-CredentialChangeInfo-changeType: CredentialChangeType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## credentialType

```TypeScript
credentialType: AuthType
```

表示凭据类型。

**Type:** [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CredentialChangeInfo-credentialType: AuthType--><!--Device-CredentialChangeInfo-credentialType: AuthType-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## deletedCredentialId

```TypeScript
deletedCredentialId?: Uint8Array
```

表示删除的凭据ID，删除凭据和更新凭据操作都会返回该ID。默认为undefined。

**Type:** Uint8Array

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CredentialChangeInfo-deletedCredentialId?: Uint8Array--><!--Device-CredentialChangeInfo-deletedCredentialId?: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## isSilent

```TypeScript
isSilent: boolean
```

表示是否为静默变更，静默变更表示变更由系统在后台自动地发起。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CredentialChangeInfo-isSilent: boolean--><!--Device-CredentialChangeInfo-isSilent: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

