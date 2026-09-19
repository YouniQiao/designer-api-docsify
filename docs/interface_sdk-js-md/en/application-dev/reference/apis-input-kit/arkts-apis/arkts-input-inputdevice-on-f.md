# on

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## on('change')

```TypeScript
function on(type: 'change', listener: Callback<DeviceListener>): void
```

Registers a listener for input device hot-swap events. This feature requires connecting external devices such as a mouse, keyboard, or touchscreen. This API uses an asynchronous callback to return the result. You are advised to execute this operation on the main application thread and unregister the listener before the thread exits.

**Since:** 9

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | Event type. This field has a fixed value of **change**. |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceListener](arkts-input-inputdevice-devicelistener-i.md)&gt; | Yes | Callback used to return the input device hot swap events. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
