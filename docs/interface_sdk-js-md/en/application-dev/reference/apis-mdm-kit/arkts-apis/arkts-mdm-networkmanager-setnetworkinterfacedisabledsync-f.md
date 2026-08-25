# setNetworkInterfaceDisabledSync

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## setNetworkInterfaceDisabledSync

```TypeScript
function setNetworkInterfaceDisabledSync(admin: Want, networkInterface: string, isDisabled: boolean): void
```

Disables the device from using the specified network interface. This API is suitable for enterprise network security management and control scenarios. It can be used to disable high-risk network interfaces, restrict devices from using specific network connections, and prevent data leaks through network interfaces. This helps enterprises reduce network security risks and prevent attacks or data leaks through specific network interfaces.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| networkInterface | string | Yes |
| isDisabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
