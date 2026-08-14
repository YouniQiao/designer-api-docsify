# FloatViewProperties

Provides the properties of the float view.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-floatView-interface FloatViewProperties--><!--Device-floatView-interface FloatViewProperties-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatView } from 'floatView';
```

## avoidArea

```TypeScript
avoidArea: window.AvoidArea
```

Avoid area for the content of the float view. Note: On the page loaded by [setUIContext](arkts-arkui-floatview-floatviewcontroller-i.md#setUIContext), components in the avoid area do not respond to gesture events. When adding components that require gesture response events, avoid the area.

**Type:** window.AvoidArea

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-avoidArea: window.AvoidArea--><!--Device-FloatViewProperties-avoidArea: window.AvoidArea-End-->

**System capability:** SystemCapability.Window.SessionManager

## displayId

```TypeScript
displayId: int
```

ID of the display where the float view is located.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-displayId: int--><!--Device-FloatViewProperties-displayId: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## inSidebar

```TypeScript
inSidebar: boolean
```

Whether the float view is in the sidebar. **true**: in the sidebar; **false**: not in the sidebar.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-inSidebar: boolean--><!--Device-FloatViewProperties-inSidebar: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## templateType

```TypeScript
templateType: FloatViewTemplateType
```

Template type of the float view.

**Type:** [FloatViewTemplateType](arkts-arkui-floatview-floatviewtemplatetype-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-templateType: FloatViewTemplateType--><!--Device-FloatViewProperties-templateType: FloatViewTemplateType-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowId

```TypeScript
windowId: int
```

Float view ID.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-windowId: int--><!--Device-FloatViewProperties-windowId: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowRect

```TypeScript
windowRect: window.Rect
```

Rectangle area of the float view.

**Type:** window.Rect

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-windowRect: window.Rect--><!--Device-FloatViewProperties-windowRect: window.Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowScale

```TypeScript
windowScale: double
```

Scale factor of the float view.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-windowScale: double--><!--Device-FloatViewProperties-windowScale: double-End-->

**System capability:** SystemCapability.Window.SessionManager

