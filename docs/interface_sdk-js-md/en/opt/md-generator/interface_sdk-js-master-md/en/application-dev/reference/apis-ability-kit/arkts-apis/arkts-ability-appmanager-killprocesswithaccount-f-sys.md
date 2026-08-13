# killProcessWithAccount (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## killProcessWithAccount

```TypeScript
function killProcessWithAccount(bundleName: string, accountId: number): Promise<void>
```

Kills a process by bundle name and account ID. This API uses a promise to return the result. > **NOTE：**> > The ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permission is not required when **accountId** specifies the > current user.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 14+: ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.KILL_APP_PROCESSES or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES
- API version 9 - 13: ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES

<!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: int): Promise<void>--><!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: int): Promise<void>-End-->

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

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'bundleName';
let accountId = 0;

try {
  appManager.killProcessWithAccount(bundleName, accountId).then(() => {
    console.info('killProcessWithAccount success');
  }).catch((err: BusinessError) => {
    console.error(`killProcessWithAccount fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```


## killProcessWithAccount

```TypeScript
function killProcessWithAccount(bundleName: string, accountId: number, clearPageStack: boolean, appIndex?: number):
    Promise<void>
```

Kills a process by bundle name and account ID. This API uses a promise to return the result. > **NOTE：**> > The ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permission is not required when **accountId** specifies the > current user.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.KILL_APP_PROCESSES or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES

<!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: int, clearPageStack: boolean, appIndex?: int):    Promise<void>--><!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: int, clearPageStack: boolean, appIndex?: int):    Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |
| clearPageStack | boolean | Yes |
| appIndex | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'bundleName';
let accountId = 0;
let isClearPageStack = false;
let appIndex = 1;

try {
  appManager.killProcessWithAccount(bundleName, accountId, isClearPageStack, appIndex).then(() => {
    console.info('killProcessWithAccount success');
  }).catch((err: BusinessError) => {
    console.error(`killProcessWithAccount fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```


## killProcessWithAccount

```TypeScript
function killProcessWithAccount(bundleName: string, accountId: number, callback: AsyncCallback<void>): void
```

Kills a process by bundle name and account ID. This API uses an asynchronous callback to return the result. > **NOTE：**> > The ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permission is not required when **accountId** specifies the > current user.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 14+: ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.KILL_APP_PROCESSES or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES
- API version 9 - 13: ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES

<!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: int, callback: AsyncCallback<void>): void--><!--Device-appManager-function killProcessWithAccount(bundleName: string, accountId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'bundleName';
let accountId = 0;

function killProcessWithAccountCallback(err: BusinessError) {
  if (err) {
    console.error(`killProcessWithAccountCallback fail, err: ${JSON.stringify(err)}`);
  } else {
    console.info('killProcessWithAccountCallback success.');
  }
}

appManager.killProcessWithAccount(bundleName, accountId, killProcessWithAccountCallback);
```
