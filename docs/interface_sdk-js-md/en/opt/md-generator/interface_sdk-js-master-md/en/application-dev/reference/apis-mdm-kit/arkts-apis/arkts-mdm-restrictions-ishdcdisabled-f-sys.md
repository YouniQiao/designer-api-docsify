# isHdcDisabled (System API)

## Modules to Import

```TypeScript
import { restrictions } from '@kit.MDMKit';
```

## isHdcDisabled

```TypeScript
function isHdcDisabled(admin: Want, callback: AsyncCallback<boolean>): void
```

Queries whether HDC is disabled. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy)(admin: Want | null, feature: FeatureForDevice)

**Required permissions:** ohos.permission.ENTERPRISE_RESTRICT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function isHdcDisabled(admin: Want, callback: AsyncCallback<boolean>): void--><!--Device-restrictions-function isHdcDisabled(admin: Want, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

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
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

restrictions.isHdcDisabled(wantTemp, (err, result) => {
  if (err) {
    console.error(`Failed to query is hdc disabled or not. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying is hdc disabled : ${result}`);
})
```


## isHdcDisabled

```TypeScript
function isHdcDisabled(admin: Want): Promise<boolean>
```

Queries whether HDC is disabled. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy)(admin: Want | null, feature: FeatureForDevice)

**Required permissions:** ohos.permission.ENTERPRISE_RESTRICT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function isHdcDisabled(admin: Want): Promise<boolean>--><!--Device-restrictions-function isHdcDisabled(admin: Want): Promise<boolean>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

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
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

restrictions.isHdcDisabled(wantTemp).then((result) => {
  console.info(`Succeeded in querying is hdc disabled : ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query is hdc disabled or not. Code is ${err.code}, message is ${err.message}`);
})
```
