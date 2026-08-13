# exit (System API)

## Modules to Import

```TypeScript
import { cloudData } from '@kit.ArkData';
```

## exit

```TypeScript
function exit(sharingResource: string, callback: AsyncCallback<Result<void>>): void
```

Exits the share of the specified shared resource. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sharing-function exit(sharingResource: string, callback: AsyncCallback<Result<void>>): void--><!--Device-sharing-function exit(sharingResource: string, callback: AsyncCallback<Result<void>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sharingResource | string | Yes | Shared resource ID. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Result&lt;void&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.sharing.exit('sharing_resource_test', ((err: BusinessError, result) => {
  if (err) {
    console.error(`exit share failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info(`exit share succeeded, result: ${result}`);
}))
```


## exit

```TypeScript
function exit(sharingResource: string): Promise<Result<void>>
```

Exits the share of the specified shared resource. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sharing-function exit(sharingResource: string): Promise<Result<void>>--><!--Device-sharing-function exit(sharingResource: string): Promise<Result<void>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sharingResource | string | Yes | Shared resource ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&lt;void&gt;&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.sharing.exit('sharing_resource_test').then((result) => {
  console.info(`exit share success, result: ${result}`);
}).catch((err: BusinessError) => {
  console.error(`exit share failed, code is ${err.code},message is ${err.message}`);
})
```

