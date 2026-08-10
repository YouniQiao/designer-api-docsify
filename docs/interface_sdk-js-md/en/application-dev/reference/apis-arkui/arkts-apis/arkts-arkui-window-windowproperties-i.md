# WindowProperties

窗口属性。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-window-interface WindowProperties--><!--Device-window-interface WindowProperties-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## brightness

```TypeScript
brightness: double
```

窗口亮度。通过  
[setWindowBrightness()](arkts-arkui-window-window-i.md#setwindowbrightness)设置窗口的亮度值。该参数为浮点数，可设置的亮度范围为[0.0, 1.0]或-1.0，其取值1.0时表示最大亮度，取值-1.0时，表示亮度跟随系统。如果窗口没有设置亮度值，表示亮度跟随系统，此时获取到的亮度值为-1.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowProperties-brightness: double--><!--Device-WindowProperties-brightness: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## dimBehindValue

```TypeScript
dimBehindValue: number
```

下层窗口的暗度值。该参数为浮点数，取值范围为[0.0, 1.0]，其取1.0表示最暗。

**说明：** 从API version 7开始支持，从API version 9开始废弃，当前无可替代接口。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-WindowProperties-dimBehindValue: number--><!--Device-WindowProperties-dimBehindValue: number-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## displayId

```TypeScript
displayId?: long
```

窗口所在屏幕ID，默认返回主屏幕ID，该参数为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-displayId?: long--><!--Device-WindowProperties-displayId?: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## drawableRect

```TypeScript
drawableRect: Rect
```

窗口内的可绘制区域尺寸，其中左边界上边界是相对于窗口左上顶点计算。在Stage模型下，需要在调用  
[loadContent()](arkts-arkui-window-window-i.md#loadcontent)或[setUIContent()](arkts-arkui-window-window-i.md#setuicontent)加载页面内容后获取该属性。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-drawableRect: Rect--><!--Device-WindowProperties-drawableRect: Rect-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## focusable

```TypeScript
focusable: boolean
```

窗口是否可获焦。true表示可获焦；false表示不可获焦。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-focusable: boolean--><!--Device-WindowProperties-focusable: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## globalDisplayRect

```TypeScript
globalDisplayRect?: Rect
```

全局坐标系下的窗口尺寸。扩展屏场景下以主屏左上角为坐标原点，虚拟屏场景下以虚拟屏左上角为坐标原点。默认值：[0, 0, 0, 0]。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WindowProperties-globalDisplayRect?: Rect--><!--Device-WindowProperties-globalDisplayRect?: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## id

```TypeScript
id: int
```

窗口ID，该参数为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-id: int--><!--Device-WindowProperties-id: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## isFullScreen

```TypeScript
isFullScreen: boolean
```

在满足isLayoutFullScreen为true的条件下如果隐藏了状态栏，返回值为true，其他情况下均返回false。

**Type:** boolean

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-isFullScreen: boolean--><!--Device-WindowProperties-isFullScreen: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## isKeepScreenOn

```TypeScript
isKeepScreenOn: boolean
```

屏幕是否常亮。true表示常亮；false表示不常亮。

**Type:** boolean

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowProperties-isKeepScreenOn: boolean--><!--Device-WindowProperties-isKeepScreenOn: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## isLayoutFullScreen

```TypeScript
isLayoutFullScreen: boolean
```

对于子窗，如果设置了[沉浸式布局](../../../windowmanager/window-terminology.md#沉浸式布局)，返回值为true。

对于主窗，如果设置了[沉浸式布局](../../../windowmanager/window-terminology.md#沉浸式布局)且处于全屏模式，返回值为true。

其他情况下均返回false

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-isLayoutFullScreen: boolean--><!--Device-WindowProperties-isLayoutFullScreen: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## isPrivacyMode

```TypeScript
isPrivacyMode: boolean
```

窗口是否为隐私模式。true表示窗口为隐私模式；false表示窗口为非隐私模式。可通过  
[setWindowPrivacyMode()](arkts-arkui-window-window-i.md#setwindowprivacymode)设置窗口的隐私模式。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-isPrivacyMode: boolean--><!--Device-WindowProperties-isPrivacyMode: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## isRoundCorner

```TypeScript
isRoundCorner: boolean
```

窗口是否为圆角。true表示窗口为圆角；false表示窗口为非圆角。

**说明：** 从API version 7开始支持，从API version 9开始废弃，当前无可替代接口。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-WindowProperties-isRoundCorner: boolean--><!--Device-WindowProperties-isRoundCorner: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## isTransparent

```TypeScript
isTransparent: boolean
```

窗口背景是否透明。true表示透明；false表示不透明。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-isTransparent: boolean--><!--Device-WindowProperties-isTransparent: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## name

```TypeScript
name?: string
```

窗口名称，默认为空字符串。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-WindowProperties-name?: string--><!--Device-WindowProperties-name?: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## touchable

```TypeScript
touchable: boolean
```

窗口是否可触摸。true表示可触摸；false表示不可触摸。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-touchable: boolean--><!--Device-WindowProperties-touchable: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## type

```TypeScript
type: WindowType
```

窗口类型。

当前存在主窗使用[getWindowProperties()](arkts-arkui-window-window-i.md#getwindowproperties)接口返回type不准确的问题，开发者在创建窗口时已指明窗口类型，无需通过getWindowProperties()接口获取窗口类型。

**Type:** [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 26.0.0

**Substitutes:** [WindowProperties#windowType](arkts-arkui-window-windowproperties-i.md#windowtype)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowProperties-type: WindowType--><!--Device-WindowProperties-type: WindowType-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## windowRect

```TypeScript
windowRect: Rect
```

窗口尺寸，其中左边界上边界是相对于窗口所在屏幕左上顶点计算，可在页面生命周期  
[onPageShow](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#onpageshow)或应用生命周期  
[onForeground](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md/arkts-ability-app-ability-uiability-uiability-c.md#onforeground)阶段获取。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowProperties-windowRect: Rect--><!--Device-WindowProperties-windowRect: Rect-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## windowType

```TypeScript
windowType?: WindowType
```

含义：窗口类型使用场景：判断当前窗口主窗口还是子窗口等

**Type:** [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WindowProperties-windowType?: WindowType--><!--Device-WindowProperties-windowType?: WindowType-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

