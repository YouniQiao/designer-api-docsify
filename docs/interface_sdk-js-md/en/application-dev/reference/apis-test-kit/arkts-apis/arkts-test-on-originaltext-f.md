# originalText

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## originalText

```TypeScript
export function originalText(text: string, pattern?: MatchPattern): On
```

Specifies the original text for the target Component. If the accessibility property [accessibilityLevel](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#accessibilityLevel) of a component is set to 'no' or 'no-hide-descendants', you will not be able to use [text](arkts-test-uitest-on-c.md#text) to match the component with the specified original text, but you can use this method to achieve it; if the component does not set the above accessibility property, this method has no difference with [text](arkts-test-uitest-on-c.md#text)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ON-export function originalText(text: string, pattern?: MatchPattern): On--><!--Device-ON-export function originalText(text: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | the original text value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | the [MatchPattern](arkts-test-uitest-matchpattern-e.md#MatchPattern) of the text value. &lt;br&gt;Default value: [EQUALS](arkts-test-uitest-matchpattern-e.md#EQUALS) |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

