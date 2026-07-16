# Restorer (System API)

Defines a tool class for restoring factory settings.

**Since:** 9

<!--Device-update-export interface Restorer--><!--Device-update-export interface Restorer-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from '@kit.BasicServicesKit';
```

## deepFactoryReset

```TypeScript
deepFactoryReset(factoryResetStrategy: FactoryResetStrategy): Promise<void>
```

Clears the user data partition and OS partition by means of overwriting. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.FACTORY_RESET

**Model restriction:** This API can be used only in the stage model.

<!--Device-Restorer-deepFactoryReset(factoryResetStrategy: FactoryResetStrategy): Promise<void>--><!--Device-Restorer-deepFactoryReset(factoryResetStrategy: FactoryResetStrategy): Promise<void>-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factoryResetStrategy | [FactoryResetStrategy](arkts-basicservices-factoryresetstrategy-i-sys.md) | Yes | Factory reset strategy. |

**Return value:**

| Type | Description |
| --- | --- |
| [Promise](../../apis-na/arkts-apis/arkts-na-promise-i.md)<void> | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) | This function is prohibited by enterprise management policies. |
| [11500104](../../apis-basic-services-kit/errorcode-update.md#11500104-ipc-error) | IPC error. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let restorer = update.getRestorer();
  let factoryResetStrategy: update.FactoryResetStrategy = {
    scope: update.FactoryResetScope.DATA,
    strategy: "deepFactoryReset test"
  };
  restorer.deepFactoryReset(factoryResetStrategy).then(() => {
    console.info(`deepFactoryReset success`);
  }).catch((err: BusinessError) => {
    console.error(`deepFactoryReset error ${JSON.stringify(err)}`);
  });
} catch(error) {
  console.error(`Fail to get restorer: ${error}`);
}

```

## factoryReset

```TypeScript
factoryReset(callback: AsyncCallback<void>): void
```

Clears the user data partition. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.FACTORY_RESET

<!--Device-Restorer-factoryReset(callback: AsyncCallback<void>): void--><!--Device-Restorer-factoryReset(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-i.md)<void> | Yes | Callback used to return the result. If the factory reset is successful,**err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) | This function is prohibited by enterprise management policies. |
| [11500104](../../apis-basic-services-kit/errorcode-update.md#11500104-ipc-error) | IPC error. |

**Example**

```TypeScript
try {
  let restorer = update.getRestorer();
  restorer.factoryReset((err) => {
    console.info(`factoryReset error ${JSON.stringify(err)}`);
  });
} catch(error) {
  console.error(`Fail to get restorer: ${error}`);
}

```

## factoryReset

```TypeScript
factoryReset(): Promise<void>
```

Clears the user data partition. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.FACTORY_RESET

<!--Device-Restorer-factoryReset(): Promise<void>--><!--Device-Restorer-factoryReset(): Promise<void>-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [Promise](../../apis-na/arkts-apis/arkts-na-promise-i.md)<void> | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) | This function is prohibited by enterprise management policies. |
| [11500104](../../apis-basic-services-kit/errorcode-update.md#11500104-ipc-error) | IPC error. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let restorer = update.getRestorer();
  restorer.factoryReset().then(() => {
    console.info(`factoryReset success`);
  }).catch((err: BusinessError) => {
    console.error(`factoryReset error ${JSON.stringify(err)}`);
  });
} catch(error) {
  console.error(`Fail to get restorer: ${error}`);
}

```

## forceFactoryReset

```TypeScript
forceFactoryReset(): Promise<void>
```

Clears the user data partition and the file key. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.FORCE_FACTORY_RESET

<!--Device-Restorer-forceFactoryReset(): Promise<void>--><!--Device-Restorer-forceFactoryReset(): Promise<void>-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [Promise](../../apis-na/arkts-apis/arkts-na-promise-i.md)<void> | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) | This function is prohibited by enterprise management policies. |
| [11500104](../../apis-basic-services-kit/errorcode-update.md#11500104-ipc-error) | IPC error. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let restorer = update.getRestorer();
  restorer.forceFactoryReset().then(() => {
    console.info(`forceFactoryReset success`);
  }).catch((err: BusinessError) => {
    console.error(`forceFactoryReset error ${JSON.stringify(err)}`);
  });
} catch(error) {
  console.error(`Fail to get restorer: ${error}`);
}

```

## getDeepFactoryResetInfo

```TypeScript
getDeepFactoryResetInfo(factoryResetStrategy: FactoryResetStrategy): Promise<FactoryResetInfo>
```

Obtains the factory reset information. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.FACTORY_RESET

**Model restriction:** This API can be used only in the stage model.

<!--Device-Restorer-getDeepFactoryResetInfo(factoryResetStrategy: FactoryResetStrategy): Promise<FactoryResetInfo>--><!--Device-Restorer-getDeepFactoryResetInfo(factoryResetStrategy: FactoryResetStrategy): Promise<FactoryResetInfo>-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factoryResetStrategy | [FactoryResetStrategy](arkts-basicservices-factoryresetstrategy-i-sys.md) | Yes | Factory reset strategy. |

**Return value:**

| Type | Description |
| --- | --- |
| [Promise](../../apis-na/arkts-apis/arkts-na-promise-i.md)<FactoryResetInfo> | Promise used to return the factory reset information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [11500104](../../apis-basic-services-kit/errorcode-update.md#11500104-ipc-error) | IPC error. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let factoryResetStrategy: update.FactoryResetStrategy = {
  scope: update.FactoryResetScope.DATA,
  strategy: "deepFactoryReset"
};
try {
  let restorer = update.getRestorer();
  restorer.getDeepFactoryResetInfo(factoryResetStrategy).then((info: update.FactoryResetInfo) => {
    console.info(`getDeepFactoryResetInfo success`);
  }).catch((err: BusinessError) => {
    console.error(`getDeepFactoryResetInfo promise error ${JSON.stringify(err)}`);
  });
} catch(error) {
  console.error(`Fail to get restorer: ${error}`);
}

```

