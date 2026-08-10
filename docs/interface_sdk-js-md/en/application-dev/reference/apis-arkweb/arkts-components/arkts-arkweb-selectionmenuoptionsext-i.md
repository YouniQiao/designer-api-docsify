# SelectionMenuOptionsExt

自定义菜单扩展项。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-unnamed-declare interface SelectionMenuOptionsExt--><!--Device-unnamed-declare interface SelectionMenuOptionsExt-End-->

**System capability:** SystemCapability.Web.Webview.Core

## menuType

```TypeScript
menuType?: MenuType
```

自定义选择菜单类型。

默认值：`MenuType.SELECTION_MENU`。

从API version 20起，`MenuType.PREVIEW_MENU`支持超链接预览。

**Type:** [MenuType](../../apis-arkui/arkts-apis/arkts-arkui-menutype-e.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-SelectionMenuOptionsExt-menuType?: MenuType--><!--Device-SelectionMenuOptionsExt-menuType?: MenuType-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onAppear

```TypeScript
onAppear?: Callback<void>
```

自定义选择菜单弹出时回调。

**Type:** [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;void&gt;

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-SelectionMenuOptionsExt-onAppear?: Callback<void>--><!--Device-SelectionMenuOptionsExt-onAppear?: Callback<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onDisappear

```TypeScript
onDisappear?: Callback<void>
```

自定义选择菜单关闭时回调。

**Type:** [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;void&gt;

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-SelectionMenuOptionsExt-onDisappear?: Callback<void>--><!--Device-SelectionMenuOptionsExt-onDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onMenuHide

```TypeScript
onMenuHide?: Callback<void>
```

自定义选择菜单隐藏时回调。

**Type:** [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;void&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-SelectionMenuOptionsExt-onMenuHide?: Callback<void>--><!--Device-SelectionMenuOptionsExt-onMenuHide?: Callback<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onMenuShow

```TypeScript
onMenuShow?: Callback<void>
```

自定义选择菜单显示时回调。

**Type:** [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;void&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-SelectionMenuOptionsExt-onMenuShow?: Callback<void>--><!--Device-SelectionMenuOptionsExt-onMenuShow?: Callback<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## preview

```TypeScript
preview?: CustomBuilder
```

自定义选择菜单的预览内容样式，未配置时无预览内容。

**Type:** [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-SelectionMenuOptionsExt-preview?: CustomBuilder--><!--Device-SelectionMenuOptionsExt-preview?: CustomBuilder-End-->

**System capability:** SystemCapability.Web.Webview.Core

## previewMenuOptions

```TypeScript
previewMenuOptions?: PreviewMenuOptions
```

自定义选择预览菜单选项。

**Type:** [PreviewMenuOptions](../../apis-arkui/arkts-components/arkts-arkui-previewmenuoptions-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-SelectionMenuOptionsExt-previewMenuOptions?: PreviewMenuOptions--><!--Device-SelectionMenuOptionsExt-previewMenuOptions?: PreviewMenuOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

