# setGlobalProxySync

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## setGlobalProxySync

```TypeScript
function setGlobalProxySync(admin: Want, httpProxy: connection.HttpProxy): void
```

Sets the global network proxy. This API is suitable for enterprise network management scenarios, such as setting a unified network proxy for an enterprise, implementing network access audit, controlling network access paths, and optimizing network performance. It helps enterprises centrally manage network access, making network access auditable and controllable.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| [httpProxy](../../apis-network-kit/arkts-apis/arkts-network-ethernet-interfaceconfiguration-i-sys.md) | connection.HttpProxy | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
