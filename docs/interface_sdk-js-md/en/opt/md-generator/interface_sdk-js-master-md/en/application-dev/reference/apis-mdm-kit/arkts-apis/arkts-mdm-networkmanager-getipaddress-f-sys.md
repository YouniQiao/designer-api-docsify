# getIpAddress (System API)

## Modules to Import

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## getIpAddress

```TypeScript
function getIpAddress(admin: Want, networkInterface: string, callback: AsyncCallback<string>): void
```

Obtains the device IP address based on the network interface. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getIpAddressSync](arkts-mdm-networkmanager-getipaddresssync-f.md#getIpAddressSync)

**Required permissions:** ohos.permission.ENTERPRISE_GET_NETWORK_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function getIpAddress(admin: Want, networkInterface: string, callback: AsyncCallback<string>): void--><!--Device-networkManager-function getIpAddress(admin: Want, networkInterface: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| networkInterface | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace parameters with actual values.
networkManager.getIpAddress(wantTemp, 'eth0', (err, result) => {
  if (err) {
    console.error(`Failed to get ip address. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting ip address, result : ${result}`);
});
```


## getIpAddress

```TypeScript
function getIpAddress(admin: Want, networkInterface: string): Promise<string>
```

Obtains the device IP address based on the network interface. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getIpAddressSync](arkts-mdm-networkmanager-getipaddresssync-f.md#getIpAddressSync)

**Required permissions:** ohos.permission.ENTERPRISE_GET_NETWORK_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function getIpAddress(admin: Want, networkInterface: string): Promise<string>--><!--Device-networkManager-function getIpAddress(admin: Want, networkInterface: string): Promise<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| networkInterface | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace parameters with actual values.
networkManager.getIpAddress(wantTemp, 'eth0').then((result) => {
  console.info(`Succeeded in getting ip address, result : ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get ip address. Code: ${err.code}, message: ${err.message}`);
});
```
