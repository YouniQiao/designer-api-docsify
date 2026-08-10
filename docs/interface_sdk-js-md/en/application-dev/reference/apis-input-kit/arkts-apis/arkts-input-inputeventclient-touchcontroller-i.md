# TouchController

提供模拟触控操作的功能。模拟触控操作序列必须满足以下要求：

1. 所有触点的displayId必须相同。2. 每个触点都必须以`touchDown()`开始，以`touchUp()`结束，中间可包含多个`touchMove()`。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-inputEventClient-interface TouchController--><!--Device-inputEventClient-interface TouchController-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## touchDown

```TypeScript
touchDown(touch: TouchPoint): Promise<void>
```

触点按下。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchController-touchDown(touch: TouchPoint): Promise<void>--><!--Device-TouchController-touchDown(touch: TouchPoint): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | Yes | 与屏幕接触的触点信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 4300001 | Invalid input event sequence. Possible causes: &lt;br&gt; 1. The touch point is touching the display; 2. The touch point ID is not within the valid range [0,9]. |
| 4300002 | The display does not exist. |
| 3800001 | Input service exception. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

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
          inputEventClient.createTouchController()
            .then((touchController: inputEventClient.TouchController) => {
              const touchPoint: inputEventClient.TouchPoint = {
                id: 0,
                displayId: 0,
                displayX: 600,
                displayY: 1200
              };
              touchController.touchDown(touchPoint);
              return touchController;
            })
            .then((touchController: inputEventClient.TouchController) => {
              touchController.touchMove({
                id: 0,
                displayId: 0,
                displayX: 720,
                displayY: 1200
              });
              return touchController;
            })
            .then((touchController: inputEventClient.TouchController) => {
              touchController.touchUp({
                id: 0,
                displayId: 0,
                displayX: 720,
                displayY: 1200
              });
            })
            .then(() => {
              console.info('Succeeded in touch up');
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to simulate touch. Code: ${error.code}, message: ${error.message}.`);
            });
        })
    }
  }
}
```

## touchMove

```TypeScript
touchMove(touch: TouchPoint): Promise<void>
```

触点移动。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchController-touchMove(touch: TouchPoint): Promise<void>--><!--Device-TouchController-touchMove(touch: TouchPoint): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | Yes | 需要移动的触点信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 4300001 | Invalid input event sequence. Possible causes: &lt;br&gt; 1. The touch point is not touching the display; 2. The touch point ID is not within the valid range [0,9]. |
| 3800001 | Input service exception. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

## Examples

For details, see [touchDown](#touchdown).

## touchUp

```TypeScript
touchUp(touch: TouchPoint): Promise<void>
```

触点抬起。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchController-touchUp(touch: TouchPoint): Promise<void>--><!--Device-TouchController-touchUp(touch: TouchPoint): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | Yes | 即将离开屏幕的触点信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 4300001 | Invalid input event sequence. Possible causes: &lt;br&gt; 1. The touch point is not touching the display; 2. The touch point ID is not within the valid range [0,9]. |
| 3800001 | Input service exception. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

## Examples

For details, see [touchDown](#touchdown).

