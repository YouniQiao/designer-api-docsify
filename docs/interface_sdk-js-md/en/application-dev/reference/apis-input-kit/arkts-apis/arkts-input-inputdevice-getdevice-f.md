# getDevice

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getDevice

```TypeScript
function getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void
```

Obtains the information about the input device with the specified ID. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use
> [inputDevice.getDeviceInfo](arkts-input-inputdevice-getdeviceinfo-f.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getDeviceInfo

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md)&gt; | Yes |


## getDevice

```TypeScript
function getDevice(deviceId: number): Promise<InputDeviceData>
```

Obtains the information about the input device with the specified ID. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use
> [inputDevice.getDeviceInfo](arkts-input-inputdevice-getdeviceinfo-f.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getDeviceInfo

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md)&gt; |
