# operateDevice

## Modules to Import

```TypeScript
import { deviceControl } from 'kits/@kit.MDMKit';
```

## operateDevice

```TypeScript
function operateDevice(admin: Want, operate: string, addition?: string): void
```

Allows administrators to perform operations such as factory reset, restart, shutdown, and screen lock on devices. For example, in enterprise device management scenarios, administrators can remotely control employee devices to perform factory reset, restart, shutdown, or screen lock operations.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_OPERATE_DEVICE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| operate | string | Yes |
| [addition](../../apis-test-kit/arkts-apis/arkts-test-uitest-inputtextmode-i.md) | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## operateDevice

```TypeScript
function operateDevice(admin: Want, operation: Operation, addition?: string): void
```

Allows the administrator to operate devices, for example, erasing disks.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_OPERATE_DEVICE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| operation | [Operation](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-operation-e.md) | Yes |
| [addition](../../apis-test-kit/arkts-apis/arkts-test-uitest-inputtextmode-i.md) | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| 9201048 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
