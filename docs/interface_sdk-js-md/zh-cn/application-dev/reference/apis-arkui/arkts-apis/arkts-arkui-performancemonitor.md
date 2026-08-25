# @ohos.arkui.performanceMonitor(性能监测)

提供用户操作场景性能相关指标监测能力，在场景开始和结束时分别调用begin和end接口，即可获得该场景相关性能指标，目前仅包含响应时延、完成时延、丢帧。

> **说明：**&gt;
> - 从API Version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

> - 本模块接口为系统接口。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { performanceMonitor } from '@kit.ArkUI';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [begin(性能监测)](arkts-arkui-performancemonitor-begin-f-sys.md) |
| [end(性能监测)](arkts-arkui-performancemonitor-end-f-sys.md) |
| [recordInputEventTime(性能监测)](arkts-arkui-performancemonitor-recordinputeventtime-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ActionType(性能监测)](arkts-arkui-performancemonitor-actiontype-e-sys.md) |
| [SourceType(性能监测)](arkts-arkui-performancemonitor-sourcetype-e-sys.md) |
<!--DelEnd-->
