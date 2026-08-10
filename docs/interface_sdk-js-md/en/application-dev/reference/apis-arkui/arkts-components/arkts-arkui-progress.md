# Progress

进度条组件，用于显示内容加载或操作处理等进度。支持线性、环形、圆形、胶囊等多种样式，可自定义颜色、渐变效果和动效，适用于文件下载、数据加载、任务处理等需要展示进度状态的场景。通过丰富的样式与动效配置，可快速实现进度可视化，提升用户体
验。

## 子组件

无

## Progress

```TypeScript
Progress(options: ProgressOptions<Type>)
```

创建进度条组件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressInterface-<Type extends keyof ProgressStyleMap>(options: ProgressOptions<Type>): ProgressAttribute<Type>--><!--Device-ProgressInterface-<Type extends keyof ProgressStyleMap>(options: ProgressOptions<Type>): ProgressAttribute<Type>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ProgressOptions](arkts-arkui-progressoptions-i.md)&lt;Type&gt; | Yes | 按进度条类型不同，设置不同属性的进度条组件参数。 |

## Summary

- [CapsuleStyleOptions](arkts-arkui-progress-capsulestyleoptions-i.md)
- [CommonProgressStyleOptions](arkts-arkui-progress-commonprogressstyleoptions-i.md)
- [EclipseStyleOptions](arkts-arkui-progress-eclipsestyleoptions-i.md)
- [LinearStyleOptions](arkts-arkui-progress-linearstyleoptions-i.md)
- [ProgressConfiguration](arkts-arkui-progress-progressconfiguration-i.md)
- [ProgressOptions](arkts-arkui-progress-progressoptions-i.md)
- [ProgressStyleMap](arkts-arkui-progress-progressstylemap-i.md)
- [ProgressStyleOptions](arkts-arkui-progress-progressstyleoptions-i.md)
- [RingStyleOptions](arkts-arkui-progress-ringstyleoptions-i.md)
- [ScaleRingStyleOptions](arkts-arkui-progress-scaleringstyleoptions-i.md)
- [ScanEffectOptions](arkts-arkui-progress-scaneffectoptions-i.md)
- [ProgressStatus](arkts-arkui-progress-progressstatus-e.md)
- [ProgressStyle](arkts-arkui-progress-progressstyle-e.md)
- [ProgressType](arkts-arkui-progress-progresstype-e.md)
