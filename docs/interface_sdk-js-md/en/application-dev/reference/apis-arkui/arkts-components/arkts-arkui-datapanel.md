# DataPanel

数据面板组件，用于将多个数据占比情况使用占比图进行展示，支持环形和线性两种展示类型，可自定义颜色、阴影、底板等视觉效果，适用于存储容量、任务进度、资源占比等数据可视化场景，帮助用户直观了解数据分布情况。

> **说明：**
>
> - 该组件从API版本26.0.0开始支持[WithTheme]{@link ./with_theme}。

## 子组件

无

## DataPanel

```TypeScript
DataPanel(options: DataPanelOptions)
```

创建数据面板组件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-DataPanelInterface-(options: DataPanelOptions): DataPanelAttribute--><!--Device-DataPanelInterface-(options: DataPanelOptions): DataPanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DataPanelOptions](arkts-arkui-datapaneloptions-i.md) | Yes | 数据面板配置选项，用于设置数据面板的数据值列表、最大值和数据面板类型。 |

## Summary

- [ColorStop](arkts-arkui-datapanel-colorstop-i.md)
- [DataPanelConfiguration](arkts-arkui-datapanel-datapanelconfiguration-i.md)
- [DataPanelOptions](arkts-arkui-datapanel-datapaneloptions-i.md)
- [DataPanelShadowOptions](arkts-arkui-datapanel-datapanelshadowoptions-i.md)
- [DataPanelType](arkts-arkui-datapanel-datapaneltype-e.md)
