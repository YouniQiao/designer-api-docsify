# PermissionUsedType (System API)

Enumerates the means for using a sensitive permission.  
| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Value](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-value-t.md) | Description | | ----------------------- | -- | ---------------- | | [NORMAL_TYPE](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 0 | The sensitive permission is used after authorization through a dialog box or a system settings page. | | [PICKER_TYPE](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 1 | Indicates that a sensitive permission is used through a PICKER service, but this method does not grant the permission. | | [SECURITY_COMPONENT_TYPE](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 2 |

**Since:** 12

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## NORMAL_TYPE

```TypeScript
NORMAL_TYPE = 0
```

Sensitive resources are accessed with the declared permission or permission granted by the user.

**Since:** 12

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## PICKER_TYPE

```TypeScript
PICKER_TYPE = 1
```

Sensitive resources are accessed through a picker.

**Since:** 12

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## SECURITY_COMPONENT_TYPE

```TypeScript
SECURITY_COMPONENT_TYPE = 2
```

Sensitive resources are accessed through a security component.

**Since:** 12

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.
