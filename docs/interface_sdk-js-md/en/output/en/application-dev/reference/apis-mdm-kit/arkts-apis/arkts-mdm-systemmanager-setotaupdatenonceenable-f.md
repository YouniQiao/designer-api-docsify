# setOtaUpdateNonceEnable

## setOtaUpdateNonceEnable

```TypeScript
function setOtaUpdateNonceEnable(admin: Want, isEnable: boolean): void
```

Sets whether to enable nonce for OTA update (nonce is enabled by default). When nonce is enabled, the system verifies the validity of the nonce during the OTA update process to prevent replay attacks and enhance system security. > **NOTE** > > To ensure system security, it is not advised to disable nonce verification unless required by specific use cases > such as intranet updates.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function setOtaUpdateNonceEnable(admin: Want, isEnable: boolean): void--><!--Device-systemManager-function setOtaUpdateNonceEnable(admin: Want, isEnable: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| isEnable | boolean | Yes | The value **true** means to enable nonce for OTA update, and the value **false** means to disable nonce for OTA update. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Failed to call the API due to limited device capabilities. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |

