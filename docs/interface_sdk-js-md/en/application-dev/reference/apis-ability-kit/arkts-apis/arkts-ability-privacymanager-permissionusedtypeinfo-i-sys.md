# PermissionUsedTypeInfo (System API)

表示某次权限使用类型的详情。

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

被访问的敏感权限名称。

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

访问敏感权限的应用身份标识。

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

敏感权限使用类型。

**Type:** [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PermissionUsedTypeInfo-usedType: PermissionUsedType--><!--Device-PermissionUsedTypeInfo-usedType: PermissionUsedType-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

