# ON

The static builder for building [On](arkts-test-uitest-on-c.md#On)object conveniently,usage example:ON.text('txt').enabled(true).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace ON--><!--Device-unnamed-declare namespace ON-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component } from 'Component';
import { DisplayRotation } from 'DisplayRotation';
import { Driver } from 'Driver';
import { MatchPattern } from 'MatchPattern';
import { MouseButton } from 'MouseButton';
import { ON } from 'ON';
import { On } from 'On';
import { PointerMatrix } from 'PointerMatrix';
import { ResizeDirection } from 'ResizeDirection';
import { UIElementInfo } from 'UIElementInfo';
import { UIEventObserver } from 'UIEventObserver';
import { UiDirection } from 'UiDirection';
import { UiWindow } from 'UiWindow';
import { WindowMode } from 'WindowMode';
import { Point } from 'Point';
import { WindowFilter } from 'WindowFilter';
import { Rect } from 'Rect';
import { TouchPadSwipeOptions } from 'TouchPadSwipeOptions';
import { InputTextMode } from 'InputTextMode';
import { WindowChangeType } from 'WindowChangeType';
import { ComponentEventType } from 'ComponentEventType';
import { WindowChangeOptions } from 'WindowChangeOptions';
import { ComponentEventOptions } from 'ComponentEventOptions';
import { TouchOptions } from 'TouchOptions';
import { KeyOptions } from 'KeyOptions';
import { PenKey } from 'PenKey';
import { PenMode } from 'PenMode';
import { PenKeyOperation } from 'PenKeyOperation';
import { PenKeyOperationOptions } from 'PenKeyOperationOptions';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [text](arkts-test-on-text-f.md#text) | Specifies the text for the target Component. |
| [id](arkts-test-on-id-f.md#id) | Specifies the id of the target Component. |
| [type](arkts-test-on-type-f.md#type) | Specifies the type of the target Component. |
| [clickable](arkts-test-on-clickable-f.md#clickable) | Specifies the clickable status of the target Component. |
| [longClickable](arkts-test-on-longclickable-f.md#longClickable) | Specifies the longClickable status of the target Component. |
| [scrollable](arkts-test-on-scrollable-f.md#scrollable) | Specifies the scrollable status of the target Component. |
| [enabled](arkts-test-on-enabled-f.md#enabled) | Specifies the enabled status of the target Component. |
| [focused](arkts-test-on-focused-f.md#focused) | Specifies the focused status of the target Component. |
| [selected](arkts-test-on-selected-f.md#selected) | Specifies the selected status of the target Component. |
| [checked](arkts-test-on-checked-f.md#checked) | Specifies the checked status of the target Component. |
| [checkable](arkts-test-on-checkable-f.md#checkable) | Specifies the checkable status of the target Component. |
| [isBefore](arkts-test-on-isbefore-f.md#isBefore) | Requires that the target Component which is before another Component that specified by the given [On](arkts-test-uitest-on-c.md#On) object,used to locate Component relatively. |
| [isAfter](arkts-test-on-isafter-f.md#isAfter) | Requires that the target Component which is after another Component that specified by the given [On](arkts-test-uitest-on-c.md#On) object,used to locate Component relatively. |
| [within](arkts-test-on-within-f.md#within) | Requires that the target Component which is inside of another Component that specified by the given [On](arkts-test-uitest-on-c.md#On) object,used to locate Component relatively. |
| [inWindow](arkts-test-on-inwindow-f.md#inWindow) | Specifies the bundleName of the application which the window that the target Component is located belongs. |
| [belongingDisplay](arkts-test-on-belongingdisplay-f.md#belongingDisplay) | Specifies the displayId to which the target Component belongs. |
| [description](arkts-test-on-description-f.md#description) | Specifies the description for the target Component. |
| [id](arkts-test-on-id-f.md#id) | Specifies the id of the target Component. |
| [type](arkts-test-on-type-f.md#type) | Specifies the type of the target Component. |
| [hint](arkts-test-on-hint-f.md#hint) | Specifies the hint for the target Component. |
| [originalText](arkts-test-on-originaltext-f.md#originalText) | Specifies the original text for the target Component. If the accessibility property [accessibilityLevel](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#accessibilityLevel) of a component is set to 'no' or 'no-hide-descendants', you will not be able to use [text](arkts-test-uitest-on-c.md#text) to match the component with the specified original text, but you can use this method to achieve it; if the component does not set the above accessibility property, this method has no difference with [text](arkts-test-uitest-on-c.md#text) |
| [beforeComponent](arkts-test-on-beforecomponent-f.md#beforeComponent) | Requires that the target Component which is before another Component that specified by the given [Component](arkts-test-uitest-component-c.md#Component) object,used to locate Component relatively. |
| [afterComponent](arkts-test-on-aftercomponent-f.md#afterComponent) | Requires that the target Component which is after another Component that specified by the given [Component](arkts-test-uitest-component-c.md#Component) object,used to locate Component relatively. |
| [withinComponent](arkts-test-on-withincomponent-f.md#withinComponent) | Requires that the target Component which is inside of another Component that specified by the given [Component](arkts-test-uitest-component-c.md#Component) object,used to locate Component relatively. |

