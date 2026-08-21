# off_willDraw

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## off('willDraw')

```TypeScript
export function off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void
```

Unregisters the listener for drawing instruction dispatch in each frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void--><!--Device-uiObserver-export function off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'willDraw' | Yes | Event event. The value **'willDraw'** indicates whether drawing is about to occur. |
| context | [UIContext](arkts-arkui-arkuiuicontext-uicontext-c.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | No | Target listener to unregister. |

