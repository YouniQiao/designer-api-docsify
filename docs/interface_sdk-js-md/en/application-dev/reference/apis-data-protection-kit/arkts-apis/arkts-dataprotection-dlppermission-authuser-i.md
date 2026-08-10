# AuthUser

表示授权用户数据。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-dlpPermission-export interface AuthUser--><!--Device-dlpPermission-export interface AuthUser-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## authAccount

```TypeScript
authAccount: string
```

表示被授权用户账号。不超过255字节，超出此范围抛出错误码401。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-AuthUser-authAccount: string--><!--Device-AuthUser-authAccount: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## authAccountType

```TypeScript
authAccountType: AccountType
```

表示被授权用户账号类型。

**Type:** [AccountType](arkts-dataprotection-dlppermission-accounttype-e.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-AuthUser-authAccountType: AccountType--><!--Device-AuthUser-authAccountType: AccountType-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## dlpFileAccess

```TypeScript
dlpFileAccess: DLPFileAccess
```

表示被授予的权限。

**Type:** [DLPFileAccess](arkts-dataprotection-dlppermission-dlpfileaccess-e.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-AuthUser-dlpFileAccess: DLPFileAccess--><!--Device-AuthUser-dlpFileAccess: DLPFileAccess-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## permExpiryTime

```TypeScript
permExpiryTime: number
```

表示授权到期时间。取值范围大于等于0，超出此范围将被强转为非符号整数。单位：s。

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-AuthUser-permExpiryTime: number--><!--Device-AuthUser-permExpiryTime: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

