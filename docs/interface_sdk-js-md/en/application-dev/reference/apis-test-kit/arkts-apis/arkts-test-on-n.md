# ON

The static builder for building {@link On}object conveniently,usage example:ON.text('txt').enabled(true).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare namespace ON--><!--Device-unnamed-declare namespace ON-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [text](arkts-test-on-text-f.md#text) | Specifies the text for the target Component. |
| [id](arkts-test-on-id-f.md#id) | Specifies the id of the target Component. |
| [type](arkts-test-on-type-f.md#type) | Specifies the type of the target Component. |
| [clickable](arkts-test-on-clickable-f.md#clickable) | Specifies the clickable status of the target Component. |
| [longClickable](arkts-test-on-longclickable-f.md#longclickable) | Specifies the longClickable status of the target Component. |
| [scrollable](arkts-test-on-scrollable-f.md#scrollable) | Specifies the scrollable status of the target Component. |
| [enabled](arkts-test-on-enabled-f.md#enabled) | Specifies the enabled status of the target Component. |
| [focused](arkts-test-on-focused-f.md#focused) | Specifies the focused status of the target Component. |
| [selected](arkts-test-on-selected-f.md#selected) | Specifies the selected status of the target Component. |
| [checked](arkts-test-on-checked-f.md#checked) | Specifies the checked status of the target Component. |
| [checkable](arkts-test-on-checkable-f.md#checkable) | Specifies the checkable status of the target Component. |
| [isBefore](arkts-test-on-isbefore-f.md#isbefore) | Requires that the target Component which is before another Component that specified by the given {@link On}object,used to locate Component relatively. |
| [isAfter](arkts-test-on-isafter-f.md#isafter) | Requires that the target Component which is after another Component that specified by the given {@link On}object,used to locate Component relatively. |
| [within](arkts-test-on-within-f.md#within) | Requires that the target Component which is inside of another Component that specified by the given {@link On}object,used to locate Component relatively. |
| [inWindow](arkts-test-on-inwindow-f.md#inwindow) | Specifies the bundleName of the application which the window that the target Component is located belongs. |
| [belongingDisplay](arkts-test-on-belongingdisplay-f.md#belongingdisplay) | Specifies the displayId to which the target Component belongs. |
| [description](arkts-test-on-description-f.md#description) | Specifies the description for the target Component. |
| [id](arkts-test-on-id-f.md#id-1) | Specifies the id of the target Component. |
| [type](arkts-test-on-type-f.md#type-1) | Specifies the type of the target Component. |
| [hint](arkts-test-on-hint-f.md#hint) | Specifies the hint for the target Component. |
| [originalText](arkts-test-on-originaltext-f.md#originaltext) | Specifies the original text for the target Component.If the accessibility property  [accessibilityLevel](../../apis-arkui/arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#accessibilitylevel)of a component is set to 'no' or 'no-hide-descendants',you will not be able to use {@link On.text} to match the component with the specified original text, but you can use this method to achieve it;if the component does not set the above accessibility property, this method has no difference with {@link On.text} |
| [beforeComponent](arkts-test-on-beforecomponent-f.md#beforecomponent) | Requires that the target Component which is before another Component that specified by the given {@link Component}object,used to locate Component relatively. |
| [afterComponent](arkts-test-on-aftercomponent-f.md#aftercomponent) | Requires that the target Component which is after another Component that specified by the given {@link Component}object,used to locate Component relatively. |
| [withinComponent](arkts-test-on-withincomponent-f.md#withincomponent) | Requires that the target Component which is inside of another Component that specified by the given {@link Component}object,used to locate Component relatively. |

