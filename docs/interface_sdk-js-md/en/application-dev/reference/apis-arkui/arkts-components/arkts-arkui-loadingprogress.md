# LoadingProgress

LoadingProgress是用于显示加载进度条的组件，在数据加载过程中为用户提供视觉反馈，提升用户体验。该组件支持设置前景色、控制动画显示状态等特性，适用于需要在应用内展示加载进度的场景。

加载进度条的动效在组件不可见时停止，组件的可见状态基于
[onVisibleAreaChange]{@link CommonMethod#onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback)}
处理，可见阈值ratios大于0即视为可见状态。

> **说明：**
>
> - 该组件从API版本26.0.0开始支持[WithTheme]{@link ./with_theme}。

## 子组件

无

## LoadingProgress

```TypeScript
LoadingProgress()
```

创建加载进度组件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LoadingProgressInterface-(): LoadingProgressAttribute--><!--Device-LoadingProgressInterface-(): LoadingProgressAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

- [LoadingProgressConfiguration](arkts-arkui-loadingprogress-loadingprogressconfiguration-i.md)
- [LoadingProgressStyle](arkts-arkui-loadingprogress-loadingprogressstyle-e.md)
