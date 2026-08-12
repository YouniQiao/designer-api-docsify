# getHistoricalSessionDescriptors (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## getHistoricalSessionDescriptors

```TypeScript
function getHistoricalSessionDescriptors(maxSize: number, callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void
```

Get history avsession records. These sessions have been destroyed.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getHistoricalSessionDescriptors(maxSize: int, callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void--><!--Device-avSession-function getHistoricalSessionDescriptors(maxSize: int, callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxSize | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Readonly](../../apis-default/arkts-apis/arkts-readonly-t.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i.md)&gt;&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6600101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
avSession.getHistoricalSessionDescriptors(1, (descriptors: avSession.AVSessionDescriptor[]) => { 
    console.info(`Succeeded in getting historical session descriptors, length: ${descriptors.length}`); 
    if (descriptors.length > 0 ) { 
      console.info(`Succeeded in getting historical session descriptor, isActive: ${descriptors[0].isActive}`); 
      console.info(`Succeeded in getting historical session descriptor, type: ${descriptors[0].type}`); 
      console.info(`Succeeded in getting historical session descriptor, sessionTag: ${descriptors[0].sessionTag}`); 
      console.info(`Succeeded in getting historical session descriptor, sessionId: ${descriptors[0].sessionId}`); 
      console.info(`Succeeded in getting historical session descriptor, bundleName: ${descriptors[0].elementName.bundleName}`); 
    } 
});
```


## getHistoricalSessionDescriptors

```TypeScript
function getHistoricalSessionDescriptors(maxSize?: number): Promise<Array<Readonly<AVSessionDescriptor>>>
```

Get history avsession records. These sessions have been destroyed.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getHistoricalSessionDescriptors(maxSize?: int): Promise<Array<Readonly<AVSessionDescriptor>>>--><!--Device-avSession-function getHistoricalSessionDescriptors(maxSize?: int): Promise<Array<Readonly<AVSessionDescriptor>>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxSize | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Readonly](../../apis-default/arkts-apis/arkts-readonly-t.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i.md)&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6600101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
avSession.getHistoricalSessionDescriptors().then((descriptors: avSession.AVSessionDescriptor[]) => {
  console.info(`Succeeded in getting historical session descriptors, length: ${descriptors.length}`);
  if (descriptors.length > 0 && descriptors[0]) {
    console.info(`Succeeded in getting historical session descriptor, isActive: ${descriptors[0].isActive}`);
    console.info(`Succeeded in getting historical session descriptor, type: ${descriptors[0].type}`);
    console.info(`Succeeded in getting historical session descriptor, sessionTag: ${descriptors[0].sessionTag}`);
    console.info(`Succeeded in getting historical session descriptor, sessionId: ${descriptors[0].sessionId}`);
    console.info(`Succeeded in getting historical session descriptor, bundleName: ${descriptors[0].elementName.bundleName}`);
  }
});
```
