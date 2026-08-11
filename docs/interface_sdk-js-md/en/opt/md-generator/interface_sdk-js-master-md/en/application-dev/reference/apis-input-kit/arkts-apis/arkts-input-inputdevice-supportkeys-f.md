# supportKeys

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## supportKeys

```TypeScript
function supportKeys(deviceId: number, keys: Array<KeyCode>, callback: AsyncCallback<Array<boolean>>): void
```

Queries whether a specified input device supports specified keys. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-inputDevice-function supportKeys(deviceId: int, keys: Array<KeyCode>, callback: AsyncCallback<Array<boolean>>): void--><!--Device-inputDevice-function supportKeys(deviceId: int, keys: Array<KeyCode>, callback: AsyncCallback<Array<boolean>>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| keys | Array&lt;[KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;boolean&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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
          // Check whether the input device whose ID is 1 supports keys 17, 22, and 2055.
          try {
            // Querying Key Support
            inputDevice.supportKeys(1, [17, 22, 2055], (error: BusinessError, supportResult: Array<Boolean>) => {
              console.info(`Succeeded in querying support keys, supportResult: ${JSON.stringify(supportResult)}.`);
            });
          } catch (error) {
            console.error(`Failed to query support key, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## supportKeys

```TypeScript
function supportKeys(deviceId: number, keys: Array<KeyCode>): Promise<Array<boolean>>
```

Checks whether the input device supports the specified keys. This API uses a promise to return the result.

**Since:** 9

<!--Device-inputDevice-function supportKeys(deviceId: int, keys: Array<KeyCode>): Promise<Array<boolean>>--><!--Device-inputDevice-function supportKeys(deviceId: int, keys: Array<KeyCode>): Promise<Array<boolean>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| keys | Array&lt;[KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;boolean&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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
          // Check whether the input device whose ID is 1 supports keys 17, 22, and 2055.
          try {
            // Querying Key Support
            inputDevice.supportKeys(1, [17, 22, 2055]).then((supportResult: Array<Boolean>) => {
              console.info(`Succeeded in querying support keys, result: ${JSON.stringify(supportResult)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to query support Keys, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to query support key, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
