# CliPermissionDetail (System API)

表示CLI指令声明的单个CLI权限的状态信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-abilityAccessCtrl-interface CliPermissionDetail--><!--Device-abilityAccessCtrl-interface CliPermissionDetail-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { Context, Permissions, PermissionRequestResult } from 'kits/@kit.AbilityKit';
```

## cliPermissionStatus

```TypeScript
cliPermissionStatus: PermissionDecisionStatus
```

CLI指令声明的CLI权限的决策状态。

**Type:** [PermissionDecisionStatus](arkts-ability-abilityaccessctrl-permissiondecisionstatus-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CliPermissionDetail-cliPermissionStatus: PermissionDecisionStatus--><!--Device-CliPermissionDetail-cliPermissionStatus: PermissionDecisionStatus-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## requiredCliPermission

```TypeScript
requiredCliPermission: Permissions
```

调用CLI所需的CLI权限。

**Type:** [Permissions](arkts-ability-permissions-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CliPermissionDetail-requiredCliPermission: Permissions--><!--Device-CliPermissionDetail-requiredCliPermission: Permissions-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## usedPermissions

```TypeScript
usedPermissions: Array<Permissions>
```

由requiredCliPermission映射出的运行时权限列表。

**Type:** Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CliPermissionDetail-usedPermissions: Array<Permissions>--><!--Device-CliPermissionDetail-usedPermissions: Array<Permissions>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

