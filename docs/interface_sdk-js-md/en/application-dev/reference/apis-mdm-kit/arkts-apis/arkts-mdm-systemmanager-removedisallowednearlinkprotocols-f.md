# removeDisallowedNearLinkProtocols

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## removeDisallowedNearLinkProtocols

```TypeScript
function removeDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void
```

Removes the list of disallowed NearLink protocols for a specified user. After successful removal, the specified user can use the removed NearLink protocols for communication again, restoring the corresponding protocol connection capabilities. Use cases: In enterprise device management scenarios, administrators can use this API to remove previously set NearLink protocol disabling policies, allowing users to resume communication between devices via NearLink protocols. This is suitable for scenarios where there is a need to restore NearLink communication capabilities for specific users, helping enterprise administrators flexibly adjust NearLink protocol access permissions of user devices to meet communication requirements in different business scenarios.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| [protocols](../../apis-network-kit/arkts-apis/arkts-network-socket-tlssecureoptions-i.md) | Array&lt;[NearLinkProtocol](arkts-mdm-systemmanager-nearlinkprotocol-e.md)&gt; | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
