# PosterOptions

用于描述当前视频是否配置首帧送显。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PosterOptions--><!--Device-unnamed-export declare interface PosterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentTransitionEffect

```TypeScript
contentTransitionEffect?: ContentTransitionEffect
```

当前视频的预览图内容变化时的转场动效。配置showFirstFrame为true（即配置开启首帧送显时），或未配置有效的VideoOptions的previewUri时，该字段不生效。默认值：ContentTransitionEffect.IDENTITY。设置为undefined或null时，取值为ContentTransitionEffect.IDENTITY。

**Type:** [ContentTransitionEffect](../arkts-components/arkts-arkui-contenttransitioneffect-c.md)

**Default:** ContentTransitionEffect.IDENTITY

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PosterOptions-contentTransitionEffect?: ContentTransitionEffect--><!--Device-PosterOptions-contentTransitionEffect?: ContentTransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showFirstFrame

```TypeScript
showFirstFrame?: boolean
```

当前视频是否配置首帧送显，当开启首帧送显时，VideoOptions中的previewUri字段不生效。true：开启首帧送显；false：关闭首帧送显。默认值：false

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PosterOptions-showFirstFrame?: boolean--><!--Device-PosterOptions-showFirstFrame?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

