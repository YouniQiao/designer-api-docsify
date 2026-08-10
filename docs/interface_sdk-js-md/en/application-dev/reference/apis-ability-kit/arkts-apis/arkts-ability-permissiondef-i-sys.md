# PermissionDef (System API)

[module.json5配置文件](../../../quick-start/module-configuration-file.md)中定义的权限详细信息，通过接口  
[bundleManager.getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md#getpermissiondef)获取。

> **说明：**
> 
> 本模块为系统接口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface PermissionDef--><!--Device-unnamed-export interface PermissionDef-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## descriptionId

```TypeScript
readonly descriptionId: long
```

描述权限的ID。

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

[权限的授予方式](../../../security/AccessToken/app-permission-mgmt-overview.md#授权方式)。0：表示用户授权，1：表示系统授权。

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

权限的标签ID。

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

用户权限名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionDef-readonly permissionName: string--><!--Device-PermissionDef-readonly permissionName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

