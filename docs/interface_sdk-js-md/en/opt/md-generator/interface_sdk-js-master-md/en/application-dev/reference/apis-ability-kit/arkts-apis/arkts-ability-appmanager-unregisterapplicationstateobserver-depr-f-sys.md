# unregisterApplicationStateObserver (System API)

## unregisterApplicationStateObserver

```TypeScript
function unregisterApplicationStateObserver(observerId: number, callback: AsyncCallback<void>): void
```

Unregister application state observer.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-ability-appmanager-offapplicationstate-f.md#off_applicationState)

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function unregisterApplicationStateObserver(observerId: number, callback: AsyncCallback<void>): void--><!--Device-appManager-function unregisterApplicationStateObserver(observerId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| observerId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

let observerId = 100;

function unregisterApplicationStateObserverCallback(err: BusinessError) {
  if (err) {
    console.error(`UnregisterApplicationStateObserverCallback failed, error code: ${err.code}, error msg: ${err.message}.`);
    return;
  }
}

appManager.unregisterApplicationStateObserver(observerId, unregisterApplicationStateObserverCallback);
```


## unregisterApplicationStateObserver

```TypeScript
function unregisterApplicationStateObserver(observerId: number): Promise<void>
```

Unregister application state observer.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-ability-appmanager-offapplicationstate-f.md#off_applicationState)

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function unregisterApplicationStateObserver(observerId: number): Promise<void>--><!--Device-appManager-function unregisterApplicationStateObserver(observerId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| observerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

let observerId = 100;

appManager.unregisterApplicationStateObserver(observerId)
.then((data) => {
    console.info(`unregisterApplicationStateObserver success, data: ${data}.`);
})
.catch((err: BusinessError) => {
    console.error(`unregisterApplicationStateObserver failed, err code: ${err.code}, err msg: ${err.message}.`);
});
```
