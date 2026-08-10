# queryBusinessAbilityInfo (System API)

## Modules to Import

```TypeScript
import { businessAbilityRouter } from 'kits/@kit.AbilityKit';
```

## queryBusinessAbilityInfo

```TypeScript
function queryBusinessAbilityInfo(
    filter: BusinessAbilityFilter,
    callback: AsyncCallback<Array<BusinessAbilityInfo>>
  ): void
```

Query the business ability info of by the given filter. ohos.permission.GET_BUNDLE_INFO_PRIVILEGED is required for cross user access.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(    filter: BusinessAbilityFilter,    callback: AsyncCallback<Array<BusinessAbilityInfo>>  ): void--><!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(    filter: BusinessAbilityFilter,    callback: AsyncCallback<Array<BusinessAbilityInfo>>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | Yes | Indicates the filter containing the business ability info to be queried. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BusinessAbilityInfo&gt;&gt; | Yes | The callback of querying business ability info result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | non-system app called system api. |

## Examples

```TypeScript
import { businessAbilityRouter } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let filter: businessAbilityRouter.BusinessAbilityFilter = { businessType: businessAbilityRouter.BusinessType.SHARE };

try {
  businessAbilityRouter.queryBusinessAbilityInfo(filter, (error, data) => {
    if (error) {
      console.error('queryBusinessAbilityInfo failed ' + error.message);
      return;
    }
    console.info('queryBusinessAbilityInfo success');
  });
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('queryBusinessAbilityInfo failed ' + message);
}
```


## queryBusinessAbilityInfo

```TypeScript
function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>
```

Query the business ability info of by the given filter. ohos.permission.GET_BUNDLE_INFO_PRIVILEGED is required for cross user access.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>--><!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | Yes | Indicates the filter containing the business ability info to be queried. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BusinessAbilityInfo&gt;&gt; | Returns a list of business ability info objects. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | non-system app called system api. |

## Examples

```TypeScript
import { businessAbilityRouter } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let filter: businessAbilityRouter.BusinessAbilityFilter = { businessType: businessAbilityRouter.BusinessType.SHARE };

try {
  businessAbilityRouter.queryBusinessAbilityInfo(filter)
    .then(() => {
      console.info('queryBusinessAbilityInfo success');
    }).catch((error: BusinessError) => {
    console.error('queryBusinessAbilityInfo failed ' + error.message);
  });
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('queryBusinessAbilityInfo failed ' + message);
}
```

