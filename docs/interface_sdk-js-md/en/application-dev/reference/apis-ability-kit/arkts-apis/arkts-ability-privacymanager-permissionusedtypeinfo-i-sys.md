# PermissionUsedTypeInfo (System API)

Represents detailed information about the use of a permission.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface PermissionUsedTypeInfo--><!--Device-privacyManager-interface PermissionUsedTypeInfo-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## permissionName

```TypeScript
permissionName: Permissions
```

Name of the sensitive permission accessed.

**Type:** [Permissions](arkts-ability-permissions-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PermissionUsedTypeInfo-permissionName: Permissions--><!--Device-PermissionUsedTypeInfo-permissionName: Permissions-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## tokenId

```TypeScript
tokenId: int
```

Token ID of the application that accesses the sensitive permission.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PermissionUsedTypeInfo-tokenId: int--><!--Device-PermissionUsedTypeInfo-tokenId: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## usedType

```TypeScript
usedType: PermissionUsedType
```

Usage type of the sensitive permission.

**Type:** [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PermissionUsedTypeInfo-usedType: PermissionUsedType--><!--Device-PermissionUsedTypeInfo-usedType: PermissionUsedType-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

