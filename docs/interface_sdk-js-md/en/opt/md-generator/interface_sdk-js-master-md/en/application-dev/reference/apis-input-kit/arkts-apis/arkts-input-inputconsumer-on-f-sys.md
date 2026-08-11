# on (System API)

## Modules to Import

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## on('key')

```TypeScript
function on(type: 'key', keyOptions: KeyOptions, callback: Callback<KeyOptions>): void
```

Enables listening for system hotkey change events. This API uses an asynchronous callback to return the system hotkey data when a system hotkey event that meets the specified condition occurs.

> **NOTE：**
> 
> - You can subscribe to only the Down event of a key, or subscribe to both the Down and Up events of a key.
> 
> - If you subscribe to only the Up event of a key, the Down event may be consumed by the focus window, and the Up
> event may not be closed. In this case, check whether the design and implementation are proper.

**Since:** 8

<!--Device-inputConsumer-function on(type: 'key', keyOptions: KeyOptions, callback: Callback<KeyOptions>): void--><!--Device-inputConsumer-function on(type: 'key', keyOptions: KeyOptions, callback: Callback<KeyOptions>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'key' | Yes |
| keyOptions | [KeyOptions](../../apis-test-kit/arkts-apis/arkts-test-uitest-keyoptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;KeyOptions&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
          let leftAltKey = 2045;
          let tabKey = 2049;
          let keyOptions: inputConsumer.KeyOptions = {
            preKeys: [ leftAltKey ],
            finalKey: tabKey,
            isFinalKeyDown: true,
            finalKeyDownDuration: 0
          };
          let callback = (keyOptions: inputConsumer.KeyOptions) => {
            console.info(`keyOptions: ${JSON.stringify(keyOptions)}`);
          }
          try {
            inputConsumer.on("key", keyOptions, callback);
          } catch (error) {
            console.error(`Subscribe failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```
