# SelectionMenuOptions

菜单的选项。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface SelectionMenuOptions--><!--Device-unnamed-declare interface SelectionMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAppear

```TypeScript
onAppear?: MenuOnAppearCallback
```

自定义选择菜单弹出时回调。若需在菜单弹出时执行自定义逻辑（如记录用户操作、动态调整菜单内容），可传入此参数；不传入则无额外回调触发。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SelectionMenuOptions-onAppear?: MenuOnAppearCallback--><!--Device-SelectionMenuOptions-onAppear?: MenuOnAppearCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMenuHide

```TypeScript
onMenuHide?: MenuCallback
```

自定义选择菜单隐藏时回调。若需在菜单隐藏时执行自定义逻辑，可传入此参数；不传入则无回调触发。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SelectionMenuOptions-onMenuHide?: MenuCallback--><!--Device-SelectionMenuOptions-onMenuHide?: MenuCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMenuShow

```TypeScript
onMenuShow?: MenuCallback
```

自定义选择菜单显示时回调。若需在菜单显示时执行自定义逻辑，可传入此参数；不传入则无回调触发。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SelectionMenuOptions-onMenuShow?: MenuCallback--><!--Device-SelectionMenuOptions-onMenuShow?: MenuCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## menuType

```TypeScript
menuType?: MenuType
```

自定义选择菜单类型。

默认值：MenuType.SELECTION_MENU。

**Type:** [MenuType](../arkts-apis/arkts-arkui-menutype-e.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-SelectionMenuOptions-menuType?: MenuType--><!--Device-SelectionMenuOptions-menuType?: MenuType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDisappear

```TypeScript
onDisappear?: Callback<void>
```

自定义选择菜单关闭时回调。若需在菜单关闭时执行自定义逻辑（如恢复界面状态、清理临时数据），可传入此参数；不传入则无额外回调触发。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SelectionMenuOptions-onDisappear?: Callback<void>--><!--Device-SelectionMenuOptions-onDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## previewMenuOptions

```TypeScript
previewMenuOptions?: PreviewMenuOptions
```

预览菜单的选项。该参数只在RichEditor中生效。

从API版本26.0.0开始，该参数在Text组件中也生效。

不传入时，预览菜单使用默认配置。

**Type:** [PreviewMenuOptions](arkts-arkui-previewmenuoptions-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectionMenuOptions-previewMenuOptions?: PreviewMenuOptions--><!--Device-SelectionMenuOptions-previewMenuOptions?: PreviewMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

