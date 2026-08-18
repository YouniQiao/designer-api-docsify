# getForegroundApplications (System API)

## Modules to Import

```TypeScript
```

## getForegroundApplications

```TypeScript
function getForegroundApplications(callback: AsyncCallback<Array<AppStateData>>): void
```

getForegroundApplications.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getforegroundapplications-system-api)

**Required permissions:** ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function getForegroundApplications(callback: AsyncCallback<Array<AppStateData>>): void--><!--Device-appManager-function getForegroundApplications(callback: AsyncCallback<Array<AppStateData>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppStateData](arkts-ability-appstatedata-c.md)&gt;&gt; | Yes |

**Examples**

```TypeScript
import appManager from '@ohos.application.appManager';

appManager.getForegroundApplications((err, data) => {
  if (err) {
    console.error(`GetForegroundApplications failed, error code: ${err.code}, error msg: ${err.message}.`);
  } else {
    console.info(`GetForegroundApplications success, data: ${JSON.stringify(data)}.`);
  }
});
```


## getForegroundApplications

```TypeScript
function getForegroundApplications(): Promise<Array<AppStateData>>
```

getForegroundApplications.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getforegroundapplications-system-api)

**Required permissions:** ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function getForegroundApplications(): Promise<Array<AppStateData>>--><!--Device-appManager-function getForegroundApplications(): Promise<Array<AppStateData>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AppStateData](arkts-ability-appstatedata-c.md)&gt;&gt; |

**Examples**

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.getForegroundApplications()
  .then((data) => {
    console.info(`GetForegroundApplications success, data: ${JSON.stringify(data)}.`);
  })
  .catch((err: BusinessError) => {
    console.error(`GetForegroundApplications failed, error code: ${err.code}, error msg: ${err.message}.`);
  });
```
