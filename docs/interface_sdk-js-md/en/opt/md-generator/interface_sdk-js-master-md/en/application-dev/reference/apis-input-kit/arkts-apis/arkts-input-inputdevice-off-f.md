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

<!--Device-inputDevice-function off(type: 'change', listener?: Callback<DeviceListener>): void--><!--Device-inputDevice-function off(type: 'change', listener?: Callback<DeviceListener>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceListener](arkts-input-inputdevice-devicelistener-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
