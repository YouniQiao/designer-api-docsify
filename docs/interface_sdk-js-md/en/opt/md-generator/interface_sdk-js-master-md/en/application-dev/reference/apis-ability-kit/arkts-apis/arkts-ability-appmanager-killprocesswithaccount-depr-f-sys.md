# killProcessWithAccount (System API)

## Modules to Import

```TypeScript
```

## killProcessWithAccount

```TypeScript
function killProcessWithAccount(bundleName: string, accountId: number): Promise<void>
```

Kill process with account.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killprocesswithaccount-system-api)

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES

<!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: number): Promise<void>--><!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

let bundleName = 'bundleName';
let accountId = 0;
appManager.killProcessWithAccount(bundleName, accountId)
  .then((data) => {
    console.info(`KillProcessWithAccount success, data: ${JSON.stringify(data)}.`);
  })
  .catch((err: BusinessError) => {
    console.error(`KillProcessWithAccount failed, error code: ${err.code}, error msg: ${err.message}.`);
  });
```


## killProcessWithAccount

```TypeScript
function killProcessWithAccount(bundleName: string, accountId: number, callback: AsyncCallback<void>): void
```

Kill process with account.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killprocesswithaccount-system-api)

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES

<!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: number, callback: AsyncCallback<void>): void--><!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

let bundleName = 'bundleName';
let accountId = 0;

function killProcessWithAccountCallback(err: BusinessError, data: void) {
  if (err) {
    console.error(`KillProcessWithAccountCallback failed, error code: ${err.code}, error msg: ${err.message}.`);
  } else {
    console.info(`KillProcessWithAccountCallback success, data: ${JSON.stringify(data)}`);
  }
}

appManager.killProcessWithAccount(bundleName, accountId, killProcessWithAccountCallback);
```
