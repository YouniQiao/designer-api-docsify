# queryApn

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## queryApn

```TypeScript
function queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>
```

Queries the APN ID. This API is suitable for enterprise mobile network configuration audit scenarios, such as finding APNs with specific configurations, verifying whether an APN configuration exists, and providing APN ID parameters for APN management operations. It helps enterprises locate and manage APN configurations, and supplies the necessary parameter information for updating and deleting APNs.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APN

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| apnInfo | Record & lt;string, string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |


## queryApn

```TypeScript
function queryApn(admin: Want, apnId: string): Record<string, string>
```

Queries the APN parameter information. This API is suitable for enterprise mobile network configuration audit scenarios, such as checking the configuration parameters of a specific APN, verifying whether the APN configuration is correct, and auditing mobile network access point settings. It helps enterprises review and validate APN configurations to ensure that mobile network settings meet requirements.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APN

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| apnId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Record & lt;string, string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
