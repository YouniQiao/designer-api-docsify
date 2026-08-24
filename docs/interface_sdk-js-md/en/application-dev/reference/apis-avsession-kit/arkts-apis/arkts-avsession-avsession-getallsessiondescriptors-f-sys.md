# getAllSessionDescriptors (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## getAllSessionDescriptors

```TypeScript
function getAllSessionDescriptors(callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void
```

Get all avsession descriptors of the system

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAllSessionDescriptors(callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void--><!--Device-avSession-function getAllSessionDescriptors(callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Readonly&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt;&gt;&gt; | Yes | async callback for an array of AVSessionDescriptors. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avSession.getAllSessionDescriptors().then((descriptors: avSession.AVSessionDescriptor[]) => {
  console.info(`getAllSessionDescriptors : SUCCESS : descriptors.length : ${descriptors.length}`);
  if (descriptors.length > 0 ) {
    console.info(`getAllSessionDescriptors : SUCCESS : descriptors[0].isActive : ${descriptors[0].isActive}`);
    console.info(`GetAllSessionDescriptors : SUCCESS : descriptors[0].type : ${descriptors[0].type}`);
    console.info(`GetAllSessionDescriptors : SUCCESS : descriptors[0].sessionTag : ${descriptors[0].sessionTag}`);
  }
}).catch((err: BusinessError) => {
  console.error(`GetAllSessionDescriptors BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avSession.getAllSessionDescriptors((err: BusinessError, descriptors: avSession.AVSessionDescriptor[]) => {
  if (err) {
    console.error(`GetAllSessionDescriptors BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetAllSessionDescriptors : SUCCESS : descriptors.length : ${descriptors.length}`);
    if (descriptors.length > 0 ) {
        console.info(`getAllSessionDescriptors : SUCCESS : descriptors[0].isActive : ${descriptors[0].isActive}`);
        console.info(`getAllSessionDescriptors : SUCCESS : descriptors[0].type : ${descriptors[0].type}`);
        console.info(`getAllSessionDescriptors : SUCCESS : descriptors[0].sessionTag : ${descriptors[0].sessionTag}`);
    }
  }
});
```


## getAllSessionDescriptors

```TypeScript
function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>
```

Get all avsession descriptors which can be shown on system entrance.

**Since:** 23

**Required permissions:** 
- API version 23+: ohos.permission.MANAGE_MEDIA_RESOURCES or ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
- API version 9 - 22: ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>--><!--Device-avSession-function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Readonly&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt;&gt;&gt; | Promise for an array of AVSessionDescriptors |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App.<br>**Applicable version:** 9 - 22 |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

**Examples**

See [getAllSessionDescriptors](#getallsessiondescriptors)

