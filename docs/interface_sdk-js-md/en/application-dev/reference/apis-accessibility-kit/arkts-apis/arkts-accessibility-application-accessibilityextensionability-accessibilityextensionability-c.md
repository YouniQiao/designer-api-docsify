# AccessibilityExtensionAbility

The **AccessibilityExtensionAbility** module provides accessibility extension capabilities based on the ExtensionAbility framework.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class AccessibilityExtensionAbility--><!--Device-unnamed-declare class AccessibilityExtensionAbility-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { Rect, TouchPosition, AccessibilityVirtualNode, ElementAttributeKeys, FocusCondition, AccessibilityExtensionContext, ElementAttributeValues, AccessibilityEventInfo, AccessibilityEvent, AccessibilityElement, FocusRule, FocusMoveResult, FocusType, Parameter, FocusDirection, WindowType } from '@kit.AccessibilityKit';
```

## onAccessibilityEvent

```TypeScript
onAccessibilityEvent(event: AccessibilityEvent): void
```

Called when an event that matches the specified bundle and event type occurs. In this API, you can implement event- specific service logic. Generally, this API needs to be overridden.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityExtensionAbility-onAccessibilityEvent(event: AccessibilityEvent): void--><!--Device-AccessibilityExtensionAbility-onAccessibilityEvent(event: AccessibilityEvent): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [AccessibilityEvent](arkts-accessibility-application-accessibilityextensionability-accessibilityevent-i.md) | Yes | Accessibility event. No return value. |

## Examples

```TypeScript
import { AccessibilityExtensionAbility, AccessibilityEvent } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onAccessibilityEvent(event: AccessibilityEvent): void {
    console.info('AxExtensionAbility onAccessibilityEvent');
    if (event.eventType === 'click') {
      console.info('AxExtensionAbility onAccessibilityEvent: click');
    }
  }
}
```

## onConnect

```TypeScript
onConnect(): void
```

Called when the **AccessibilityExtensionAbility** is enabled and connected to the system service. In this API, you can have the service logic initialized. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityExtensionAbility-onConnect(): void--><!--Device-AccessibilityExtensionAbility-onConnect(): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Examples

```TypeScript
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onConnect(): void {
    console.info('AxExtensionAbility onConnect');
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(): void
```

Called when the **AccessibilityExtensionAbility** is disabled and disconnected from the system service. In this API , you can implement the service logic of resource release and exit. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityExtensionAbility-onDisconnect(): void--><!--Device-AccessibilityExtensionAbility-onDisconnect(): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Examples

```TypeScript
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onDisconnect(): void {
    console.info('AxExtensionAbility onDisconnect');
  }
}
```

## onKeyEvent

```TypeScript
onKeyEvent(keyEvent: KeyEvent): boolean
```

Called when a physical key is pressed. In this API, you can determine whether to consume the event based on the service.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityExtensionAbility-onKeyEvent(keyEvent: KeyEvent): boolean--><!--Device-AccessibilityExtensionAbility-onKeyEvent(keyEvent: KeyEvent): boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyEvent | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | Yes | Key event. If **true** is returned, the key is consumed. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the event is consumed and will not be transferred;&lt;br&gt;returns **false** if the event is not consumed and will be transferred. |

## Examples

```TypeScript
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';
import { KeyEvent } from '@kit.InputKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onKeyEvent(keyEvent: KeyEvent): boolean {
    console.info('AxExtensionAbility onKeyEvent');
    if (keyEvent.key.code === 16) {
      console.info('AxExtensionAbility onKeyEvent: intercept 16');
      return true;
    }
    return false;
  }
}
```

## context

```TypeScript
context: AccessibilityExtensionContext
```

Context of the accessibility extension ability.

**Type:** [AccessibilityExtensionContext](arkts-accessibility-accessibilityextensioncontext-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AccessibilityExtensionAbility-context: AccessibilityExtensionContext--><!--Device-AccessibilityExtensionAbility-context: AccessibilityExtensionContext-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

