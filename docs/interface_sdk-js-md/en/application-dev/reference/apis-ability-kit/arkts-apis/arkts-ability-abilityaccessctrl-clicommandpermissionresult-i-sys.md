# CliCommandPermissionResult (System API)

表示单条CLI命令的权限信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-abilityAccessCtrl-interface CliCommandPermissionResult--><!--Device-abilityAccessCtrl-interface CliCommandPermissionResult-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { Context, Permissions, PermissionRequestResult } from 'kits/@kit.AbilityKit';
```

## requiredCliPermissions

```TypeScript
requiredCliPermissions: Array<CliPermissionDetail>
```

当前CLI命令依赖的CLI权限信息列表。

**Type:** Array&lt;CliPermissionDetail&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CliCommandPermissionResult-requiredCliPermissions: Array<CliPermissionDetail>--><!--Device-CliCommandPermissionResult-requiredCliPermissions: Array<CliPermissionDetail>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

