# TabBarOptions

设置页签内的图片和文字内容。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TabBarOptions--><!--Device-unnamed-export declare interface TabBarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## badge

```TypeScript
badge?: BadgeParamWithNumber | BadgeParamWithString
```

TabBar 信息标记组件。

**Type:** [BadgeParamWithNumber](arkts-arkui-badge-badgeparamwithnumber-i.md) \| BadgeParamWithString

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarOptions-badge?: BadgeParamWithNumber | BadgeParamWithString--><!--Device-TabBarOptions-badge?: BadgeParamWithNumber | BadgeParamWithString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: string | Resource
```

页签内的图片内容。未设置时不显示图片。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarOptions-icon?: string | Resource--><!--Device-TabBarOptions-icon?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: string | Resource
```

页签内的文字内容。未设置时不显示文字。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarOptions-text?: string | Resource--><!--Device-TabBarOptions-text?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

