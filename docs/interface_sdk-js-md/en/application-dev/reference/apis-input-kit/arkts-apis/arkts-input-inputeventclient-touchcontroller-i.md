# TouchController

Provides the capability of simulating touch operations. The simulated touch operation sequence must meet the following requirements:
1. All touch points must share the same **displayId**.
2. Each touch point must begin with a **touchDown()** call, followed by zero or more **touchMove()** calls, and end
with an **touchUp()** call.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from '@kit.InputKit';
```

## touchDown

```TypeScript
touchDown(touch: TouchPoint): Promise<void>
```

Presses down a touch point. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [4300001](../errorcode-inputeventclient.md#4300001-status-error) |
| [4300002](../errorcode-inputeventclient.md#4300002-display-does-not-exist) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |

## touchMove

```TypeScript
touchMove(touch: TouchPoint): Promise<void>
```

Moves a touch point. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | Yes |

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

## touchUp

```TypeScript
touchUp(touch: TouchPoint): Promise<void>
```

Releases a touch point. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | Yes |

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
