# setTouchpadDoubleTapAndDragState (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setTouchpadDoubleTapAndDragState

```TypeScript
function setTouchpadDoubleTapAndDragState(isOpen: boolean, callback: AsyncCallback<void>): void
```

Sets the touchpad double-tap and drag switch state. This API uses an asynchronous callback to return the result.

**Since:** 14

<!--Device-pointer-function setTouchpadDoubleTapAndDragState(isOpen: boolean, callback: AsyncCallback<void>): void--><!--Device-pointer-function setTouchpadDoubleTapAndDragState(isOpen: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isOpen](../../apis-network-kit/arkts-apis/arkts-network-netfirewall-netfirewallpolicy-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
            // Set the touchpad double-tap and drag switch state.
            pointer.setTouchpadDoubleTapAndDragState(true, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to set touchpad double tap and drag state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in setting touchpad double tap and drag state.`);
            });
          } catch (error) {
            console.error(`Failed to set touchpad double tap and drag state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## setTouchpadDoubleTapAndDragState

```TypeScript
function setTouchpadDoubleTapAndDragState(isOpen: boolean): Promise<void>
```

Sets the touchpad double-tap and drag switch state. This API uses a promise to return the result.

**Since:** 14

<!--Device-pointer-function setTouchpadDoubleTapAndDragState(isOpen: boolean): Promise<void>--><!--Device-pointer-function setTouchpadDoubleTapAndDragState(isOpen: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isOpen](../../apis-network-kit/arkts-apis/arkts-network-netfirewall-netfirewallpolicy-i.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
            // Set the touchpad double-tap and drag switch state.
            pointer.setTouchpadDoubleTapAndDragState(false).then(() => {
              console.info(`Succeeded in setting touchpad double tap and drag state.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set touchpad double tap and drag state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to set touchpad double tap and drag state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
