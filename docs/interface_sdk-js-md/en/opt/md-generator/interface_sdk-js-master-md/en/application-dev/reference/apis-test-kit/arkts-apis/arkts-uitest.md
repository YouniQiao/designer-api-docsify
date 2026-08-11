# @ohos.UiTest

The **UiTest** module provides UI automation test capabilities, such as component search and operation, coordinate
 clicking/sliding, key injections, screenshot, window management, multi-finger operations, and mouse/stylus/touchpad
 operations.
 This module provides the following functions:
 - [On<sup>9+</sup>](arkts-test-uitest-on-c.md): provides UI component feature description APIs for component filtering and matching.
 - [Component<sup>9+</sup>](arkts-test-uitest-component-c.md): represents a component on the UI and provides APIs for obtaining
 component attributes, clicking a component, scrolling to search for a component, and text injection.
 - [Driver<sup>9+</sup>](arkts-test-uitest-driver-c.md): works as the entry class and provides APIs for features such as component
 matching/search, key injection, coordinate clicking/sliding, and screenshot.
 - [UiWindow<sup>9+</sup>](arkts-test-uitest-uiwindow-c.md): represents a window object on the UI and provides APIs for obtaining window attributes,
 dragging windows, and adjusting window sizes.
 - [By<sup>(deprecated)</sup>](arkts-test-uitest-by-c.md): provides UI component feature description APIs for component filtering and
 matching. This API is supported since API version 8 and deprecated since API version 9.
 You are advised to use {@link On} instead.
 - [UiComponent<sup>(deprecated)</sup>](arkts-test-uitest-uicomponent-c.md): represents a component on the UI and provides APIs for
 obtaining component attributes, clicking a component, scrolling to search for a component, and text injection.
 This API is supported since API version 8 and deprecated since API version 9.
 You are advised to use [Component<sup>9+</sup>](arkts-test-uitest-component-c.md) instead.
 - [UiDriver<sup>(deprecated)</sup>](arkts-test-uitest-uidriver-c.md): works as the entry class and provides APIs for features such as
 component matching/search, key injection, coordinate clicking/sliding, and screenshot.
 This API is supported since API version 8 and deprecated since API version 9.
 You are advised to use [Driver<sup>9+</sup>](arkts-test-uitest-driver-c.md) instead.
 > **NOTE**
 >
 > - The APIs of this module can be used only in <!--RP1-->[UITest](../../../application-test/uitest-guidelines.md)<!--RP1End-->.
 >
 > - The APIs of this module do not support concurrent calls.


## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |
| [Component](arkts-test-uitest-component-c.md) |
| [Driver](arkts-test-uitest-driver-c.md) |
| [On](arkts-test-uitest-on-c.md) |
| [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) |
| [UiComponent](arkts-test-uitest-uicomponent-c.md) |
| [UiDriver](arkts-test-uitest-uidriver-c.md) |
| [UiWindow](arkts-test-uitest-uiwindow-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) |
| [InputTextMode](arkts-test-uitest-inputtextmode-i.md) |
| [KeyOptions](arkts-test-uitest-keyoptions-i.md) |
| [PenKeyOperationOptions](arkts-test-uitest-penkeyoperationoptions-i.md) |
| [Point](arkts-test-uitest-point-i.md) |
| [Rect](arkts-test-uitest-rect-i.md) |
| [TouchOptions](arkts-test-uitest-touchoptions-i.md) |
| [TouchPadSwipeOptions](arkts-test-uitest-touchpadswipeoptions-i.md) |
| [UIElementInfo](arkts-test-uitest-uielementinfo-i.md) |
| [UIEventObserver](arkts-test-uitest-uieventobserver-i.md) |
| [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) |
| [WindowFilter](arkts-test-uitest-windowfilter-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) |
| [DisplayRotation](arkts-test-uitest-displayrotation-e.md) |
| [MatchPattern](arkts-test-uitest-matchpattern-e.md) |
| [MouseButton](arkts-test-uitest-mousebutton-e.md) |
| [PenKey](arkts-test-uitest-penkey-e.md) |
| [PenKeyOperation](arkts-test-uitest-penkeyoperation-e.md) |
| [PenMode](arkts-test-uitest-penmode-e.md) |
| [ResizeDirection](arkts-test-uitest-resizedirection-e.md) |
| [UiDirection](arkts-test-uitest-uidirection-e.md) |
| [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) |
| [WindowMode](arkts-test-uitest-windowmode-e.md) |
