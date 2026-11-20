# ImmersiveStrategy

```TypeScript
declare enum ImmersiveStrategy
```

安全区域的沉浸式策略枚举。

**起始版本：** 26.1.0

<!--Device-unnamed-declare enum ImmersiveStrategy--><!--Device-unnamed-declare enum ImmersiveStrategy-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## AVOID_CUTOUT

```TypeScript
AVOID_CUTOUT = 0
```

避让挖孔区域。

> **说明：** 
> 
> 该策略的优先级比module.json5中的avoid_cutout配置项低，
> 如果在module.json5的metadata中配置了avoid_cutout，
> 该配置项的效果会优先生效。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ImmersiveStrategy-AVOID_CUTOUT = 0--><!--Device-ImmersiveStrategy-AVOID_CUTOUT = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## AVOID_FLOAT_NAV

```TypeScript
AVOID_FLOAT_NAV = 1
```

避让三键导航栏区域。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ImmersiveStrategy-AVOID_FLOAT_NAV = 1--><!--Device-ImmersiveStrategy-AVOID_FLOAT_NAV = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## BIND_SHEET_EXPAND_SAFE_AREA

```TypeScript
BIND_SHEET_EXPAND_SAFE_AREA = 7
```

扩展bindSheet的标题区作为内容区的安全区。

> **NOTE:** 
> 
> 通过[applyDefaultImmersiveStrategy](arkts-arkui-arkui-uicontext-uicontext-c.md#applydefaultimmersivestrategy)应用此策略后，
> bindSheet的[titleBarHoverMode](../arkts-components/arkts-arkui-common-comp-sheetoptions-i.md#titlebarhovermode)默认为
> [SAFE_AREA_PADDING](../arkts-components/arkts-arkui-common-comp-sheettitlebarhovermode-e.md#safe_area_padding)。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ImmersiveStrategy-BIND_SHEET_EXPAND_SAFE_AREA = 7--><!--Device-ImmersiveStrategy-BIND_SHEET_EXPAND_SAFE_AREA = 7-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
