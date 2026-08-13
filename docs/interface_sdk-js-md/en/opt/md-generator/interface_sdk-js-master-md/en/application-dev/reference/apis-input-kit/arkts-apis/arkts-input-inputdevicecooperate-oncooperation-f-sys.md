# on_cooperation (System API)

## Modules to Import

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
```

## on_cooperation

```TypeScript
function on(type: 'cooperation', callback: AsyncCallback<{ deviceDescriptor: string, eventMsg: EventMsg }>): void
```

Registers a listener for screen hopping state changes. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [on](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-oncooperate-f-sys.md#on_cooperate)

<!--Device-inputDeviceCooperate-function on(type: 'cooperation', callback: AsyncCallback<{ deviceDescriptor: string, eventMsg: EventMsg }>): void--><!--Device-inputDeviceCooperate-function on(type: 'cooperation', callback: AsyncCallback<{ deviceDescriptor: string, eventMsg: EventMsg }>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cooperation' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ deviceDescriptor: string, eventMsg: EventMsg }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let callback = (msg: object) => {
            console.info(`Succeeded in monitoring cooperation, msg: ${JSON.stringify(msg)}.`);
            return false;
          }
          try {
            inputDeviceCooperate.on('cooperation', callback);
          } catch (error) {
            console.error(`Failed to register keyboard and mouse traversal status, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
