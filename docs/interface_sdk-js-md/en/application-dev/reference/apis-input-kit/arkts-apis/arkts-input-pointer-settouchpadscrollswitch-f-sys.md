# setTouchpadScrollSwitch (System API)

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## setTouchpadScrollSwitch

```TypeScript
function setTouchpadScrollSwitch(state: boolean, callback: AsyncCallback<void>): void
```

Sets the touchpad scroll switch. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function setTouchpadScrollSwitch(state: boolean, callback: AsyncCallback<void>): void--><!--Device-pointer-function setTouchpadScrollSwitch(state: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | boolean | Yes | Scroll switch status. The value **true** indicates that the switch is enabled, and the value **false** indicates the opposite. The default value is **true**. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

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
            pointer.setTouchpadScrollSwitch(true, (error: BusinessError) => {
              if (error) {
                console.error(`setTouchpadScrollSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`setTouchpadScrollSwitch success`);
            });
          } catch (error) {
            console.error(`setTouchpadScrollSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## setTouchpadScrollSwitch

```TypeScript
function setTouchpadScrollSwitch(state: boolean): Promise<void>
```

Sets the touchpad scroll switch. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function setTouchpadScrollSwitch(state: boolean): Promise<void>--><!--Device-pointer-function setTouchpadScrollSwitch(state: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | boolean | Yes | Scroll switch status. The value **true** indicates that the switch is enabled, and the value **false** indicates the opposite. The default value is **true**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

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
            pointer.setTouchpadScrollSwitch(false).then(() => {
              console.info(`setTouchpadScrollSwitch success`);
            }).catch((error: BusinessError) => {
              console.error(`Set touchpad scroll switch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`setTouchpadScrollSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

