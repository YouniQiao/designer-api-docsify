# removeDockApp

## removeDockApp

```TypeScript
function removeDockApp(admin: Want, bundleName: string, abilityName: string): void
```

Removes an application from the shortcut bar. > **NOTE** > > The following applications cannot be removed from the shortcut bar using this API: Application Center, Task > Center, Files, and Recycle Bin. Otherwise, error code 9201018 will be reported.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function removeDockApp(admin: Want, bundleName: string, abilityName: string): void--><!--Device-applicationManager-function removeDockApp(admin: Want, bundleName: string, abilityName: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the application. |
| abilityName | string | Yes | Ability name of the application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9201016](../errorcode-enterpriseDeviceManager.md#9201016-specified-application-not-in-dock) | The application has not been added to the Dock. |
| [9201018](../errorcode-enterpriseDeviceManager.md#9201018-specified-application-inoperable) | The application is inoperable. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Failed to call the API due to limited device capabilities. |

