# getKeyboardRepeatDelay (System API)

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## getKeyboardRepeatDelay

```TypeScript
function getKeyboardRepeatDelay(callback: AsyncCallback<number>): void
```

Obtains the keyboard repeat delay. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-inputDevice-function getKeyboardRepeatDelay(callback: AsyncCallback<int>): void--><!--Device-inputDevice-function getKeyboardRepeatDelay(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
            // Obtaining the Key Repeat Delay
            inputDevice.getKeyboardRepeatDelay((error: BusinessError, delay: number) => {
              if (error) {
                console.error(`Failed to get keyboard repeat delay, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting keyboard repeat delay.`);
            });
          } catch (error) {
            console.error(`Failed to get keyboard repeat delay, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getKeyboardRepeatDelay

```TypeScript
function getKeyboardRepeatDelay(): Promise<number>
```

Obtains the keyboard repeat delay. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-inputDevice-function getKeyboardRepeatDelay(): Promise<int>--><!--Device-inputDevice-function getKeyboardRepeatDelay(): Promise<int>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
            // Obtaining the Key Repeat Delay
            inputDevice.getKeyboardRepeatDelay().then((delay: number) => {
              console.info(`Succeeded in getting keyboard repeat delay.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get keyboard, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get keyboard repeat delay, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
