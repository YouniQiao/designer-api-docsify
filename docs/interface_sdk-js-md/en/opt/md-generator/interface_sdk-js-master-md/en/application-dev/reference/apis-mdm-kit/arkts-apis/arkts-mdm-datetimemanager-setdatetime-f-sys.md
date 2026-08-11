# setDateTime (System API)

## Modules to Import

```TypeScript
import { dateTimeManager } from 'kits/@kit.MDMKit';
```

## setDateTime

```TypeScript
function setDateTime(admin: Want, time: number, callback: AsyncCallback<void>): void
```

Sets the system time. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.enterprise.deviceSettings:deviceSettings.setValue](arkts-mdm-devicesettings-setvalue-f.md#setvalue)

**Required permissions:** ohos.permission.ENTERPRISE_SET_DATETIME

**Model restriction:** This API can be used only in the stage model.

<!--Device-dateTimeManager-function setDateTime(admin: Want, time: number, callback: AsyncCallback<void>): void--><!--Device-dateTimeManager-function setDateTime(admin: Want, time: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| time | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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

// Replace with actual values.
dateTimeManager.setDateTime(wantTemp, 1526003846000, (err) => {
  if (err) {
    console.error(`Failed to set date time. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting date time');
})
```


## setDateTime

```TypeScript
function setDateTime(admin: Want, time: number): Promise<void>
```

Sets the system time. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.enterprise.deviceSettings:deviceSettings.setValue](arkts-mdm-devicesettings-setvalue-f.md#setvalue)

**Required permissions:** ohos.permission.ENTERPRISE_SET_DATETIME

**Model restriction:** This API can be used only in the stage model.

<!--Device-dateTimeManager-function setDateTime(admin: Want, time: number): Promise<void>--><!--Device-dateTimeManager-function setDateTime(admin: Want, time: number): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| time | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

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

// Replace with actual values.
dateTimeManager.setDateTime(wantTemp, 1526003846000).then(() => {
  console.info('Succeeded in setting date time');
}).catch((err: BusinessError) => {
  console.error(`Failed to set date time. Code is ${err.code}, message is ${err.message}`);
})
```
