# PermissionStateChangeInfo

Represents the permission state change details.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-abilityAccessCtrl-interface PermissionStateChangeInfo--><!--Device-abilityAccessCtrl-interface PermissionStateChangeInfo-End-->

**System capability:** SystemCapability.Security.AccessToken

## change

```TypeScript
change: PermissionStateChangeType
```

Operation that triggers the permission state change.

**Type:** PermissionStateChangeType

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PermissionStateChangeInfo-change: PermissionStateChangeType--><!--Device-PermissionStateChangeInfo-change: PermissionStateChangeType-End-->

**System capability:** SystemCapability.Security.AccessToken

## permissionName

```TypeScript
permissionName: Permissions
```

Permissions whose authorization state changes. For details about the permissions, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** Permissions

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PermissionStateChangeInfo-permissionName: Permissions--><!--Device-PermissionStateChangeInfo-permissionName: Permissions-End-->

**System capability:** SystemCapability.Security.AccessToken

## tokenID

```TypeScript
tokenID: int
```

ID of the subscribed application, which can be obtained through the [accessTokenId]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ field in ApplicationInfo of BundleInfo. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PermissionStateChangeInfo-tokenID: int--><!--Device-PermissionStateChangeInfo-tokenID: int-End-->

**System capability:** SystemCapability.Security.AccessToken

