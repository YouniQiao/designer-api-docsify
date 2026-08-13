# AccessibilityActionInterceptCallback

```TypeScript
export declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult
```

Defines the callback type used in accessibility action intercept. The value of action indicates the accessibility action type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult--><!--Device-unnamed-export declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | [AccessibilityAction](arkts-na-common-accessibilityaction-e.md) | Yes | the enum of accessibility action type. |

**Return value:**

| Type | Description |
| --- | --- |
| [AccessibilityActionInterceptResult](arkts-na-common-accessibilityactioninterceptresult-e.md) | the result of continuing to execute the action or interrupting it or bubbling up |

