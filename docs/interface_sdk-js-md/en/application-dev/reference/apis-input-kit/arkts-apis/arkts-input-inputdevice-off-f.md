# off

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## off('change')

```TypeScript
function off(type: 'change', listener?: Callback<DeviceListener>): void
```

Disables listening for device hot swap events. This API is called before the application exits. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-inputDevice-function off(type: 'change', listener?: Callback<DeviceListener>): void--><!--Device-inputDevice-function off(type: 'change', listener?: Callback<DeviceListener>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | Event type. This field has a fixed value of **change**. |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceListener](arkts-input-inputdevice-devicelistener-i.md)&gt; | No | Callback to unregister. If this parameter is left unspecified, listening for hot swap events of all input devices will be canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

