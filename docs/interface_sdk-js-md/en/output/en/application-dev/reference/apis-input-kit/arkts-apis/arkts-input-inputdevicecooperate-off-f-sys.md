# off (System API)

## off('cooperation')

```TypeScript
function off(type: 'cooperation', callback?: AsyncCallback<void>): void
```

Deregisters the listener for screen hopping status changes. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Substitutes:** ohos.cooperate/cooperate#off

<!--Device-inputDeviceCooperate-function off(type: 'cooperation', callback?: AsyncCallback<void>): void--><!--Device-inputDeviceCooperate-function off(type: 'cooperation', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cooperation' | Yes | Event type. The value is **cooperation**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback used to return the result. If the operation is successful,**err** is **undefined**. Otherwise, **err** is undefined. If this parameter is not specified, all callbacks registered by the current application are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |

**Example**

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Unregister a single callback.
          let callbackOn = (msg: object) => {
            console.info(`Keyboard mouse crossing event: ${JSON.stringify(msg)}`);
            return false;
          }
          try {
            inputDeviceCooperate.on('cooperation', callbackOn);
            inputDeviceCooperate.off("cooperation", callbackOn);
          } catch (error) {
            console.error(`Execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Unregister all callbacks.
          let callback = (msg: object) => {
            console.info(`Keyboard mouse crossing event: ${JSON.stringify(msg)}`);
            return false;
          }
          try {
            inputDeviceCooperate.on('cooperation', callback);
            inputDeviceCooperate.off("cooperation");
          } catch (error) {
            console.error(`Execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

