# PermissionStateChangeInfo

Represents the permission state change details.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-abilityAccessCtrl-interface PermissionStateChangeInfo--><!--Device-abilityAccessCtrl-interface PermissionStateChangeInfo-End-->

**System capability:** SystemCapability.Security.AccessToken

## Modules to Import

```TypeScript
import { Context, Permissions, PermissionRequestResult } from '@kit.AbilityKit';
```

## change

```TypeScript
change: PermissionStateChangeType
```

Operation that triggers the permission state change.

**Type:** [PermissionStateChangeType](arkts-ability-abilityaccessctrl-permissionstatechangetype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PermissionStateChangeInfo-change: PermissionStateChangeType--><!--Device-PermissionStateChangeInfo-change: PermissionStateChangeType-End-->

**System capability:** SystemCapability.Security.AccessToken

## permissionName

```TypeScript
permissionName: Permissions
```

Permissions whose authorization state changes. For details about the permissions, see [Application Permissions](../../../security/AccessToken/app-permissions.md).

**Type:** [Permissions](arkts-ability-permissions-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PermissionStateChangeInfo-permissionName: Permissions--><!--Device-PermissionStateChangeInfo-permissionName: Permissions-End-->

**System capability:** SystemCapability.Security.AccessToken

## tokenID

```TypeScript
tokenID: int
```

ID of the subscribed application, which can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accessTokenId) field in ApplicationInfo of BundleInfo. &lt;br&gt;For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getBundleInfoSync).

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PermissionStateChangeInfo-tokenID: int--><!--Device-PermissionStateChangeInfo-tokenID: int-End-->

**System capability:** SystemCapability.Security.AccessToken

