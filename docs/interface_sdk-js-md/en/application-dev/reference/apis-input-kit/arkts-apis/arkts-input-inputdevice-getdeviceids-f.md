# getDeviceIds

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getDeviceIds

```TypeScript
function getDeviceIds(callback: AsyncCallback<Array<number>>): void
```

Obtains the IDs of all input devices. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use
> [inputDevice.getDeviceList](arkts-input-inputdevice-getdevicelist-f.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getDeviceList

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |


## getDeviceIds

```TypeScript
function getDeviceIds(): Promise<Array<number>>
```

Obtains the IDs of all input devices. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use
> [inputDevice.getDeviceList](arkts-input-inputdevice-getdevicelist-f.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getDeviceList

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |
