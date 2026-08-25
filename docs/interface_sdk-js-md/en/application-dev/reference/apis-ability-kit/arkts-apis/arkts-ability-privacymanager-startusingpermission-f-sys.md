# startUsingPermission (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## startUsingPermission

```TypeScript
function startUsingPermission(tokenID: number, permissionName: Permissions): Promise<void>
```

A system application can call this API to report the application's permission usage status in the foreground or background to the system. The privacy service notifies all subscribers of this permission usage status change event (refer to [on](arkts-ability-privacymanager-on-f-sys.md) for the subscription method). This API uses a promise to return the result.After starting to use a permission, [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md) must be called to stop using the permission when the usage ends.

**Since:** 9

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |


## startUsingPermission

```TypeScript
function startUsingPermission(
    tokenID: number,
    permissionName: Permissions,
    pid?: number,
    usedType?: PermissionUsedType
  ): Promise<void>
```

A system application can call this API to report the application's permission usage status in the foreground or background to the system. The privacy service notifies all subscribers of this permission usage status change event (refer to [on](arkts-ability-privacymanager-on-f-sys.md) for the subscription method). This API uses a promise to return the result.After starting to use a permission, [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md) must be called to stop using the permission when the usage ends.

**Since:** 18

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| pid | number | No |
| usedType | [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |


## startUsingPermission

```TypeScript
function startUsingPermission(
     tokenID: number,
     permissionName: Permissions,
     pid?: number,
     usedType?: PermissionUsedType,
     options?: PermissionUsingOptions
   ): Promise<void>
```

A system application can call this API to report the application's permission usage status in the foreground or background to the system. The privacy service notifies all subscribers of this permission usage status change event (refer to [on](arkts-ability-privacymanager-on-f-sys.md) for the subscription method). This API uses a promise to return the result.After starting to use a permission, [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md) must be called to stop using the permission when the usage ends.When a pid is passed in, the pid must be the same as the pid passed into [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md). If the pairing relationship is not satisfied, error code 12100004 is returned.

**Since:** 26.0.0

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| pid | number | No |
| usedType | [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | No |
| options | [PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |


## startUsingPermission

```TypeScript
function startUsingPermission(
    tokenID: number,
    permissionName: Permissions,
    callback: AsyncCallback<void>
  ): void
```

A system application can call this API to report the application's permission usage status in the foreground or background to the system. The privacy service notifies all subscribers of this permission usage status change event (refer to [on](arkts-ability-privacymanager-on-f-sys.md) for the subscription method). This API uses an asynchronous callback to return the result.After starting to use a permission, [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md) must be called to stop using the permission when the usage ends.

**Since:** 9

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |
