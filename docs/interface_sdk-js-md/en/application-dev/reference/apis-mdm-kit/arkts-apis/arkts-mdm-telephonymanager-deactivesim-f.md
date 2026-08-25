# deactiveSim

## Modules to Import

```TypeScript
import { telephonyManager } from '@kit.MDMKit';
```

## deactiveSim

```TypeScript
function deactiveSim(admin: Want, slotId: number): void
```

Deactivates the SIM card in the specified slot. After deactivation, the SIM card in that slot cannot be used for making or receiving calls, sending or receiving SMSs, or accessing the internet. For example, an enterprise can temporarily deactivate a SIM card during employee leave or device maintenance. To successfully call this API, the SIM card must be inserted and airplane mode must be turned off.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| slotId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201017](../errorcode-enterpriseDeviceManager.md#9201017-failed-to-enable-or-disable-the-sim-card) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
