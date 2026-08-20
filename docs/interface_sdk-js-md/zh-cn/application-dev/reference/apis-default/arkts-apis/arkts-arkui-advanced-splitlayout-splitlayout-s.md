# SplitLayout

声明SplitLayout。SplitLayout用于上下图文布局。 @struct { SplitLayout }

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare struct SplitLayout--><!--Device-unnamed-export declare struct SplitLayout-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
    build(): void
```

构造组件的方法。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SplitLayout-@Builder    build(): void--><!--Device-SplitLayout-@Builder    build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## container

```TypeScript
@BuilderParam
    container: () => void
```

容器内组件。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SplitLayout-@BuilderParam    container: () => void--><!--Device-SplitLayout-@BuilderParam    container: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## mainImage

```TypeScript
@State
    mainImage: ResourceStr
```

传入图片。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SplitLayout-@State    mainImage: ResourceStr--><!--Device-SplitLayout-@State    mainImage: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryText

```TypeScript
@PropRef
    primaryText: ResourceStr
```

标题内容。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SplitLayout-@PropRef    primaryText: ResourceStr--><!--Device-SplitLayout-@PropRef    primaryText: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryText

```TypeScript
@PropRef
    secondaryText?: ResourceStr
```

副标题内容。当需要在标题下方显示副标题时传入，不传入时取默认值，不显示副标题。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SplitLayout-@PropRef    secondaryText?: ResourceStr--><!--Device-SplitLayout-@PropRef    secondaryText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## tertiaryText

```TypeScript
@PropRef
    tertiaryText?: ResourceStr
```

辅助文本。当需要显示辅助文本时传入，不传入时取默认值，不显示辅助文本。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SplitLayout-@PropRef    tertiaryText?: ResourceStr--><!--Device-SplitLayout-@PropRef    tertiaryText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

