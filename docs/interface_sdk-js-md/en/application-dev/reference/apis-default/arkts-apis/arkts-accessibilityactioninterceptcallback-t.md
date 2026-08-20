# AccessibilityActionInterceptCallback

```TypeScript
export declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult
```

Defines the callback type used in accessibility action intercept. The value of action indicates the accessibility action type.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult--><!--Device-unnamed-export declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | [AccessibilityAction](arkts-common-accessibilityaction-e.md) | Yes | the enum of accessibility action type. |

**Return value:**

| Type | Description |
| --- | --- |
| [AccessibilityActionInterceptResult](arkts-common-accessibilityactioninterceptresult-e.md) | the result of continuing to execute the action or interrupting it or bubbling up |

