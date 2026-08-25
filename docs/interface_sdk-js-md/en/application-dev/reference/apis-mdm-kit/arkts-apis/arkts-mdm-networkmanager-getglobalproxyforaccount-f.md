# getGlobalProxyForAccount

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## getGlobalProxyForAccount

```TypeScript
function getGlobalProxyForAccount(admin: Want | null, accountId: number): connection.HttpProxy
```

Obtains the network proxy for a specified user. This API is suitable for network management scenarios in enterprise environments with multiple users, such as auditing user-level network proxy configurations, verifying user network access policies, and troubleshooting user network access issues. It helps enterprises check and verify user-level network management policies.

> **NOTE：**&gt;
> This API is used to obtain the proxy configuration of a specified user set by the **setGlobalProxyForAccount**
> API. To obtain the global proxy configuration that applies to all users, you are advised to use the
> [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md) API.

**Since:** 15

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| connection.HttpProxy |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
