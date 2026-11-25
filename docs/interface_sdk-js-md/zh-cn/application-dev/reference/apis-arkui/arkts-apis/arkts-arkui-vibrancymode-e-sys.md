# VibrancyMode（系统接口）

```TypeScript
declare enum VibrancyMode
```

定义提亮压暗模式，指定是否对内容使用提亮或压暗效果，以提升通透材质背景下的可读性。

**起始版本：** 26.1.0

<!--Device-unnamed-declare enum VibrancyMode--><!--Device-unnamed-declare enum VibrancyMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## AUTO

```TypeScript
AUTO = 1
```

自动模式。当自身或祖先组件的系统材质能够自动反色时，跟随材质的反色结果（材质取色为深色时提亮，为浅色时压暗）；否则跟随控件的深浅色模式（深色模式时提亮，浅色模式时压暗）。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VibrancyMode-AUTO = 1--><!--Device-VibrancyMode-AUTO = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## BRIGHTEN

```TypeScript
BRIGHTEN = 2
```

提亮模式。始终对内容提亮，以提升深色背景下的可读性。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VibrancyMode-BRIGHTEN = 2--><!--Device-VibrancyMode-BRIGHTEN = 2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## DARKEN

```TypeScript
DARKEN = 3
```

压暗模式。始终对内容压暗，以提升浅色背景下的可读性。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VibrancyMode-DARKEN = 3--><!--Device-VibrancyMode-DARKEN = 3-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## DISABLED

```TypeScript
DISABLED = 0
```

不启用提亮压暗，内容无提亮压暗效果。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VibrancyMode-DISABLED = 0--><!--Device-VibrancyMode-DISABLED = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
