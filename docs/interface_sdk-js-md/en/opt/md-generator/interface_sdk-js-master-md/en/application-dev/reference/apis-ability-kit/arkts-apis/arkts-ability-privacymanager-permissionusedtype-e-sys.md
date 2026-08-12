# PermissionUsedType (System API)

Enumerates the means for using a sensitive permission.

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Value](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-value-i.md) | Description |
| ----------------------- | -- | ---------------- |
| [NORMAL_TYPE](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 0 | The sensitive permission is used after authorization through a dialog box or a system settings page. |
| [PICKER_TYPE](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 1 | Indicates that a sensitive permission is used through a PICKER service, but this method does not grant the permission. |
| [SECURITY_COMPONENT_TYPE](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 2 |

**Since:** 12

<!--Device-privacyManager-enum PermissionUsedType--><!--Device-privacyManager-enum PermissionUsedType-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## NORMAL_TYPE

```TypeScript
NORMAL_TYPE = 0
```

Sensitive resources are accessed with the declared permission or permission granted by the user.

**Since:** 12

<!--Device-PermissionUsedType-NORMAL_TYPE = 0--><!--Device-PermissionUsedType-NORMAL_TYPE = 0-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## PICKER_TYPE

```TypeScript
PICKER_TYPE = 1
```

Sensitive resources are accessed through a picker.

**Since:** 12

<!--Device-PermissionUsedType-PICKER_TYPE = 1--><!--Device-PermissionUsedType-PICKER_TYPE = 1-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## SECURITY_COMPONENT_TYPE

```TypeScript
SECURITY_COMPONENT_TYPE = 2
```

Sensitive resources are accessed through a security component.

**Since:** 12

<!--Device-PermissionUsedType-SECURITY_COMPONENT_TYPE = 2--><!--Device-PermissionUsedType-SECURITY_COMPONENT_TYPE = 2-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.
