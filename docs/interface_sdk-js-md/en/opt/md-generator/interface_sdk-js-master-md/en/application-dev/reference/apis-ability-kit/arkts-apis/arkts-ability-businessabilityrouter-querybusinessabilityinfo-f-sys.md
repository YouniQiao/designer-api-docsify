# queryBusinessAbilityInfo (System API)

## Modules to Import

```TypeScript
import { businessAbilityRouter } from '@kit.AbilityKit';
```

## queryBusinessAbilityInfo

```TypeScript
function queryBusinessAbilityInfo(
    filter: BusinessAbilityFilter,
    callback: AsyncCallback<Array<BusinessAbilityInfo>>
  ): void
```

Query the business ability info of by the given filter. ohos.permission.GET_BUNDLE_INFO_PRIVILEGED is required for cross user access.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(    filter: BusinessAbilityFilter,    callback: AsyncCallback<Array<BusinessAbilityInfo>>  ): void--><!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(    filter: BusinessAbilityFilter,    callback: AsyncCallback<Array<BusinessAbilityInfo>>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BusinessAbilityInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>--><!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;BusinessAbilityInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
