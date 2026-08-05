# ActiveChangeResponse (System API)

Defines the detailed permission usage information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface ActiveChangeResponse--><!--Device-privacyManager-interface ActiveChangeResponse-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## activeStatus

```TypeScript
activeStatus: PermissionActiveStatus
```

Permission usage status.

**Type:** PermissionActiveStatus

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ActiveChangeResponse-activeStatus: PermissionActiveStatus--><!--Device-ActiveChangeResponse-activeStatus: PermissionActiveStatus-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## callingTokenId

```TypeScript
callingTokenId?: int
```

Identity of the caller application. This field is invalid when **activeStatus** is **INACTIVE**. Default value: **0**.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ActiveChangeResponse-callingTokenId?: int--><!--Device-ActiveChangeResponse-callingTokenId?: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## deviceId

```TypeScript
deviceId: string
```

ID of the device where the permission usage status change occurred.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ActiveChangeResponse-deviceId: string--><!--Device-ActiveChangeResponse-deviceId: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## enhancedIdentity

```TypeScript
enhancedIdentity?: string
```

Extension identity, used to identify additional identity information of the caller. This field is returned when it is necessary to distinguish permission usage records from different call sources within the same application. The maximum length is 48. Default value: Empty string.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActiveChangeResponse-enhancedIdentity?: string--><!--Device-ActiveChangeResponse-enhancedIdentity?: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## permissionName

```TypeScript
permissionName: Permissions
```

Name of the permission whose usage status has changed.

**Type:** Permissions

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ActiveChangeResponse-permissionName: Permissions--><!--Device-ActiveChangeResponse-permissionName: Permissions-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## tokenId

```TypeScript
tokenId: int
```

Token ID of the application whose permission usage changes are subscribed to.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ActiveChangeResponse-tokenId: int--><!--Device-ActiveChangeResponse-tokenId: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## usedType

```TypeScript
usedType?: PermissionUsedType
```

Sensitive permission usage type. This value is invalid when activeStatus is INACTIVE. Default value: NORMAL\_TYPE.

**Type:** PermissionUsedType

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ActiveChangeResponse-usedType?: PermissionUsedType--><!--Device-ActiveChangeResponse-usedType?: PermissionUsedType-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

