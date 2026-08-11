# setEthernetConfig

## setEthernetConfig

```TypeScript
function setEthernetConfig(admin: Want, networkInterface: string, config: InterfaceConfig): void
```

设置特定以太网网络接口的IP地址。适用于企业网络管理场景，例如配置设备静态IP地址、统一管理企业网络设备IP分配、设置网络参数，帮助企业集中管理网络配置，确保设备网络参数符合企业网络管理策略。

**起始版本：** 23

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-networkManager-function setEthernetConfig(admin: Want, networkInterface: string, config: InterfaceConfig): void--><!--Device-networkManager-function setEthernetConfig(admin: Want, networkInterface: string, config: InterfaceConfig): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| networkInterface | string | 是 |
| config | [InterfaceConfig](arkts-mdm-networkmanager-interfaceconfig-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9201010](../errorcode-enterpriseDeviceManager.md#9201010-以太网网络接口配置失败) |

## 示例

```TypeScript
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let config: networkManager.InterfaceConfig = {
  // 需根据实际情况进行替换
  "ipSetMode": networkManager.IpSetMode.STATIC,
  "ipAddress": "192.168.1.121",
  "gateway": "192.168.1.1",
  "netMask": "255.255.255.0",
  "dnsServers": "192.168.1.1"
}
let networkInterface: string = "eth0"; // 需根据实际情况进行替换
try {
  networkManager.setEthernetConfig(wantTemp, networkInterface, config);
  console.info('Succeeded in setting ethernet config.');
} catch (err) {
  console.error(`Failed to set ethernet config. Code: ${err.code}, message: ${err.message}`);
}
```
