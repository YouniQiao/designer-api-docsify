# onAnimationReduceStateChange

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { accessibility } from '@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from '@kit.AccessibilityKit';
import { GesturePath } from '@kit.AccessibilityKit';
import { GesturePoint } from '@kit.AccessibilityKit';
```

## onAnimationReduceStateChange

```TypeScript
function onAnimationReduceStateChange(callback: Callback<boolean>): void
```

Subscribes to the state changes of animation reduction mode. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; - The callback parameter for registering a listener must use a named function instead of an anonymous function. &gt; Otherwise, a new underlying object is created each time the function is called, causing memory leakage. &gt; &gt; - After calling this method, ensure that &gt; [accessibility.offAnimationReduceStateChange](arkts-accessibility-accessibility-offanimationreducestatechange-f.md) is used to &gt; unsubscribe before the component instance is destroyed (for example, in the **aboutToDisappear** lifecycle &gt; callback). Otherwise, a crash may occur.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function onAnimationReduceStateChange(callback: Callback<boolean>): void--><!--Device-accessibility-function onAnimationReduceStateChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | Callback invoked when the reduced motion mode status changes. The value **true** indicates that the reduced motion mode is enabled, and **false** indicates that the reduced motion mode is disabled. |

**Examples**

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe animationReduce state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onAnimationReduceStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

