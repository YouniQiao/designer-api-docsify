# offHotkeyChange

## Modules to Import

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## offHotkeyChange

```TypeScript
function offHotkeyChange(hotkeyOptions: HotkeyOptions, callback?: Callback<HotkeyOptions>): void
```

Unsubscribe from hotkey event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputConsumer-function offHotkeyChange(hotkeyOptions: HotkeyOptions, callback?: Callback<HotkeyOptions>): void--><!--Device-inputConsumer-function offHotkeyChange(hotkeyOptions: HotkeyOptions, callback?: Callback<HotkeyOptions>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hotkeyOptions | [HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md) | Yes | Hotkey options. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HotkeyOptions&gt; | No | Callback used to return hotkey event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

