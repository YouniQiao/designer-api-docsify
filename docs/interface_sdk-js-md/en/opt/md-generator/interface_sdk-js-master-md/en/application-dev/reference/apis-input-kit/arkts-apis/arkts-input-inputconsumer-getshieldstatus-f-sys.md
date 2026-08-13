# getShieldStatus (System API)

## Modules to Import

```TypeScript
import { inputConsumer } from '@kit.InputKit';
```

## getShieldStatus

```TypeScript
function getShieldStatus(shieldMode: ShieldMode): boolean
```

Obtains the system hotkey shield status.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INPUT_CONTROL_DISPATCHING

<!--Device-inputConsumer-function getShieldStatus(shieldMode: ShieldMode): boolean--><!--Device-inputConsumer-function getShieldStatus(shieldMode: ShieldMode): boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shieldMode | [ShieldMode](arkts-input-inputconsumer-shieldmode-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputConsumer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let FACTORY_MODE = 0;
            let shieldstatusResult:Boolean =  inputConsumer.getShieldStatus(FACTORY_MODE);
            console.info(` get shield status result:${JSON.stringify(shieldstatusResult)}`);
          } catch (error) {
            console.error(`Failed to get shield status, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```
