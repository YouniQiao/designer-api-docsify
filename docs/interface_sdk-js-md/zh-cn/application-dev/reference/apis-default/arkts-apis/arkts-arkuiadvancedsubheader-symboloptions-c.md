# SymbolOptions

Declare type SymbolOptions

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class SymbolOptions--><!--Device-unnamed-export declare class SymbolOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## effectStrategy

```TypeScript
public effectStrategy?: SymbolEffectStrategy
```

设置SymbolGlyph动效策略。

默认值：SymbolEffectStrategy.NONE

**说明：**

\$r('sys.symbol.ohos_*')中引用的资源仅ohos_wifi支持层级动效模式。

**类型：** [SymbolEffectStrategy](../../apis-arkui/arkts-components/arkts-arkui-symbolglyph-symboleffectstrategy-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SymbolOptions-public effectStrategy?: SymbolEffectStrategy--><!--Device-SymbolOptions-public effectStrategy?: SymbolEffectStrategy-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
public fontColor?: Array<ResourceColor>
```

设置SymbolGlyph颜色。

默认值：不同渲染策略下默认值不同。

**类型：** Array&lt;[ResourceColor](arkts-resourcecolor-t.md)&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SymbolOptions-public fontColor?: Array<ResourceColor>--><!--Device-SymbolOptions-public fontColor?: Array<ResourceColor>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
public fontSize?: double | string | Resource
```

设置SymbolGlyph大小。

number类型取值范围：大于等于0。

设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如："10"，"10fp"。

默认值：系统默认值。

**类型：** double \| string \| [Resource](arkts-resource-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SymbolOptions-public fontSize?: double | string | Resource--><!--Device-SymbolOptions-public fontSize?: double | string | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
public fontWeight?: int | FontWeight | string
```

设置SymbolGlyph粗细。

number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。

string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。

默认值：FontWeight.Normal

**类型：** int \| [FontWeight](arkts-enums-fontweight-e.md) \| string

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SymbolOptions-public fontWeight?: int | FontWeight | string--><!--Device-SymbolOptions-public fontWeight?: int | FontWeight | string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## renderingStrategy

```TypeScript
public renderingStrategy?: SymbolRenderingStrategy
```

设置SymbolGlyph渲染策略。

默认值：SymbolRenderingStrategy.SINGLE

**说明：**

\$r('sys.symbol.ohos_*')中引用的资源仅ohos_trash_circle、ohos_folder_badge_plus、ohos_lungs支持分层与多色模式。

**类型：** [SymbolRenderingStrategy](../../apis-arkui/arkts-components/arkts-arkui-symbolglyph-symbolrenderingstrategy-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SymbolOptions-public renderingStrategy?: SymbolRenderingStrategy--><!--Device-SymbolOptions-public renderingStrategy?: SymbolRenderingStrategy-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

