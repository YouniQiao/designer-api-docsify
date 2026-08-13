# getDisallowedRunningBundles (System API)

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## getDisallowedRunningBundles

```TypeScript
function getDisallowedRunningBundles(admin: Want, callback: AsyncCallback<Array<string>>): void
```

Obtains applications that are not allowed to run by the current user. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md#getDisallowedRunningBundlesSync)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SET_APP_RUNNING_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getDisallowedRunningBundles(admin: Want, callback: AsyncCallback<Array<string>>): void--><!--Device-applicationManager-function getDisallowedRunningBundles(admin: Want, callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

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
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

applicationManager.getDisallowedRunningBundles(wantTemp, (err, result) => {
  if (err) {
    console.error(`Failed to get disallowed running bundles. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting disallowed running bundles, result : ${JSON.stringify(result)}`);
});
```


## getDisallowedRunningBundles

```TypeScript
function getDisallowedRunningBundles(admin: Want, userId: number, callback: AsyncCallback<Array<string>>): void
```

Obtains an application from the applications that are not allowed to run by the current user (specified by **userId**). This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md#getDisallowedRunningBundlesSync)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SET_APP_RUNNING_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getDisallowedRunningBundles(admin: Want, userId: number, callback: AsyncCallback<Array<string>>): void--><!--Device-applicationManager-function getDisallowedRunningBundles(admin: Want, userId: number, callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

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
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

applicationManager.getDisallowedRunningBundles(wantTemp, 100, (err, result) => {
  if (err) {
    console.error(`Failed to get disallowed running bundles. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting disallowed running bundles, result : ${JSON.stringify(result)}`);
});
```


## getDisallowedRunningBundles

```TypeScript
function getDisallowedRunningBundles(admin: Want, userId?: number): Promise<Array<string>>
```

Obtains applications that are not allowed to run under the current user or a specified user. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md#getDisallowedRunningBundlesSync)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SET_APP_RUNNING_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getDisallowedRunningBundles(admin: Want, userId?: number): Promise<Array<string>>--><!--Device-applicationManager-function getDisallowedRunningBundles(admin: Want, userId?: number): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

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
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

applicationManager.getDisallowedRunningBundles(wantTemp, 100).then((result) => {
  console.info(`Succeeded in getting disallowed running bundles, result : ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get disallowed running bundles. Code is ${err.code}, message is ${err.message}`);
});
```
