# setScreenLockDisabledForAccount

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## setScreenLockDisabledForAccount

```TypeScript
function setScreenLockDisabledForAccount(admin: Want, disable: boolean): void
```

Disables or enables swipe-to-unlock for the current user. When enabled, the user must swipe on the screen after the screen is turned on to access the home screen. When disabled, the screen goes directly to the home screen after being turned on. This API is suitable for enterprise device management scenarios, such as disabling swipe-to-unlock in specific security environments to simplify operations, or enabling it in general scenarios as a basic security measure.

> **NOTE：**&gt;
> 1. This API takes effect only when no lock screen password is set on the device.&gt;
> 2. By default, swipe-to-unlock is enabled on the device.&gt;
> 3. If a lock screen password exists on the device, attempting to disable swipe-to-unlock will fail and return
> error code 9201021.&gt;
> 4. After a policy to disable swipe-to-unlock is applied, if the user subsequently sets a device password, the
> password will take effect and the device will require password verification before entering the home screen. In
> this case, the previously applied policy will no longer take effect.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| disable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9201021](../errorcode-enterpriseDeviceManager.md#9201021-the-device-has-a-screen-lock-password) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
