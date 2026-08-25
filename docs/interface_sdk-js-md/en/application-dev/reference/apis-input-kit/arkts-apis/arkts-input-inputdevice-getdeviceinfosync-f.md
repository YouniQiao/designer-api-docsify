# getDeviceInfoSync

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getDeviceInfoSync

```TypeScript
function getDeviceInfoSync(deviceId: number): InputDeviceData
```

Obtains information about the specified input device.

**Since:** 10

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
