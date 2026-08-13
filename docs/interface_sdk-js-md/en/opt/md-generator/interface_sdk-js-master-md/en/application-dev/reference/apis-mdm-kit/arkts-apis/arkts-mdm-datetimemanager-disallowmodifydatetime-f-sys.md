# disallowModifyDateTime (System API)

## Modules to Import

```TypeScript
import { dateTimeManager } from '@kit.MDMKit';
```

## disallowModifyDateTime

```TypeScript
function disallowModifyDateTime(admin: Want, disallow: boolean, callback: AsyncCallback<void>): void
```

Disallows the device to modify the system time. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy)(admin: Want, feature: FeatureForDevice, disallow: boolean)

**Required permissions:** ohos.permission.ENTERPRISE_SET_DATETIME

**Model restriction:** This API can be used only in the stage model.

<!--Device-dateTimeManager-function disallowModifyDateTime(admin: Want, disallow: boolean, callback: AsyncCallback<void>): void--><!--Device-dateTimeManager-function disallowModifyDateTime(admin: Want, disallow: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| disallow | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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
import { dateTimeManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

dateTimeManager.disallowModifyDateTime(wantTemp, true, (err) => {
  if (err) {
    console.error(`Failed to disallow modify date time. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in disallowing modify date time');
})
```


## disallowModifyDateTime

```TypeScript
function disallowModifyDateTime(admin: Want, disallow: boolean): Promise<void>
```

Disallows the device to modify the system time. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy)(admin: Want, feature: FeatureForDevice, disallow: boolean)

**Required permissions:** ohos.permission.ENTERPRISE_SET_DATETIME

**Model restriction:** This API can be used only in the stage model.

<!--Device-dateTimeManager-function disallowModifyDateTime(admin: Want, disallow: boolean): Promise<void>--><!--Device-dateTimeManager-function disallowModifyDateTime(admin: Want, disallow: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| disallow | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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
import { dateTimeManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

dateTimeManager.disallowModifyDateTime(wantTemp, true).then(() => {
  console.info('Succeeded in disallowing modify date time');
}).catch((err: BusinessError) => {
  console.error(`Failed to disallow modify date time. Code is ${err.code}, message is ${err.message}`);
})
```
