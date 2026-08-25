# setSimDisabled

## Modules to Import

```TypeScript
import { telephonyManager } from 'kits/@kit.MDMKit';
```

## setSimDisabled

```TypeScript
function setSimDisabled(admin: Want, slotId: number): void
```

Disables the SIM card in the specified slot. After being disabled, the SIM card in the specified slot cannot be used for making or receiving calls, sending or receiving SMSs, or accessing the internet. For example, an enterprise device administrator can disable the SIM card when an employee leaves the company or a device is lost, preventing unauthorized use. This is applicable in scenarios where enterprises need to restrict employee devices'communication capabilities, such as preventing SIM card misuse after employee departure or device loss, thereby ensuring enterprise communication security and cost control.

**Since:** 20

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
