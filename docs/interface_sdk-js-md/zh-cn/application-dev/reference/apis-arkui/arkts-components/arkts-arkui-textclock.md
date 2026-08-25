# TextClock

TextClock组件通过文本将当前系统时间显示在设备上，支持不同时区的时间显示和时间格式自定义，最高精度到秒级。适用于需要在应用界面上实时展示系统时间、支持多时区显示的场景，可帮助开发者快速实现时间文本展示功能，无需手动计算和更新时 间。
组件不可见时，时间变动将停止。组件的可见状态基于 onVisibleAreaChange 处理，可见阈值ratios大于0即视为可见状态。

## 子组件

无

## TextClock

```TypeScript
TextClock(options?: TextClockOptions)
```

创建文本时钟组件。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TextClockOptions](arkts-arkui-textclockoptions-i.md) | 否 |

## 汇总

### 接口

| 名称 |
| --- |
