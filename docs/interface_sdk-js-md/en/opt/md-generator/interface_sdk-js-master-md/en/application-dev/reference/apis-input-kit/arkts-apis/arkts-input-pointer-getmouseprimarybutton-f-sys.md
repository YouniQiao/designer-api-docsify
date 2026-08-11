# getMousePrimaryButton (System API)

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getMousePrimaryButton

```TypeScript
function getMousePrimaryButton(callback: AsyncCallback<PrimaryButton>): void
```

Obtains the current primary mouse button. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-pointer-function getMousePrimaryButton(callback: AsyncCallback<PrimaryButton>): void--><!--Device-pointer-function getMousePrimaryButton(callback: AsyncCallback<PrimaryButton>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PrimaryButton&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Obtain the primary mouse button.
            pointer.getMousePrimaryButton((error: BusinessError, primary: pointer.PrimaryButton) => {
              if (error) {
                console.error(`Failed to get mouse primary button, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              } else {
                console.info(`Succeeded in getting mouse primary button, primary: ${JSON.stringify(primary)}.`);
              }
            });
          } catch (error) {
            console.error(`Failed to get mouse primary button, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getMousePrimaryButton

```TypeScript
function getMousePrimaryButton(): Promise<PrimaryButton>
```

Obtains the current primary mouse button. This API uses a promise to return the result.

**Since:** 10

<!--Device-pointer-function getMousePrimaryButton(): Promise<PrimaryButton>--><!--Device-pointer-function getMousePrimaryButton(): Promise<PrimaryButton>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PrimaryButton&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Obtain the primary mouse button.
            pointer.getMousePrimaryButton().then((primary: pointer.PrimaryButton) => {
              console.info(`Succeeded in getting mouse primary button, primary: ${JSON.stringify(primary)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get mouse primary button, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get mouse primary button, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
