# KeyboardController

Provides the capability of simulating key operations. The simulated key operation sequence must meet the following requirements:
1. A key can only be pressed when it is in the released state, or when it is the most recently pressed key and
has not been released.
2. A key can only be released after it has been pressed.
3. A maximum of five keys can be pressed and held simultaneously.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from '@kit.InputKit';
```

## pressKey

```TypeScript
pressKey(keyCode: KeyCode): Promise<void>
```

Presses a key. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyCode | [KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [4300001](../errorcode-inputeventclient.md#4300001-status-error) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |

## releaseKey

```TypeScript
releaseKey(keyCode: KeyCode): Promise<void>
```

Releases a key. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyCode | [KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [4300001](../errorcode-inputeventclient.md#4300001-status-error) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
