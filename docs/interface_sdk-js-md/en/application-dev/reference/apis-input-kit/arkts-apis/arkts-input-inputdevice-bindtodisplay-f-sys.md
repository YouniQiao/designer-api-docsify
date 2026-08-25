# bindToDisplay (System API)

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## bindToDisplay

```TypeScript
function bindToDisplay(inputDeviceId: number, displayId: number): Promise<void>
```

Bind input devices to a display. Only external USB and Bluetooth mice, touchpads, keyboards, and game controllers are supported. After binding, the device will be fixed to operate on the display group where the specified display is located. This API uses a promise to return the result.

**Since:** 26.1.0

**Required permissions:** ohos.permission.INPUT_DEVICE_CONTROLLER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputDeviceId | number | Yes |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
| [3900001](../errorcode-inputdevice.md#3900001-device-not-exist) |
| 3900004 |
| 3900005 |
