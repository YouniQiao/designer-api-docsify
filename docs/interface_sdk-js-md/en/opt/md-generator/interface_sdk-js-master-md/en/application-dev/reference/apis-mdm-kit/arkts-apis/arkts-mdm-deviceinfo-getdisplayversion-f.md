# getDisplayVersion

## Modules to Import

```TypeScript
import { deviceInfo } from 'kits/@kit.MDMKit';
```

## getDisplayVersion

```TypeScript
function getDisplayVersion(admin: Want, callback: AsyncCallback<string>): void
```

Obtains the device version number. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [deviceInfo.getDeviceInfo](arkts-mdm-deviceinfo-getdeviceinfo-f.md#getdeviceinfo)

**Required permissions:** ohos.permission.ENTERPRISE_GET_DEVICE_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceInfo-function getDisplayVersion(admin: Want, callback: AsyncCallback<string>): void--><!--Device-deviceInfo-function getDisplayVersion(admin: Want, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { deviceInfo } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

deviceInfo.getDisplayVersion(wantTemp, (err, result) => {
  if (err) {
    console.error(`Failed to get display version. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting display version, result : ${result}`);
});
```


## getDisplayVersion

```TypeScript
function getDisplayVersion(admin: Want): Promise<string>
```

Obtains the device version number. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [deviceInfo.getDeviceInfo](arkts-mdm-deviceinfo-getdeviceinfo-f.md#getdeviceinfo)

**Required permissions:** ohos.permission.ENTERPRISE_GET_DEVICE_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceInfo-function getDisplayVersion(admin: Want): Promise<string>--><!--Device-deviceInfo-function getDisplayVersion(admin: Want): Promise<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { deviceInfo } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

deviceInfo.getDisplayVersion(wantTemp).then((result) => {
  console.info(`Succeeded in getting display version, result : ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get display version. Code: ${err.code}, message: ${err.message}`);
});
```
