# isModifyDateTimeDisallowed (System API)

## Modules to Import

```TypeScript
import { dateTimeManager } from 'kits/@kit.MDMKit';
```

## isModifyDateTimeDisallowed

```TypeScript
function isModifyDateTimeDisallowed(admin: Want, callback: AsyncCallback<boolean>): void
```

Queries whether the system time of a device can be modified. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.enterprise.restrictions:restrictions.getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy)(admin:

**Required permissions:** ohos.permission.ENTERPRISE_SET_DATETIME

**Model restriction:** This API can be used only in the stage model.

<!--Device-dateTimeManager-function isModifyDateTimeDisallowed(admin: Want, callback: AsyncCallback<boolean>): void--><!--Device-dateTimeManager-function isModifyDateTimeDisallowed(admin: Want, callback: AsyncCallback<boolean>): void-End-->

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
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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

dateTimeManager.isModifyDateTimeDisallowed(wantTemp, (err, result) => {
  if (err) {
    console.error(`Failed to query modify date time is disallowed or not. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying modify date time is disallowed : ${result}`);
})
```


## isModifyDateTimeDisallowed

```TypeScript
function isModifyDateTimeDisallowed(admin: Want): Promise<boolean>
```

Queries whether the system time of a device can be modified. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.enterprise.restrictions:restrictions.getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy)(admin:

**Required permissions:** ohos.permission.ENTERPRISE_SET_DATETIME

**Model restriction:** This API can be used only in the stage model.

<!--Device-dateTimeManager-function isModifyDateTimeDisallowed(admin: Want): Promise<boolean>--><!--Device-dateTimeManager-function isModifyDateTimeDisallowed(admin: Want): Promise<boolean>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

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
import { dateTimeManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

dateTimeManager.isModifyDateTimeDisallowed(wantTemp).then((result) => {
  console.info(`Succeeded in querying modify date time is disallowed : ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query modify date time is disallowed or not. Code is ${err.code}, message is ${err.message}`);
})
```
