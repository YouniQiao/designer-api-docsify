# removeHideLauncherIcon

## removeHideLauncherIcon

```TypeScript
function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void
```

Removes applications from the home screen icon hide list. > **NOTE** > > After unhiding, applications will be placed in the first available slot starting from the second screen of the > home screen. If no empty slot is found on screens 2 to 18, it will search for an empty slot on the first screen. > If no empty slot is available on the first screen, a small folder will be created at the position of the first > application on the second screen to contain the applications.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void--><!--Device-applicationManager-function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleNames | Array&lt;string&gt; | Yes | Application bundle name array, which specifies the applications to be unhidden. A maximum of 500 applications are supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Failed to call the API due to limited device capabilities. |

