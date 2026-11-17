# VersionCondition

```TypeScript
declare interface VersionCondition
```

定义VersionCondition接口。

**起始版本：** 26.1.0

<!--Device-unnamed-declare interface VersionCondition--><!--Device-unnamed-declare interface VersionCondition-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## maxApiVersion

```TypeScript
maxApiVersion?: number | string
```

样式或扩展生效的最大API版本。表示运行时的设备版本，取值为数字或字符串。默认值：undefined，此时版本限制不生效。

**类型：** number &#124; string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-VersionCondition-maxApiVersion?: number | string--><!--Device-VersionCondition-maxApiVersion?: number | string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## minApiVersion

```TypeScript
minApiVersion?: number | string
```

样式或扩展生效的最小API版本。表示运行时的设备版本，取值为数字或字符串。默认值：undefined，此时版本限制不生效。

**类型：** number &#124; string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-VersionCondition-minApiVersion?: number | string--><!--Device-VersionCondition-minApiVersion?: number | string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
