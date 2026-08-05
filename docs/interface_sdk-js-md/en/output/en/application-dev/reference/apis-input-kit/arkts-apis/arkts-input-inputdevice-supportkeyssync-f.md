# supportKeysSync

## supportKeysSync

```TypeScript
function supportKeysSync(deviceId: int, keys: Array<KeyCode>): Array<boolean>
```

Checks whether the input device supports the specified keys.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputDevice-function supportKeysSync(deviceId: int, keys: Array<KeyCode>): Array<boolean>--><!--Device-inputDevice-function supportKeysSync(deviceId: int, keys: Array<KeyCode>): Array<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| keys | Array&lt;KeyCode&gt; | Yes | Keys to be queried. A maximum of five keys can be specified. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;boolean&gt; | Result indicating whether the input device supports the keycode value. The value |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

```TypeScript
import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Check whether the input device whose ID is 1 supports keys 17, 22, and 2055.
          try {
            let supportResult: Array<Boolean> = inputDevice.supportKeysSync(1, [17, 22, 2055])
            console.info(`Query result: ${JSON.stringify(supportResult)}`)
          } catch (error) {
            console.error(`Query failed, error: ${JSON.stringify(error, [`code`, `message`])}`)
          }
        })
    }
  }
}
```

