# on

## Modules to Import

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## on('hotkeyChange')

```TypeScript
function on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void
```

Subscribes to application shortcut key change events. This API obtains combination key input events that meet the specified conditions, and uses an asynchronous callback to return the result.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-inputConsumer-function on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void--><!--Device-inputConsumer-function on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hotkeyChange' | Yes | Event type. This parameter has a fixed value of **hotkeyChange**. |
| hotkeyOptions | [HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md) | Yes | Shortcut key options. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HotkeyOptions&gt; | Yes | Callback used to return the combination key input events that meet the conditions. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [4200002](../errorcode-inputconsumer.md#4200002-shortcut-key-already-registered-by-a-system-application) | The hotkey has been used by the system. |
| [4200003](../errorcode-inputconsumer.md#4200003-shortcut-key-already-registered-by-another-application) | The hotkey has been subscribed to by another. |

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
          let leftCtrlKey = 2072;
          let zKey = 2042;
          let hotkeyOptions: inputConsumer.HotkeyOptions = {
            preKeys: [leftCtrlKey],
            finalKey: zKey,
            isRepeat: true
          };
          let hotkeyCallback = (hotkeyOptions: inputConsumer.HotkeyOptions) => {
            console.info(`hotkeyOptions: ${JSON.stringify(hotkeyOptions)}`);
          }
          try {
            inputConsumer.on("hotkeyChange", hotkeyOptions, hotkeyCallback);
          } catch (error) {
            console.error(`Subscribe failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## on('keyPressed')

```TypeScript
function on(type: 'keyPressed', options: KeyPressedConfig, callback: Callback<KeyEvent>): void
```

Subscribes to key press events. If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed. This API uses an asynchronous callback to return the result.

If the API call is successful, the system's default response to the key event will be intercepted; that is, system-level actions, such as volume adjustment, will no longer be triggered. To restore the system response, call  
[off](inputConsumer.off(type: 'keyPressed', callback?: Callback&lt;KeyEvent&gt;)) to disable listening for the key event.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn only, since version 16.

<!--Device-inputConsumer-function on(type: 'keyPressed', options: KeyPressedConfig, callback: Callback<KeyEvent>): void--><!--Device-inputConsumer-function on(type: 'keyPressed', options: KeyPressedConfig, callback: Callback<KeyEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyPressed' | Yes | Event type. This parameter has a fixed value of **keyPressed**. |
| options | [KeyPressedConfig](arkts-input-inputconsumer-keypressedconfig-i.md) | Yes | Sets the key event consumption configuration. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | Yes | Callback used to return key press events. Ensure that different callbacks are used for different key events. Otherwise, the subscription does not take effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

## Examples

```TypeScript
import { inputConsumer, KeyEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let options: inputConsumer.KeyPressedConfig = {
              key: 16,
              action: 1,
              isRepeat: false,
            }
            inputConsumer.on('keyPressed', options, (event: KeyEvent) => {
              console.info(`Subscribe success ${JSON.stringify(event)}`);
            });
          } catch (error) {
            console.error(`Subscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

