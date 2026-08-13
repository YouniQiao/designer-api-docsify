# off_sessionDestroy (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## off_sessionDestroy

```TypeScript
function off(type: 'sessionDestroy', callback?: (session: AVSessionDescriptor) => void): void
```

Unregister session destroy callback

**Since:** 9

**Deprecated since:** -1

<!--Device-avSession-function off(type: 'sessionDestroy', callback?: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function off(type: 'sessionDestroy', callback?: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sessionDestroy' | Yes |
| callback | (session: AVSessionDescriptor) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
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
            avSession.on('sessionDestroy', (descriptor: avSession.AVSessionDescriptor) => {
            });
            avSession.off('sessionDestroy');
          })
      }
    .width('100%')
    .height('100%')
  }
}
```
