# setFunctionKeyEnabled

## Modules to Import

```TypeScript
```

## setFunctionKeyEnabled

```TypeScript
function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>
```

Specifies whether to enable a function key (for example, **CapsLock**). This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INPUT_KEYBOARD_CONTROLLER

<!--Device-inputDevice-function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>--><!--Device-inputDevice-function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| functionKey | [FunctionKey](arkts-input-inputdevice-functionkey-e.md) | Yes |
| enabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3900003](../errorcode-inputdevice.md#3900003-api-call-failed-for-a-noninput-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3900002](../errorcode-inputdevice.md#3900002-keyboard-not-connected) |

**Examples**

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
            // Set Function Key Enabled Status
            inputDevice.setFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK, true).then(() => {
              console.info(`Succeeded in setting capslock state.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set capslock state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to set capslock enable, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
