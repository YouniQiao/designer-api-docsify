# ON

The static builder for building [On](arkts-test-uitest-on-c.md)object conveniently,usage example:ON.text('txt').enabled(true).

**Since:** 23

<!--Device-unnamed-declare namespace ON--><!--Device-unnamed-declare namespace ON-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [text](arkts-test-on-text-f.md) | Specifies the text for the target Component. |
| [id](arkts-test-on-id-f.md) | Specifies the id of the target Component. |
| [type](arkts-test-on-type-f.md) | Specifies the type of the target Component. |
| [clickable](arkts-test-on-clickable-f.md) | Specifies the clickable status of the target Component. |
| [longClickable](arkts-test-on-longclickable-f.md) | Specifies the longClickable status of the target Component. |
| [scrollable](arkts-test-on-scrollable-f.md) | Specifies the scrollable status of the target Component. |
| [enabled](arkts-test-on-enabled-f.md) | Specifies the enabled status of the target Component. |
| [focused](arkts-test-on-focused-f.md) | Specifies the focused status of the target Component. |
| [selected](arkts-test-on-selected-f.md) | Specifies the selected status of the target Component. |
| [checked](arkts-test-on-checked-f.md) | Specifies the checked status of the target Component. |
| [checkable](arkts-test-on-checkable-f.md) | Specifies the checkable status of the target Component. |
| [isBefore](arkts-test-on-isbefore-f.md) | Requires that the target Component which is before another Component that specified by the given [On](arkts-test-uitest-on-c.md) object,used to locate Component relatively. |
| [isAfter](arkts-test-on-isafter-f.md) | Requires that the target Component which is after another Component that specified by the given [On](arkts-test-uitest-on-c.md) object,used to locate Component relatively. |
| [within](arkts-test-on-within-f.md) | Requires that the target Component which is inside of another Component that specified by the given [On](arkts-test-uitest-on-c.md) object,used to locate Component relatively. |
| [inWindow](arkts-test-on-inwindow-f.md) | Specifies the bundleName of the application which the window that the target Component is located belongs. |
| [belongingDisplay](arkts-test-on-belongingdisplay-f.md) | Specifies the displayId to which the target Component belongs. |
| [description](arkts-test-on-description-f.md) | Specifies the description for the target Component. |
| [id](arkts-test-on-id-f.md) | Specifies the id of the target Component. |
| [type](arkts-test-on-type-f.md) | Specifies the type of the target Component. |
| [hint](arkts-test-on-hint-f.md) | Specifies the hint for the target Component. |
| [originalText](arkts-test-on-originaltext-f.md) | Specifies the original text for the target Component. If the accessibility property [accessibilityLevel](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#accessibilitylevel) of a component is set to 'no' or 'no-hide-descendants', you will not be able to use [text](arkts-test-uitest-on-c.md#text) to match the component with the specified original text, but you can use this method to achieve it; if the component does not set the above accessibility property, this method has no difference with [text](arkts-test-uitest-on-c.md#text) |
| [beforeComponent](arkts-test-on-beforecomponent-f.md) | Requires that the target Component which is before another Component that specified by the given [Component](arkts-test-uitest-component-c.md) object,used to locate Component relatively. |
| [afterComponent](arkts-test-on-aftercomponent-f.md) | Requires that the target Component which is after another Component that specified by the given [Component](arkts-test-uitest-component-c.md) object,used to locate Component relatively. |
| [withinComponent](arkts-test-on-withincomponent-f.md) | Requires that the target Component which is inside of another Component that specified by the given [Component](arkts-test-uitest-component-c.md) object,used to locate Component relatively. |

