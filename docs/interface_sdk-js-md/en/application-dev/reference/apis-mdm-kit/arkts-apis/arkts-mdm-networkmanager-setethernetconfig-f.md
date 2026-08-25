# setEthernetConfig

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## setEthernetConfig

```TypeScript
function setEthernetConfig(admin: Want, networkInterface: string, config: InterfaceConfig): void
```

Sets the IP address of a specific Ethernet interface. This API is suitable for enterprise network management scenarios, such as configuring static IP addresses for devices, centrally managing IP address allocation for enterprise network devices, and setting network parameters. It helps enterprises centrally manage network configurations and ensures that device network parameters comply with enterprise network management policies.

**Since:** 23

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| networkInterface | string | Yes |
| config | [InterfaceConfig](arkts-mdm-networkmanager-interfaceconfig-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201010](../errorcode-enterpriseDeviceManager.md#9201010-failed-to-configure-the-ethernet-network-interface) |
| [201](../../errorcode-universal.md#201-permission-denied) |
