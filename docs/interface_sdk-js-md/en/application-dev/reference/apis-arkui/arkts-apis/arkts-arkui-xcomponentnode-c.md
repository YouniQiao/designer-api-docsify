# XComponentNode

定义XComponent Node。

**Inheritance/Implementation:** XComponentNode extends [FrameNode](arkts-arkui-framenode-c.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 12

**Substitutes:** ohos.arkui.node/typeNode#XComponent

<!--Device-unnamed-export declare class XComponentNode extends FrameNode--><!--Device-unnamed-export declare class XComponentNode extends FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeRenderType

```TypeScript
changeRenderType(type: NodeRenderType): boolean
```

设置builderNode的渲染类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 12

**Substitutes:** ohos.arkui.node/FrameNode#appendChild

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentNode-changeRenderType(type: NodeRenderType): boolean--><!--Device-XComponentNode-changeRenderType(type: NodeRenderType): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [NodeRenderType](arkts-arkui-buildernode-noderendertype-e.md) | Yes | 渲染类型 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回是否成功修改渲染类型。 |

## constructor

```TypeScript
constructor(uiContext: UIContext, options: RenderOptions,
    id: string, type: XComponentType, libraryName?: string)
```

构造函数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 12

**Substitutes:** ohos.arkui.node/typeNode#createNode

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentNode-constructor(uiContext: UIContext, options: RenderOptions,    id: string, type: XComponentType, libraryName?: string)--><!--Device-XComponentNode-constructor(uiContext: UIContext, options: RenderOptions,    id: string, type: XComponentType, libraryName?: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 用于创建FrameNode的UIContext |
| options | [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | Yes | Builder Node的渲染选项 |
| id | string | Yes | 应用定义的XComponent id |
| type | [XComponentType](arkts-arkui-enums-xcomponenttype-e.md) | Yes | XComponent类型 |
| libraryName | string | No | XComponent要加载的库名称 |

## onCreate

```TypeScript
onCreate(event?: Object): void
```

当XComponent的surface创建完成时回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 12

**Substitutes:** XComponent/XComponentAttribute#onLoad

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentNode-onCreate(event?: Object): void--><!--Device-XComponentNode-onCreate(event?: Object): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | Object | No | 加载库时来自native的事件 |

## onDestroy

```TypeScript
onDestroy(): void
```

当XComponent的surface被销毁时回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 12

**Substitutes:** XComponent/XComponentAttribute#onDestroy

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentNode-onDestroy(): void--><!--Device-XComponentNode-onDestroy(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

