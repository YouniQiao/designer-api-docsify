# SubWindowAttachOptions (System API)

子窗与主窗保持相对位置不变时的参数。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-window-interface SubWindowAttachOptions--><!--Device-window-interface SubWindowAttachOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## currentLayoutMode

```TypeScript
currentLayoutMode?: string
```

子窗当前布局模式，用于控制应用定制的UI效果。若不传，则默认为空字符串。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubWindowAttachOptions-currentLayoutMode?: string--><!--Device-SubWindowAttachOptions-currentLayoutMode?: string-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## isIntersectedHeightLimit

```TypeScript
isIntersectedHeightLimit?: boolean
```

是否使用处于协同关系中两个窗口的高度限制的交集。

**Type:** boolean

**Default:** false

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubWindowAttachOptions-isIntersectedHeightLimit?: boolean--><!--Device-SubWindowAttachOptions-isIntersectedHeightLimit?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## isIntersectedWidthLimit

```TypeScript
isIntersectedWidthLimit?: boolean
```

是否使用处于协同关系中两个窗口的宽度限制的交集。

**Type:** boolean

**Default:** false

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubWindowAttachOptions-isIntersectedWidthLimit?: boolean--><!--Device-SubWindowAttachOptions-isIntersectedWidthLimit?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## parentWindowSizeChangeCallback

```TypeScript
parentWindowSizeChangeCallback?: Callback<Size>
```

父窗大小变化的回调。绑定后立即回调一次，后续父窗大小变化时通知。默认不传，无法收到父窗大小变化通知。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Size&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubWindowAttachOptions-parentWindowSizeChangeCallback?: Callback<Size>--><!--Device-SubWindowAttachOptions-parentWindowSizeChangeCallback?: Callback<Size>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## parentWindowStatusChangeCallback

```TypeScript
parentWindowStatusChangeCallback?: Callback<WindowStatusType>
```

父窗模式变化的回调。绑定后立即回调一次，后续父窗模式变化时通知。默认不传，无法收到父窗模式变化通知。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;WindowStatusType&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubWindowAttachOptions-parentWindowStatusChangeCallback?: Callback<WindowStatusType>--><!--Device-SubWindowAttachOptions-parentWindowStatusChangeCallback?: Callback<WindowStatusType>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

