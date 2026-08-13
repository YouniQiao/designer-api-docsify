# isFunctionKeyEnabled

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## isFunctionKeyEnabled

```TypeScript
function isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>
```

Checks whether the specified function key (for example, **CapsLock**) is enabled. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-inputDevice-function isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>--><!--Device-inputDevice-function isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| functionKey | [FunctionKey](arkts-input-inputdevice-functionkey-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3900002](../errorcode-inputdevice.md#3900002-keyboard-not-connected) |

## Examples

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Query Whether a Function Key Is Enabled
            inputDevice.isFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK).then((state: boolean) => {
              console.info(`Succeeded in getting capslock state: ${JSON.stringify(state)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get capslock state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get capslock state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
