# getSystemSize (System API)

## Modules to Import

```TypeScript
```

## getSystemSize

```TypeScript
function getSystemSize(callback: AsyncCallback<number>): void
```

Get the system size.

**Since:** 23

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getSystemSize(callback: AsyncCallback<long>): void--><!--Device-storageStatistics-function getSystemSize(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getSystemSize((error: BusinessError, number: number) => {
  if (error) {
    console.error("getSystemSize failed with error:" + JSON.stringify(error));
  } else {
    // Do something.
    console.info("getSystemSize successfully:" + number);
  }
});
```


## getSystemSize

```TypeScript
function getSystemSize(): Promise<number>
```

Get the system size.

**Since:** 23

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getSystemSize(): Promise<long>--><!--Device-storageStatistics-function getSystemSize(): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getSystemSize().then((number: number) => {
  console.info("getSystemSize successfully:" + number);
}).catch((err: BusinessError) => {
  console.error("getSystemSize failed with error:" + JSON.stringify(err));
});
```
