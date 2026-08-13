# setGlobalProxyForAccount

## Modules to Import

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## setGlobalProxyForAccount

```TypeScript
function setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void
```

Sets the network proxy for a specified user. This API is suitable for network management scenarios in enterprise environments with multiple users. For example, you can set different network proxy policies for different users, implement user-level network access control, and meet the network access requirements of different users, helping enterprises implement refined user-level network management.

**Since:** 15

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void--><!--Device-networkManager-function setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| [httpProxy](../../apis-network-kit/arkts-apis/arkts-network-ethernet-interfaceconfiguration-i-sys.md) | connection.HttpProxy | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let httpProxy: connection.HttpProxy = {
  // Replace with actual values.
  host: '192.168.xx.xxx',
  port: 8080,
  exclusionList: ['192.168', 'baidu.com']
};

try {
  // Replace parameters with actual values.
  networkManager.setGlobalProxyForAccount(wantTemp, httpProxy, 100);
  console.info(`Succeeded in setting network global proxy.`);
} catch (err) {
  console.error(`Failed to set network global proxy. Code: ${err.code}, message: ${err.message}`);
}
```
