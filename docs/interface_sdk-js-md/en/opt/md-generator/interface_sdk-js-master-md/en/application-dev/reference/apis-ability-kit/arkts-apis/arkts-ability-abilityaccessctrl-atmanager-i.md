# AtManager

Program access control management class, providing capabilities such as permission verification, runtime permission dialog box request, settings page authorization guidance, global switch request, and permission status monitoring. Obtain an instance through [createAtManager](arkts-ability-abilityaccessctrl-createatmanager-f.md#createatmanager).

**Since:** 23

<!--Device-abilityAccessCtrl-interface AtManager--><!--Device-abilityAccessCtrl-interface AtManager-End-->

**System capability:** SystemCapability.Security.AccessToken

## Modules to Import

```TypeScript
```

## checkAccessToken

```TypeScript
checkAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>
```

Verifies whether an app has been granted the specified permission. After the call is successful, the authorization status of the current permission is returned. The developer can decide accordingly whether to directly execute subsequent services, continue to initiate a permission request, or guide the user to go to system settings to modify the authorization status. This API uses a promise to return the result. Applicable to scenarios where a pre-permission check is performed before an app accesses protected resources such as the camera, microphone, or location.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AtManager-checkAccessToken(tokenID: int, permissionName: Permissions): Promise<GrantStatus>--><!--Device-AtManager-checkAccessToken(tokenID: int, permissionName: Permissions): Promise<GrantStatus>-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;GrantStatus & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a permission manager instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the bundleInfo of the app
let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
// Obtain the TokenID of the app
let tokenID: number = bundleInfo.appInfo.accessTokenId;
// Set the permission name to be verified
let permissionName: Permissions = 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS';
// Verify whether the app has been granted the permission
atManager.checkAccessToken(tokenID, permissionName).then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(`checkAccessToken success, result: ${data}`);
}).catch((err: BusinessError): void => {
  console.error(`checkAccessToken fail, code: ${err.code}, message: ${err.message}`);
});
```

## checkAccessTokenSync

```TypeScript
checkAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus
```

Verifies whether an app has been granted the specified permission, and synchronously returns the authorization status of the permission. The developer can decide accordingly whether to directly execute subsequent service processes, continue to initiate a permission request, or guide the user to go to the settings page to modify the authorization status. Compared with [checkAccessToken](#checkaccesstoken), this API returns the authorization status synchronously, making it suitable for permission verification scenarios that do not require asynchronous processing. Applicable to scenarios where a pre-permission check is performed before an app accesses protected resources such as the camera, microphone, or location.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AtManager-checkAccessTokenSync(tokenID: int, permissionName: Permissions): GrantStatus--><!--Device-AtManager-checkAccessTokenSync(tokenID: int, permissionName: Permissions): GrantStatus-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GrantStatus](arkts-ability-bundle-grantstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';

// Create a permission manager instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the bundleInfo of the app
let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
// Obtain the TokenID of the app
let tokenID: number = bundleInfo.appInfo.accessTokenId;
// Set the permission name to be verified
let permissionName: Permissions = 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS';
// Synchronously verify whether the app has been granted the permission
let data: abilityAccessCtrl.GrantStatus = atManager.checkAccessTokenSync(tokenID, permissionName);
console.info(`Result: ${data}`);
```

## getSelfPermissionStatus

```TypeScript
getSelfPermissionStatus(permissionName: Permissions): PermissionStatus
```

Queries the permission status of the current app and returns the result synchronously. After the call is successful, the status of the current permission is returned. Unlike [checkAccessToken](#checkaccesstoken), this API does not require passing in the app identity and is only used to query the permission status of the current app itself. Applicable to scenarios such as before determining whether to request a permission, confirming the authorization result after a permission request, or re-querying after monitoring a permission status change.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtManager-getSelfPermissionStatus(permissionName: Permissions): PermissionStatus--><!--Device-AtManager-getSelfPermissionStatus(permissionName: Permissions): PermissionStatus-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PermissionStatus](arkts-ability-abilityaccessctrl-permissionstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a permission management instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
try {
  // Query the permission status of the current app
  let data: abilityAccessCtrl.PermissionStatus = atManager.getSelfPermissionStatus('ohos.permission.CAMERA');
  console.info(`getSelfPermissionStatus success, result: ${data}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`getSelfPermissionStatus fail, code: ${error.code}, message: ${error.message}`);
}
```

## offSelfPermissionStateChange

```TypeScript
offSelfPermissionStateChange(
      permissionList: Array<Permissions>,
      callback?: Callback<PermissionStateChangeInfo>
    ): void
```

Unsubscribes from permission status change events for the specified permission list of itself. After the unsubscription is successful, status change notifications for the specified permission list will no longer be received. This API can be called to unsubscribe in scenarios such as when there is no need to continue monitoring permission changes, when the app exits, or when switching pages. When the callback parameter is not passed in, all callback functions associated with the permissionList will be deleted in batch. This API is usually used in conjunction with [onSelfPermissionStateChange](#onselfpermissionstatechange) to cancel the monitoring relationship created through on.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-offSelfPermissionStateChange(      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-offSelfPermissionStateChange(      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## off_selfPermissionStateChange

```TypeScript
off(
      type: 'selfPermissionStateChange',
      permissionList: Array<Permissions>,
      callback?: Callback<PermissionStateChangeInfo>
    ): void
```

Unsubscribes from permission status change events for the specified permission list of itself. After the unsubscription is successful, status change notifications for the specified permission list will no longer be received. This API can be called to unsubscribe in scenarios such as when there is no need to continue monitoring permission changes, when the app exits, or when switching pages. When the callback parameter is not passed in, all callback functions associated with the permissionList will be deleted in batch. This API is usually used in conjunction with [on](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#onpermissionstatechange) to cancel the monitoring relationship created through on.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtManager-off(      type: 'selfPermissionStateChange',      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-off(      type: 'selfPermissionStateChange',      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'selfPermissionStateChange' | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Create a permission management instance
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  // Set the permission list to unsubscribe from
  let permissionList: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION'];
  // Unsubscribe from permission status changes
  atManager.off('selfPermissionStateChange', permissionList);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Code: ${error.code}, message: ${error.message}`);
}
```

## onSelfPermissionStateChange

```TypeScript
onSelfPermissionStateChange(
      permissionList: Array<Permissions>,
      callback: Callback<PermissionStateChangeInfo>
    ): void
```

Subscribes to permission authorization status change events for a specified permission list of this app, using an asynchronous callback. It can be used in scenarios such as updating the UI or service logic in real time based on permission status, and monitoring user authorization behavior. When monitoring is no longer needed, call [offSelfPermissionStateChange](#offselfpermissionstatechange) to unsubscribe. - When this subscription API is called for multiple times, if the subscribed permission lists are the same but the callbacks are different, the subscription is successful. - When this subscription API is called for multiple times, if the subscribed permission lists contain the same subset and the callbacks are the same, the subscription fails. There are two possible scenarios when the permission status changes from "authorized" to "unauthorized": - User actively revokes: The system will terminate the corresponding app process. - System actively reclaims: The app process will not be terminated. A typical scenario is the one-time authorization of a security component, which is automatically reclaimed by the system after the authorization period ends. This API is usually used in conjunction with [offSelfPermissionStateChange](#offselfpermissionstatechange). When monitoring is no longer needed, call offSelfPermissionStateChange to unsubscribe.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-onSelfPermissionStateChange(      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-onSelfPermissionStateChange(      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100005](../errorcode-access-token.md#12100005-listener-overflows) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## on_selfPermissionStateChange

```TypeScript
on(
      type: 'selfPermissionStateChange',
      permissionList: Array<Permissions>,
      callback: Callback<PermissionStateChangeInfo>
    ): void
```

Subscribes to permission authorization status change events for a specified permission list of this app, using an asynchronous callback. It can be used in scenarios such as updating the UI or service logic in real time based on permission status, and monitoring user authorization behavior. When monitoring is no longer needed, call [off](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#offpermissionstatechange) to unsubscribe. - When this subscription API is called for multiple times, if the subscribed permission lists are the same but the callbacks are different, the subscription is successful. - When this subscription API is called for multiple times, if the subscribed permission lists contain the same subset and the callbacks are the same, the subscription fails. There are two possible scenarios when the permission status changes from "authorized" to "unauthorized": - User actively revokes: The system will terminate the corresponding app process. - System actively reclaims: The app process will not be terminated. A typical scenario is the one-time authorization of a security component, which is automatically reclaimed by the system after the authorization period ends. This API is usually used in conjunction with [off](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#offpermissionstatechange). When monitoring is no longer needed, call off to unsubscribe.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtManager-on(      type: 'selfPermissionStateChange',      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-on(      type: 'selfPermissionStateChange',      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'selfPermissionStateChange' | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100005](../errorcode-access-token.md#12100005-listener-overflows) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Create a permission management instance
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  // Set the list of permissions to subscribe to
  let permissionList: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION'];
  // Subscribe to permission status changes
  atManager.on('selfPermissionStateChange', permissionList, (data: abilityAccessCtrl.PermissionStateChangeInfo) => {
    console.info('receive permission state change');
    console.info(`data change: ${data.change}, tokenID: ${data.tokenID}, permission name: ${data.permissionName}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Code: ${error.code}, message: ${error.message}`);
}
```

## openPermissionOnSetting

```TypeScript
openPermissionOnSetting(context: Context, permission: Permissions): Promise<SelectedResult>
```

Used by [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#uiability)/ [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability) to bring up the permission settings page. After the call is successful, the permission settings page will be opened. After the user operates on the page, the user's selection result on the settings page will be returned. This API uses a promise to return the result. Applicable to scenarios where [manual_settings](../../../security/AccessToken/app-permission-mgmt-overview.md#manual_settings-manual-authorization) type permissions cannot be applied for through the normal authorization dialog box and the user must be guided to enter system settings to complete authorization. manual_settings type permissions are permissions that can only be manually enabled by the user in system settings and cannot be directly applied for through the normal authorization dialog box.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-openPermissionOnSetting(context: Context, permission: Permissions): Promise<SelectedResult>--><!--Device-AtManager-openPermissionOnSetting(context: Context, permission: Permissions): Promise<SelectedResult>-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | Yes |
| permission | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SelectedResult](arkts-ability-abilityaccessctrl-selectedresult-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
| [12100014](../errorcode-access-token.md#12100014-unexpected-permission) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |

**Examples**

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a permission manager instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// Launch the pop-up window for redirecting to the settings page
atManager.openPermissionOnSetting(context, 'ohos.permission.HOOK_KEY_EVENT').then((data: abilityAccessCtrl.SelectedResult) => {
  console.info(`openPermissionOnSetting success, result: ${data}`);
}).catch((err: BusinessError): void => {
  console.error(`openPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
});
```

## requestGlobalSwitch

```TypeScript
requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>
```

Used by UIAbility/UIExtensionAbility to bring up the global switch settings dialog box. After the call is successful, if the global switch is off, the global switch settings interface will pop up for the user to operate. If the global switch is already on, the dialog box will not be brought up and **true** will be returned. This API uses a promise to return the result. Applicable to scenarios that depend on system-level global switches (such as camera, microphone, and location) being turned on. When an app needs to use functions such as the camera, microphone, or location that require global switch control, if the corresponding global switch is turned off, the app can bring up this dialog box to request the user to turn on the corresponding function. If the current global switch status is on, the dialog box will not be brought up. &lt;!--RP5--&gt;  &lt;!--RP5End--&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtManager-requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>--><!--Device-AtManager-requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | Yes |
| type | [SwitchType](arkts-ability-abilityaccessctrl-switchtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
| [12100013](../errorcode-access-token.md#12100013-global-switch-enabled) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |

## requestPermissionOnSetting

```TypeScript
requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>
```

Used by [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#uiability)/ [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability) to bring up the permission settings dialog box for a second time, and returns an array of authorization statuses. This API uses a promise to return the result. Applicable to scenarios where the user has already denied the permission grant in the first dialog box and needs to continue applying for the permission through the settings page. Before calling this API, the app needs to call [requestPermissionsFromUser](#requestpermissionsfromuser) first. If the user has already authorized in the first dialog box, calling this API will not bring up the authorization dialog box. &lt;!--RP4--&gt;  &lt;!--RP4End--&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtManager-requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>--><!--Device-AtManager-requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;GrantStatus & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
| [12100010](../errorcode-access-token.md#12100010-pending-request) |
| [12100011](../errorcode-access-token.md#12100011-all-requested-permissions-granted) |
| [12100012](../errorcode-access-token.md#12100012-not-all-permissions-are-rejected-by-the-user) |
| [12100014](../errorcode-access-token.md#12100014-unexpected-permission) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>, requestCallback: AsyncCallback<PermissionRequestResult>) : void
```

Used by &lt;!--RP1--&gt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#uiability)&lt;!--RP1End--&gt; to bring up a dialog box to request [user authorization](../../../security/AccessToken/request-user-authorization.md), and returns the authorization result of the permissions requested this time. This API uses an asynchronous callback to return the result. Applicable to scenarios where an app proactively applies for [user_grant](../../../security/AccessToken/app-permission-mgmt-overview.md#user_grant-user-authorization) permissions from the user before accessing protected resources for the first time. If the user denies authorization, the authorization dialog box cannot be brought up again through this API. The developer can guide the user to go to the system settings interface for manual authorization, or call [requestPermissionOnSetting](#requestpermissiononsetting) to bring up the permission settings dialog box to guide the user to complete authorization. &lt;!--RP3--&gt;  &lt;!--RP3End--&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtManager-requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>, requestCallback: AsyncCallback<PermissionRequestResult>) : void--><!--Device-AtManager-requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>, requestCallback: AsyncCallback<PermissionRequestResult>) : void-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| requestCallback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PermissionRequestResult](arkts-ability-permissionrequestresult-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |

**Examples**

For details about the process and example of applying for user authorization, see [Requesting User Authorization](../../../security/AccessToken/request-user-authorization.md).

```TypeScript
import { abilityAccessCtrl, Context, PermissionRequestResult, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a permission manager instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// Request user authorization
atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'], (err: BusinessError, data: PermissionRequestResult) => {
  if (err) {
    console.error(`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`requestPermissionsFromUser success, result: ${data}`);
    console.info('requestPermissionsFromUser data permissions:' + data.permissions);
    console.info('requestPermissionsFromUser data authResults:' + data.authResults);
    console.info('requestPermissionsFromUser data dialogShownResults:' + data.dialogShownResults);
    console.info('requestPermissionsFromUser data errorReasons:' + data.errorReasons);
  }
});
```

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>) : Promise<PermissionRequestResult>
```

Used by &lt;!--RP1--&gt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#uiability)&lt;!--RP1End--&gt; to bring up a dialog box to request [user authorization](../../../security/AccessToken/request-user-authorization.md), and returns the authorization result of the permissions requested this time. This API uses a promise to return the result. Applicable to scenarios where an app proactively applies for user_grant permissions from the user before accessing protected resources for the first time. If the user denies authorization, the authorization dialog box cannot be brought up again through this API. The developer can guide the user to go to the system settings interface for manual authorization, or call [requestPermissionOnSetting](#requestpermissiononsetting) to bring up the permission settings dialog box to guide the user to complete authorization.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AtManager-requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>) : Promise<PermissionRequestResult>--><!--Device-AtManager-requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>) : Promise<PermissionRequestResult>-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PermissionRequestResult](arkts-ability-permissionrequestresult-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |

**Examples**

For details about the process and example of applying for user authorization, see [Requesting User Authorization](../../../security/AccessToken/request-user-authorization.md).

```TypeScript
import { abilityAccessCtrl, Context, PermissionRequestResult, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a permission manager instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// Request user authorization
atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']).then((data: PermissionRequestResult) => {
  console.info(`requestPermissionsFromUser success, result: ${data}`);
  console.info('requestPermissionsFromUser data permissions:' + data.permissions);
  console.info('requestPermissionsFromUser data authResults:' + data.authResults);
  console.info('requestPermissionsFromUser data dialogShownResults:' + data.dialogShownResults);
  console.info('requestPermissionsFromUser data errorReasons:' + data.errorReasons);
}).catch((err: BusinessError): void => {
  console.error(`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}`);
});
```

## verifyAccessToken

```TypeScript
verifyAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>
```

Verifies whether an app has been granted the specified permission. After the call is successful, the authorization status of the current permission is returned. The developer can decide accordingly whether to directly execute subsequent services, continue to initiate a permission request, or guide the user to go to system settings to modify the authorization status. This API uses a promise to return the result. Applicable to scenarios where a pre-permission check is performed before an app accesses protected resources. > **NOTE：**> You are advised to use [checkAccessToken](#checkaccesstoken).

**Since:** 23

<!--Device-AtManager-verifyAccessToken(tokenID: int, permissionName: Permissions): Promise<GrantStatus>--><!--Device-AtManager-verifyAccessToken(tokenID: int, permissionName: Permissions): Promise<GrantStatus>-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;GrantStatus & gt; |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a permission manager instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the bundleInfo of the app
let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
// Obtain the TokenID of the app
let tokenID: number = bundleInfo.appInfo.accessTokenId;
// Set the permission name to be verified
let permissionName: Permissions = 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS';
// Verify whether the app has been granted the permission
atManager.verifyAccessToken(tokenID, permissionName).then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(`verifyAccessToken success, result: ${data}`);
}).catch((err: BusinessError): void => {
  console.error(`verifyAccessToken fail, code: ${err.code}, message: ${err.message}`);
});
```

## verifyAccessToken

```TypeScript
verifyAccessToken(tokenID: number, permissionName: string): Promise<GrantStatus>
```

Verifies whether an app has been granted the specified permission. After the call is successful, the authorization status of the current permission is returned, and the developer can decide on subsequent operations accordingly. This API uses a promise to return the result. > **NOTE：**> This API is supported since API version 8 and deprecated since API version 9. It is recommended to use > [checkAccessToken](#checkaccesstoken) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [checkAccessToken](#checkaccesstoken)

<!--Device-AtManager-verifyAccessToken(tokenID: number, permissionName: string): Promise<GrantStatus>--><!--Device-AtManager-verifyAccessToken(tokenID: number, permissionName: string): Promise<GrantStatus>-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;GrantStatus & gt; |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a permission manager instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the bundleInfo of the app
let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
// Obtain the TokenID of the app
let tokenID: number = bundleInfo.appInfo.accessTokenId;
// Set the permission name to be verified
let permissionName: Permissions = 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS';
// Verify whether the app has been granted the permission
atManager.verifyAccessToken(tokenID, permissionName).then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(`verifyAccessToken success, result: ${data}`);
}).catch((err: BusinessError): void => {
  console.error(`verifyAccessToken fail, code: ${err.code}, message: ${err.message}`);
});
```

## verifyAccessTokenSync

```TypeScript
verifyAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus
```

Verifies whether an app has been granted the specified permission, and synchronously returns the authorization status of the permission. The developer can decide accordingly whether to directly execute subsequent service processes, continue to initiate a permission request, or guide the user to go to system settings to modify the authorization status. Applicable to scenarios where a pre-permission check is performed before an app accesses protected resources such as the camera, microphone, or location. It is recommended to use [checkAccessTokenSync](#checkaccesstokensync) instead.

**Since:** 23

<!--Device-AtManager-verifyAccessTokenSync(tokenID: int, permissionName: Permissions): GrantStatus--><!--Device-AtManager-verifyAccessTokenSync(tokenID: int, permissionName: Permissions): GrantStatus-End-->

**System capability:** SystemCapability.Security.AccessToken

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GrantStatus](arkts-ability-bundle-grantstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a permission manager instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the bundleInfo of the app
let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
// Obtain the TokenID of the app
let tokenID: number = bundleInfo.appInfo.accessTokenId;
try {
  // Set the permission name to be verified
  let permissionName: Permissions = 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS';
  // Synchronously verify whether the app has been granted the permission
  let data: abilityAccessCtrl.GrantStatus = atManager.verifyAccessTokenSync(tokenID, permissionName);
  console.info(`verifyAccessTokenSync success, result: ${data}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`verifyAccessTokenSync fail, code: ${error.code}, message: ${error.message}`);
}
```
