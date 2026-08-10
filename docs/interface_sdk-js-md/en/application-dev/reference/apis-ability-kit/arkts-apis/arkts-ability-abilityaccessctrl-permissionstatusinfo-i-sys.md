# PermissionStatusInfo (System API)

表示权限状态信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-abilityAccessCtrl-interface PermissionStatusInfo--><!--Device-abilityAccessCtrl-interface PermissionStatusInfo-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { Context, Permissions, PermissionRequestResult } from 'kits/@kit.AbilityKit';
```

## grantFlags

```TypeScript
grantFlags: int
```

权限标志，取值范围如下：  
- 0：用户未设置该权限。  
- 1：用户已设置该权限，若权限未授予，允许再次弹出权限弹窗请求授权。  
- 2：用户已设置该权限，若权限未授予，不允许再次弹出权限弹窗请求授权，需用户在系统设置中授权。  
- 4：系统已设置该权限。  
- 8：系统已预授权该权限，且允许取消授权。  
- 16：安全控件已设置该权限。  
- 32：安全策略已固定该权限，用户不能授权或取消授权。  
- 64：仅在当前生命周期前台期间允许使用该权限。  
- 128：管理员策略已固定该权限，用户不能授权或取消授权，管理员可取消固定。  
- 256：管理员策略取消固定该权限，用户可授权或取消授权。  
- 512：用户策略限制该权限。  
取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionStatusInfo-grantFlags: int--><!--Device-PermissionStatusInfo-grantFlags: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## grantStatus

```TypeScript
grantStatus: GrantStatus
```

权限授权状态。

**Type:** [GrantStatus](arkts-ability-bundle-grantstatus-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionStatusInfo-grantStatus: GrantStatus--><!--Device-PermissionStatusInfo-grantStatus: GrantStatus-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## grantTimestamp

```TypeScript
grantTimestamp?: long
```

授权状态变化的时间戳。该字段为可选字段，当权限状态变化时返回。单位为：毫秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionStatusInfo-grantTimestamp?: long--><!--Device-PermissionStatusInfo-grantTimestamp?: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## permissionName

```TypeScript
permissionName: Permissions
```

权限名称。

**Type:** [Permissions](arkts-ability-permissions-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionStatusInfo-permissionName: Permissions--><!--Device-PermissionStatusInfo-permissionName: Permissions-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## tokenID

```TypeScript
tokenID: int
```

应用的身份标识。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionStatusInfo-tokenID: int--><!--Device-PermissionStatusInfo-tokenID: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

