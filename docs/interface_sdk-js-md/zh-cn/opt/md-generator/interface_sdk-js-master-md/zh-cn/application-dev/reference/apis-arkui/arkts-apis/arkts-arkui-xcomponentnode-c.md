# XComponentNode

定义XComponent Node。

**继承/实现关系：** XComponentNode extends [FrameNode](FrameNode)

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [XComponent](ohos.arkui.node/typeNode#XComponent)

<!--Device-unnamed-export declare class XComponentNode extends FrameNode--><!--Device-unnamed-export declare class XComponentNode extends FrameNode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## changeRenderType

```TypeScript
changeRenderType(type: NodeRenderType): boolean
```

设置builderNode的渲染类型。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [appendChild](ohos.arkui.node/FrameNode#appendChild)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XComponentNode-changeRenderType(type: NodeRenderType): boolean--><!--Device-XComponentNode-changeRenderType(type: NodeRenderType): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [NodeRenderType](arkts-arkui-buildernode-noderendertype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## constructor

```TypeScript
constructor(uiContext: UIContext, options: RenderOptions,
    id: string, type: XComponentType, libraryName?: string)
```

构造函数。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [createNode](ohos.arkui.node/typeNode#createNode)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XComponentNode-constructor(uiContext: UIContext, options: RenderOptions,    id: string, type: XComponentType, libraryName?: string)--><!--Device-XComponentNode-constructor(uiContext: UIContext, options: RenderOptions,    id: string, type: XComponentType, libraryName?: string)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| options | [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | 是 |
| id | string | 是 |
| type | [XComponentType](arkts-arkui-xcomponenttype-e.md) | 是 |
| libraryName | string | 否 |

## onCreate

```TypeScript
onCreate(event?: Object): void
```

当XComponent的surface创建完成时回调。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [onLoad](XComponent/XComponentAttribute#onLoad)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XComponentNode-onCreate(event?: Object): void--><!--Device-XComponentNode-onCreate(event?: Object): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | Object | 否 |

## onDestroy

```TypeScript
onDestroy(): void
```

当XComponent的surface被销毁时回调。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [onDestroy](XComponent/XComponentAttribute#onDestroy)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XComponentNode-onDestroy(): void--><!--Device-XComponentNode-onDestroy(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
