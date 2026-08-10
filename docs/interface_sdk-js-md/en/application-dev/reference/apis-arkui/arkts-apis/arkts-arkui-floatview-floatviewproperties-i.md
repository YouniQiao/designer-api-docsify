# FloatViewProperties

标准悬浮窗窗口的属性。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-floatView-interface FloatViewProperties--><!--Device-floatView-interface FloatViewProperties-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## avoidArea

```TypeScript
avoidArea: window.AvoidArea
```

标准悬浮窗内容的避让区域。

**注意：**

通过[setUIContext()](arkts-arkui-floatview-floatviewcontroller-i.md#setuicontext)或  
[setUIContextByName()](arkts-arkui-floatview-floatviewcontroller-i.md#setuicontextbyname)加载的页面中，位于避让区域的组件将不响应手势事件，添加需要手势响应事件的组件时，请注意避让这些区域。

**Type:** window.AvoidArea

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-avoidArea: window.AvoidArea--><!--Device-FloatViewProperties-avoidArea: window.AvoidArea-End-->

**System capability:** SystemCapability.Window.SessionManager

## displayId

```TypeScript
displayId: int
```

标准悬浮窗所在屏幕ID。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-displayId: int--><!--Device-FloatViewProperties-displayId: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## inSidebar

```TypeScript
inSidebar: boolean
```

标准悬浮窗是否在侧边栏中。true为在侧边栏中，false为不在侧边栏中。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-inSidebar: boolean--><!--Device-FloatViewProperties-inSidebar: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## templateType

```TypeScript
templateType: FloatViewTemplateType
```

标准悬浮窗的模板类型。

**Type:** [FloatViewTemplateType](arkts-arkui-floatview-floatviewtemplatetype-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-templateType: FloatViewTemplateType--><!--Device-FloatViewProperties-templateType: FloatViewTemplateType-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowId

```TypeScript
windowId: int
```

标准悬浮窗窗口ID。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-windowId: int--><!--Device-FloatViewProperties-windowId: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowRect

```TypeScript
windowRect: window.Rect
```

标准悬浮窗窗口矩形区域。

**Type:** window.Rect

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-windowRect: window.Rect--><!--Device-FloatViewProperties-windowRect: window.Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowScale

```TypeScript
windowScale: double
```

标准悬浮窗窗口缩放比例。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewProperties-windowScale: double--><!--Device-FloatViewProperties-windowScale: double-End-->

**System capability:** SystemCapability.Window.SessionManager

