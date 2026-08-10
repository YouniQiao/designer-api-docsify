# ActionMenuOptions

操作菜单的选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-promptAction-export interface ActionMenuOptions--><!--Device-promptAction-export interface ActionMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## buttons

```TypeScript
buttons: PromptActionSingleButton | PromptActionDoubleButtons | PromptActionTripleButtons |
            PromptActionQuadrupleButtons | PromptActionQuintupleButtons | PromptActionSextupleButtons
```

菜单中菜单项按钮的数组，结构为： {text:'button', color: '#666666'}.支持1-6个按钮。按钮数量大于6个时，仅显示前6个按钮，之后的按钮不显示。

**Type:** [PromptActionSingleButton](arkts-arkui-promptaction-promptactionsinglebutton-t.md) \| PromptActionDoubleButtons \| PromptActionTripleButtons \| PromptActionQuadrupleButtons \| PromptActionQuintupleButtons \| PromptActionSextupleButtons

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-buttons: PromptActionSingleButton | PromptActionDoubleButtons | PromptActionTripleButtons |            PromptActionQuadrupleButtons | PromptActionQuintupleButtons | PromptActionSextupleButtons--><!--Device-ActionMenuOptions-buttons: PromptActionSingleButton | PromptActionDoubleButtons | PromptActionTripleButtons |            PromptActionQuadrupleButtons | PromptActionQuintupleButtons | PromptActionSextupleButtons-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

设置页面内菜单蒙层效果。&lt;br /&gt;**说明：**&lt;br /&gt;- 默认值：ImmersiveMode.DEFAULT &lt;br /&gt;- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**Type:** [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-immersiveMode?: ImmersiveMode--><!--Device-ActionMenuOptions-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

菜单是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与菜单周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与菜单周围其他控件进行交互。&lt;br/&gt;默认值：true

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-isModal?: boolean--><!--Device-ActionMenuOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

设置菜单显示层级。&lt;br /&gt;**说明：**&lt;br /&gt;- 默认值：LevelMode.OVERLAY &lt;br /&gt;- 当且仅当showInSubWindow属性设置为false时生效。

**Type:** [LevelMode](arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-levelMode?: LevelMode--><!--Device-ActionMenuOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: int
```

设置页面级菜单需要显示的层级下的节点UniqueID，该ID可以通过[getUniqueId](arkts-arkui-framenode-c.md#getuniqueid)获取。取值范围：大于等于0的数字。&lt;br /&gt;**说明：**&lt;br/&gt;- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-levelUniqueId?: int--><!--Device-ActionMenuOptions-levelUniqueId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

菜单弹出后的事件回调。&lt;br /&gt;**说明：**&lt;br /&gt;1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。&lt;br /&gt;2.快速点击弹出，关闭菜单时，onWillDisappear在onDidAppear前生效。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-onDidAppear?: VoidCallback--><!--Device-ActionMenuOptions-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

菜单消失后的事件回调。&lt;br /&gt;**说明：**&lt;br /&gt;1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-onDidDisappear?: VoidCallback--><!--Device-ActionMenuOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

菜单显示动效前的事件回调。&lt;br /&gt;**说明：**&lt;br /&gt;1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-onWillAppear?: VoidCallback--><!--Device-ActionMenuOptions-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

菜单退出动效前的事件回调。&lt;br /&gt;**说明：**&lt;br /&gt;1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-onWillDisappear?: VoidCallback--><!--Device-ActionMenuOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

某操作菜单需要显示在主窗口之外时，是否在子窗口显示此菜单。值为true表示在子窗口显示菜单。

默认值：false，在子窗口不显示菜单。

**说明：** - showInSubWindow为true的菜单无法触发显示另一个showInSubWindow为true的菜单。
- 若在UIExtension中设置showInSubWindow为true, 菜单将基于UIExtension的宿主窗口对齐。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-showInSubWindow?: boolean--><!--Device-ActionMenuOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: uiMaterial.Material
```

设置弹窗的系统材质。&lt;br/&gt;默认值：ImmersiveOptions的style为ImmersiveStyle.ULTRA_THICK的ImmersiveMaterial对象。设置undefined时与默认值保持一致。不同的材质具有不同的效果，可以影响弹窗的背景色、边框、阴影等视觉属性。

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-systemMaterial?: uiMaterial.Material--><!--Device-ActionMenuOptions-systemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string | Resource
```

标题文本。&lt;br/&gt;默认值：undefined，取值为undefined默认不显示标题。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-title?: string | Resource--><!--Device-ActionMenuOptions-title?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

