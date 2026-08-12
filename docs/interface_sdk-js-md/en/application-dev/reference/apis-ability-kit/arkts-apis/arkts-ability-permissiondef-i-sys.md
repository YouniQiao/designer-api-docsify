# PermissionDef (System API)

The module provides permission details defined in the  
[module.json5](../../../quick-start/module-configuration-file.md) file. The information can be obtained using  
[bundleManager.getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md#getPermissionDef).

> **NOTE：**
> 
> The APIs provided by this module are system APIs.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface PermissionDef--><!--Device-unnamed-export interface PermissionDef-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## descriptionId

```TypeScript
readonly descriptionId: long
```

ID of the permission description.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionDef-readonly descriptionId: long--><!--Device-PermissionDef-readonly descriptionId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## grantMode

```TypeScript
readonly grantMode: int
```

[Grant mode of the permission](../../../security/AccessToken/app-permission-mgmt-overview.md#authorization-mode).The value **0** means user authorization, and **1** means system authorization.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionDef-readonly grantMode: int--><!--Device-PermissionDef-readonly grantMode: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## labelId

```TypeScript
readonly labelId: long
```

ID of the permission label.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionDef-readonly labelId: long--><!--Device-PermissionDef-readonly labelId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## permissionName

```TypeScript
readonly permissionName: string
```

Name of the permission.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionDef-readonly permissionName: string--><!--Device-PermissionDef-readonly permissionName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

