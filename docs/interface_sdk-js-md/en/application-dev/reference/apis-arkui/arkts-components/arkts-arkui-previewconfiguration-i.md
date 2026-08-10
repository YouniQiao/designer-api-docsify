# PreviewConfiguration

配置自定义拖拽过程中的预览图样式。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-unnamed-declare interface PreviewConfiguration--><!--Device-unnamed-declare interface PreviewConfiguration-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delayCreating

```TypeScript
delayCreating?: boolean
```

组件预览builder是否在设置时加载。

默认值为false。true表示组件预览builder在设置时加载，false表示组件预览builder不在设置时加载。

**Type:** boolean

**Default:** false

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PreviewConfiguration-delayCreating?: boolean--><!--Device-PreviewConfiguration-delayCreating?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onlyForLifting

```TypeScript
onlyForLifting?: boolean
```

自定义配置的预览图是否仅用于浮起。

**说明：**

默认值为false。true表示自定义预览图仅用于浮起，false表示可用于浮起和拖拽。设置为true时，如果发起长按拖拽，浮起时的预览图为自定义配置的预览图，拖拽时的预览图不使用  
[dragPreview](arkts-arkui-commonmethod-c.md#dragpreview)属性，优先使用开发者在  
[onDragStart](arkts-arkui-commonmethod-c.md#ondragstart)中返回的预览图，如果[onDragStart](arkts-arkui-commonmethod-c.md#ondragstart)中没有返回预览图则使用组件自截图。

**Type:** boolean

**Default:** false

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PreviewConfiguration-onlyForLifting?: boolean--><!--Device-PreviewConfiguration-onlyForLifting?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

