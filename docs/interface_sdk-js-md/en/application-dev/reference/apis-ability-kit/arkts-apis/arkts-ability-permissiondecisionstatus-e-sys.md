# PermissionDecisionStatus (System API)

Enumerates the permission decision statuses.

**Since:** 26.0.0

<!--Device-abilityAccessCtrl-export enum PermissionDecisionStatus--><!--Device-abilityAccessCtrl-export enum PermissionDecisionStatus-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## NEED_PERMISSION_DIALOG

```TypeScript
NEED_PERMISSION_DIALOG = 0
```

Indicates that a permission dialog needs to pop up.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionDecisionStatus-NEED_PERMISSION_DIALOG = 0--><!--Device-PermissionDecisionStatus-NEED_PERMISSION_DIALOG = 0-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## NO_DIALOG_DENIED

```TypeScript
NO_DIALOG_DENIED = 1
```

Indicates that no dialog is needed and the permission has been denied by the user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionDecisionStatus-NO_DIALOG_DENIED = 1--><!--Device-PermissionDecisionStatus-NO_DIALOG_DENIED = 1-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## NO_DIALOG_RESTRICTED

```TypeScript
NO_DIALOG_RESTRICTED = 2
```

Indicates that no dialog is needed and the permission is restricted by the system or policy.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionDecisionStatus-NO_DIALOG_RESTRICTED = 2--><!--Device-PermissionDecisionStatus-NO_DIALOG_RESTRICTED = 2-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## NO_DIALOG_GRANTED

```TypeScript
NO_DIALOG_GRANTED = 3
```

Indicates that no dialog is needed and the permission has been granted.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionDecisionStatus-NO_DIALOG_GRANTED = 3--><!--Device-PermissionDecisionStatus-NO_DIALOG_GRANTED = 3-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## NO_DIALOG_NOT_DECLARED

```TypeScript
NO_DIALOG_NOT_DECLARED = 4
```

Indicates that no dialog is needed, but the permission is not declared.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionDecisionStatus-NO_DIALOG_NOT_DECLARED = 4--><!--Device-PermissionDecisionStatus-NO_DIALOG_NOT_DECLARED = 4-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## NO_DIALOG_CLI_PERMISSION_RESOLVED

```TypeScript
NO_DIALOG_CLI_PERMISSION_RESOLVED = 5
```

Indicates that no dialog is needed and the CLI permission has been resolved to runtime permissions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionDecisionStatus-NO_DIALOG_CLI_PERMISSION_RESOLVED = 5--><!--Device-PermissionDecisionStatus-NO_DIALOG_CLI_PERMISSION_RESOLVED = 5-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

