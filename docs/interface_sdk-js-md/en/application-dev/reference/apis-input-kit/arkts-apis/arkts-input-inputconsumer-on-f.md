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

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hotkeyChange' | Yes |
| hotkeyOptions | [HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [4200002](../errorcode-inputconsumer.md#4200002-shortcut-key-already-registered-by-a-system-application) |
| [4200003](../errorcode-inputconsumer.md#4200003-shortcut-key-already-registered-by-another-application) |


## on('keyPressed')

```TypeScript
function on(type: 'keyPressed', options: KeyPressedConfig, callback: Callback<KeyEvent>): void
```

Subscribes to key press events. If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed. This API uses an asynchronous callback to return the result.If the API call is successful, the system's default response to the key event will be intercepted; that is, system- level actions, such as volume adjustment, will no longer be triggered. To restore the system response, call off to disable listening for the key event.

**Since:** 16

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyPressed' | Yes |
| options | [KeyPressedConfig](arkts-input-inputconsumer-keypressedconfig-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
