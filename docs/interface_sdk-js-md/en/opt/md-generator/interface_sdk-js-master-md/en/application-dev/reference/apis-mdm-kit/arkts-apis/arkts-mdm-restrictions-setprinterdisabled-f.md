# setPrinterDisabled

## Modules to Import

```TypeScript
import { restrictions } from '@kit.MDMKit';
```

## setPrinterDisabled

```TypeScript
function setPrinterDisabled(admin: Want, disabled: boolean, callback: AsyncCallback<void>): void
```

Enables or disables the printing capability of the device. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [setDisallowedPolicy](restrictions.setDisallowedPolicy(admin:)

**Required permissions:** ohos.permission.ENTERPRISE_RESTRICT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function setPrinterDisabled(admin: Want, disabled: boolean, callback: AsyncCallback<void>): void--><!--Device-restrictions-function setPrinterDisabled(admin: Want, disabled: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| disabled | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

restrictions.setPrinterDisabled(wantTemp, true, (err) => {
  if (err) {
    console.error(`Failed to set printer disabled. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting printer disabled');
})
```


## setPrinterDisabled

```TypeScript
function setPrinterDisabled(admin: Want, disabled: boolean): Promise<void>
```

Enables or disables the printing capability of the device. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [setDisallowedPolicy](restrictions.setDisallowedPolicy(admin:)

**Required permissions:** ohos.permission.ENTERPRISE_RESTRICT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function setPrinterDisabled(admin: Want, disabled: boolean): Promise<void>--><!--Device-restrictions-function setPrinterDisabled(admin: Want, disabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| disabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

restrictions.setPrinterDisabled(wantTemp, true).then(() => {
  console.info('Succeeded in setting printer disabled');
}).catch((err: BusinessError) => {
  console.error(`Failed to set printer disabled. Code is ${err.code}, message is ${err.message}`);
})
```
