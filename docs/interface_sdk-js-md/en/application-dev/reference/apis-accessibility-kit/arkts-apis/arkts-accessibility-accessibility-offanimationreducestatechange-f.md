# offAnimationReduceStateChange

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## offAnimationReduceStateChange

```TypeScript
function offAnimationReduceStateChange(callback?: Callback<boolean>): void
```

Unsubscribes from the state changes in animation reduction mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function offAnimationReduceStateChange(callback?: Callback<boolean>): void--><!--Device-accessibility-function offAnimationReduceStateChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | No | Callback function. Cancels the event response of a specified callback object. The value must be the same as the value of callback in [accessibility.onAnimationReduceStateChange](accessibility.onAnimationReduceStateChange(callback: Callback&lt;boolean&gt;)) . If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type. |

## Examples

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

  aboutToDisappear(): void {
    accessibility.offAnimationReduceStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

