# getHistoricalSessionDescriptors (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## getHistoricalSessionDescriptors

```TypeScript
function getHistoricalSessionDescriptors(maxSize: int, callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void
```

Get history avsession records. These sessions have been destroyed.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getHistoricalSessionDescriptors(maxSize: int, callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void--><!--Device-avSession-function getHistoricalSessionDescriptors(maxSize: int, callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxSize | int | Yes | Specifies the maximum size of the returned value array. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt;&gt;&gt; | Yes | async callback for an array of AVSessionDescriptors. If provided '0' or not provided, the maximum value is determined by the system. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avSession.getHistoricalSessionDescriptors(1, (err: BusinessError, descriptors: avSession.AVSessionDescriptor[]) => {
  if (err) {
    console.error(`getHistoricalSessionDescriptors BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors.length : ${descriptors.length}`);
    if (descriptors.length > 0 ) {
      console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].isActive : ${descriptors[0].isActive}`);
      console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].type : ${descriptors[0].type}`);
      console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].sessionTag : ${descriptors[0].sessionTag}`);
      console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].sessionId : ${descriptors[0].sessionId}`);
      console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].elementName.bundleName : ${descriptors[0].elementName.bundleName}`);
    }
  }
});
```


## getHistoricalSessionDescriptors

```TypeScript
function getHistoricalSessionDescriptors(maxSize?: int): Promise<Array<Readonly<AVSessionDescriptor>>>
```

Get history avsession records. These sessions have been destroyed.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getHistoricalSessionDescriptors(maxSize?: int): Promise<Array<Readonly<AVSessionDescriptor>>>--><!--Device-avSession-function getHistoricalSessionDescriptors(maxSize?: int): Promise<Array<Readonly<AVSessionDescriptor>>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxSize | int | No | Specifies the maximum size of the returned value array. If provided '0' or not provided, the maximum value is determined by the system. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt;&gt;&gt; | Promise for an array of AVSessionDescriptors |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avSession.getHistoricalSessionDescriptors().then((descriptors: avSession.AVSessionDescriptor[]) => {
  console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors.length : ${descriptors.length}`);
  if (descriptors.length > 0 && descriptors[0]) {
    console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].isActive : ${descriptors[0].isActive}`);
    console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].type : ${descriptors[0].type}`);
    console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].sessionTag : ${descriptors[0].sessionTag}`);
    console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].sessionId : ${descriptors[0].sessionId}`);
    console.info(`getHistoricalSessionDescriptors : SUCCESS : descriptors[0].elementName.bundleName : ${descriptors[0].elementName.bundleName}`);
  }
}).catch((err: BusinessError) => {
  console.error(`getHistoricalSessionDescriptors BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

