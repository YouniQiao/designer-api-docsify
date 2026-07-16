# AuthUser (System API)

Represents the user authorization information.

**Since:** 21

<!--Device-dlpPermission-export interface AuthUser--><!--Device-dlpPermission-export interface AuthUser-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## authAccount

```TypeScript
authAccount: string
```

Account of the user who can access the DLP file. The value contains a maximum of 255 bytes. If the value is out of range, error code 401 is thrown.

**Type:** string

**Since:** 21

<!--Device-AuthUser-authAccount: string--><!--Device-AuthUser-authAccount: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

## authAccountType

```TypeScript
authAccountType: AccountType
```

Type of the account.

**Type:** AccountType

**Since:** 21

<!--Device-AuthUser-authAccountType: AccountType--><!--Device-AuthUser-authAccountType: AccountType-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

## dlpFileAccess

```TypeScript
dlpFileAccess: DLPFileAccess
```

Permission granted to the user.

**Type:** DLPFileAccess

**Since:** 21

<!--Device-AuthUser-dlpFileAccess: DLPFileAccess--><!--Device-AuthUser-dlpFileAccess: DLPFileAccess-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

## permExpiryTime

```TypeScript
permExpiryTime: number
```

Time when the authorization expires. The value must be greater than or equal to 0. If the value is out of range, it will be forcibly converted to an unsigned integer. Unit: s.

**Type:** number

**Since:** 21

<!--Device-AuthUser-permExpiryTime: number--><!--Device-AuthUser-permExpiryTime: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

