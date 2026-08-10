# DLPPermissionInfo

表示DLP文件的权限信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-dlpPermission-export interface DLPPermissionInfo--><!--Device-dlpPermission-export interface DLPPermissionInfo-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## dlpFileAccess

```TypeScript
dlpFileAccess: DLPFileAccess
```

表示DLP文件针对用户的授权类型，例如：只读。

**Type:** [DLPFileAccess](arkts-dataprotection-dlppermission-dlpfileaccess-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPPermissionInfo-dlpFileAccess: DLPFileAccess--><!--Device-DLPPermissionInfo-dlpFileAccess: DLPFileAccess-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## flags

```TypeScript
flags: number
```

表示DLP文件的详细操作权限，取值范围由不同[ActionFlagType](arkts-dataprotection-dlppermission-actionflagtype-e.md)的组合决定。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPPermissionInfo-flags: number--><!--Device-DLPPermissionInfo-flags: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

