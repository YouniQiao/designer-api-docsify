# onChange

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## onChange

```TypeScript
function onChange(listener: Callback<DeviceListener>): void
```

Starts listening for an input device event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputDevice-function onChange(listener: Callback<DeviceListener>): void--><!--Device-inputDevice-function onChange(listener: Callback<DeviceListener>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceListener&gt; | Yes | Callback for the input device event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

