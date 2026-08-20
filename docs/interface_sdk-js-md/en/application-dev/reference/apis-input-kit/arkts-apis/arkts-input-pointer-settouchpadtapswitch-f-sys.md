# setTouchpadTapSwitch (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setTouchpadTapSwitch

```TypeScript
function setTouchpadTapSwitch(state: boolean, callback: AsyncCallback<void>): void
```

Sets the touchpad tap switch. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-pointer-function setTouchpadTapSwitch(state: boolean, callback: AsyncCallback<void>): void--><!--Device-pointer-function setTouchpadTapSwitch(state: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | boolean | Yes | Tap switch status of the touchpad The value **true** indicates that the switch is enabled, and the value **false** indicates the opposite. The default value is **true**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

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
            pointer.setTouchpadTapSwitch(true, (error: BusinessError) => {
              if (error) {
                console.error(`setTouchpadTapSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`setTouchpadTapSwitch success`);
            });
          } catch (error) {
            console.error(`setTouchpadTapSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`); 
          }
        })
    }
  }
}
```


## setTouchpadTapSwitch

```TypeScript
function setTouchpadTapSwitch(state: boolean): Promise<void>
```

Sets the touchpad tap switch. This API uses a promise to return the result.

**Since:** 23

<!--Device-pointer-function setTouchpadTapSwitch(state: boolean): Promise<void>--><!--Device-pointer-function setTouchpadTapSwitch(state: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | boolean | Yes | State of the touchpad tap switch. The value **true** indicates that the switch is enabled, and the value **false** indicates the opposite. The default value is **true**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

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
            pointer.setTouchpadTapSwitch(false).then(() => {
              console.info(`setTouchpadTapSwitch success`);
            }).catch((error: BusinessError) => {
              console.error(`Set touchpad tap switch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`setTouchpadTapSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

