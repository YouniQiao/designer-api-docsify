# MouseController

Provides the capability of simulating mouse operations. The simulated mouse operation sequence must meet the following requirements: 1. A mouse button can be pressed only when it is in the released state. 2. A mouse button can only be released after it has been pressed. 3. A valid axis event sequence must begin with a **beginAxis** call, followed by zero or more **updateAxis** calls, and end with an **endAxis** call. 4. Only one axis event sequence can be in progress at a time.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-inputEventClient-interface MouseController--><!--Device-inputEventClient-interface MouseController-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from '@kit.InputKit';
```

## beginAxis

```TypeScript
beginAxis(axis: Axis, value: number): Promise<void>
```

Starts an axis event. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseController-beginAxis(axis: Axis, value: int): Promise<void>--><!--Device-MouseController-beginAxis(axis: Axis, value: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| axis | [Axis](arkts-input-multimodalinput-mouseevent-axis-e.md) | Yes |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [4300001](../errorcode-inputeventclient.md#4300001-status-error) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { inputEventClient, Axis } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputEventClient.createMouseController()
            .then((mouseController: inputEventClient.MouseController) => {
              mouseController.beginAxis(Axis.SCROLL_VERTICAL, 10);
              return mouseController;
            })
            .then((mouseController: inputEventClient.MouseController) => {
              mouseController.updateAxis(Axis.SCROLL_VERTICAL, 20);
              return mouseController;
            })
            .then((mouseController: inputEventClient.MouseController) => {
              mouseController.endAxis(Axis.SCROLL_VERTICAL);
            })
            .then(() => {
              console.info('Succeeded in ending axis event');
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to end axis event. Code: ${error.code}, message: ${error.message}.`);
            });
        })
    }
  }
}
```

## endAxis

```TypeScript
endAxis(axis: Axis): Promise<void>
```

Ends an axis event. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseController-endAxis(axis: Axis): Promise<void>--><!--Device-MouseController-endAxis(axis: Axis): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| axis | [Axis](arkts-input-multimodalinput-mouseevent-axis-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [4300001](../errorcode-inputeventclient.md#4300001-status-error) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

For details, see [beginAxis](#beginAxis).

## moveTo

```TypeScript
moveTo(displayId: number, displayX: number, displayY: number): Promise<void>
```

Moves the mouse cursor to the specified display coordinates. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseController-moveTo(displayId: int, displayX: int, displayY: int): Promise<void>--><!--Device-MouseController-moveTo(displayId: int, displayX: int, displayY: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |
| displayX | number | Yes |
| displayY | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [4300002](../errorcode-inputeventclient.md#4300002-display-does-not-exist) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { inputEventClient } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputEventClient.createMouseController()
            .then(mouseController => {
              return mouseController.moveTo(0, 100, 200);
            })
            .then(() => {
              console.info('Succeeded in moving mouse');
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to move mouse. Code: ${error.code}, message: ${error.message}.`);
            });
        })
    }
  }
}
```

## pressButton

```TypeScript
pressButton(button: Button): Promise<void>
```

Presses a mouse button. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseController-pressButton(button: Button): Promise<void>--><!--Device-MouseController-pressButton(button: Button): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| button | [Button](arkts-input-multimodalinput-mouseevent-button-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [4300001](../errorcode-inputeventclient.md#4300001-status-error) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { inputEventClient, Button } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputEventClient.createMouseController()
            .then((mouseController: inputEventClient.MouseController) => {
              mouseController.pressButton(Button.LEFT);
              return mouseController;
            })
            .then((mouseController: inputEventClient.MouseController) => {
              mouseController.releaseButton(Button.LEFT);
            })
            .then(() => {
              console.info('Succeeded in releasing mouse button');
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to release mouse button. Code: ${error.code}, message: ${error.message}.`);
            });
        })
    }
  }
}
```

## releaseButton

```TypeScript
releaseButton(button: Button): Promise<void>
```

Release a mouse button. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseController-releaseButton(button: Button): Promise<void>--><!--Device-MouseController-releaseButton(button: Button): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| button | [Button](arkts-input-multimodalinput-mouseevent-button-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [4300001](../errorcode-inputeventclient.md#4300001-status-error) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

For details, see [pressButton](#pressButton).

## updateAxis

```TypeScript
updateAxis(axis: Axis, value: number): Promise<void>
```

Updates an axis event. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseController-updateAxis(axis: Axis, value: int): Promise<void>--><!--Device-MouseController-updateAxis(axis: Axis, value: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| axis | [Axis](arkts-input-multimodalinput-mouseevent-axis-e.md) | Yes |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [4300001](../errorcode-inputeventclient.md#4300001-status-error) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

For details, see [beginAxis](#beginAxis).
