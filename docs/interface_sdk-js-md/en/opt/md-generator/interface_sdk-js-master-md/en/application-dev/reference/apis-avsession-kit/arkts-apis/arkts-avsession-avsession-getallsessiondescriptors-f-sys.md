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

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAllSessionDescriptors(callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void--><!--Device-avSession-function getAllSessionDescriptors(callback: AsyncCallback<Array<Readonly<AVSessionDescriptor>>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt;&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { avSession } from '@kit.AVSessionKit';

@Entry 
@Component 
struct Index { 
  @State message: string = 'hello world'; 

  build() { 
    Column() { 
        Text(this.message) 
          .onClick(()=>{ 
            avSession.getAllSessionDescriptors((descriptors: avSession.AVSessionDescriptor[]) => { 
                console.info(`Succeeded in getting all session descriptors, length: ${descriptors.length}`); 
                if (descriptors.length > 0 ) { 
                    console.info(`Succeeded in getting session descriptor, isActive: ${descriptors[0].isActive}`); 
                    console.info(`Succeeded in getting session descriptor, type: ${descriptors[0].type}`); 
                    console.info(`Succeeded in getting session descriptor, sessionTag: ${descriptors[0].sessionTag}`); 
                } 
            }); 
          }) 
      } 
    .width('100%') 
    .height('100%') 
  } 
}
```


## getAllSessionDescriptors

```TypeScript
function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>
```

Get all avsession descriptors which can be shown on system entrance.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 23+: ohos.permission.MANAGE_MEDIA_RESOURCES or ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
- API version 9 - 22: ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>--><!--Device-avSession-function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            avSession.getAllSessionDescriptors().then((descriptors: avSession.AVSessionDescriptor[]) => {
              console.info(`Succeeded in getting all session descriptors, length: ${descriptors.length}`);
              if (descriptors.length > 0 ) {
                console.info(`Succeeded in getting session descriptor, isActive: ${descriptors[0].isActive}`);
                console.info(`Succeeded in getting session descriptor, type: ${descriptors[0].type}`);
                console.info(`Succeeded in getting session descriptor, sessionTag: ${descriptors[0].sessionTag}`);
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```
