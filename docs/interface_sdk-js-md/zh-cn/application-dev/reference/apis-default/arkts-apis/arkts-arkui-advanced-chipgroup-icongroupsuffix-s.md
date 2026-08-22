# IconGroupSuffix

Defines IconGroupSuffix.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare struct IconGroupSuffix--><!--Device-unnamed-export declare struct IconGroupSuffix-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

build函数用于构造ChipGroup高级组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IconGroupSuffix-@Builder  build(): void--><!--Device-IconGroupSuffix-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconBackgroundSystemMaterial

```TypeScript
@PropRef
  iconBackgroundSystemMaterial?: uiMaterial.Material
```

设置IconGroup后缀背景系统材质。

**类型：** uiMaterial.Material

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IconGroupSuffix-@PropRef  iconBackgroundSystemMaterial?: uiMaterial.Material--><!--Device-IconGroupSuffix-@PropRef  iconBackgroundSystemMaterial?: uiMaterial.Material-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @PropRef
  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>
```

尾部区域显示的自定义项数组，支持IconItemOptions（Image图标）、SymbolGlyphModifier（Symbol图标）或SymbolItemOptions（Symbol图标配置）类型。

**类型：** Array&lt;[IconItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipgroup-iconitemoptions-i.md) \| SymbolGlyphModifier \| [SymbolItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipgroup-symbolitemoptions-i.md)&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IconGroupSuffix-@Require  @PropRef  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>--><!--Device-IconGroupSuffix-@Require  @PropRef  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

