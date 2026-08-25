# addAllowedNotificationBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## addAllowedNotificationBundles

```TypeScript
function addAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void
```

Adds applications to the notification trustlist. After the notification trustlist is set, applications not in the trustlist cannot send notifications.

> **NOTE：**&gt;
> 1. If both the Kiosk mode and the notification trustlist policy are set, applications in the Kiosk mode and those
> in the notification trustlist can send notifications.

> 2. If the device notification capability has been disabled via
> [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md), calling this API to
> set the notification trustlist will trigger error code 9200010.

> 3. The notification trustlist does not apply to system services, which can always send notifications. System
> applications are controlled by the notification trustlist.

> 4. Cross-user settings are supported. The settings take effect immediately.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleNames | Array & lt;string & gt; | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
