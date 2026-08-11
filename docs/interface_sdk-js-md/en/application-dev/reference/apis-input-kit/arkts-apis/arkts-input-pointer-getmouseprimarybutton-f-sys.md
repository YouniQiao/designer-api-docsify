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

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function getMousePrimaryButton(callback: AsyncCallback<PrimaryButton>): void--><!--Device-pointer-function getMousePrimaryButton(callback: AsyncCallback<PrimaryButton>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PrimaryButton&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **PrimaryButton** is the obtained key value. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

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
            pointer.getMousePrimaryButton((error: BusinessError, primary: pointer.PrimaryButton) => {
              if (error) {
                console.error(`Get mouse primary button failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
              } else {
                console.info(`Get mouse primary button success, primary: ${JSON.stringify(primary)}`);
              }
            });
          } catch (error) {
            console.error(`Get mouse primary button failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
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

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function getMousePrimaryButton(): Promise<PrimaryButton>--><!--Device-pointer-function getMousePrimaryButton(): Promise<PrimaryButton>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PrimaryButton&gt; | Promise used to return the primary mouse button. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

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
            pointer.getMousePrimaryButton().then((primary: pointer.PrimaryButton) => {
              console.info(`Get mouse primary button success, primary: ${JSON.stringify(primary)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get mouse failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Get mouse primary button failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

