# @ohos.hiviewdfx.hiRetrieval

本模块提供应用灰度故障维测能力，支持以下故障类型：RSS内存泄漏、ArkTS-OOM、FD内存泄漏、GPU内存泄漏。应用灰度特性是一种运维态功能，用于精准采集故障日志。 开发者在端侧集成应用灰度功能后，该应用可参与应用灰度活动。通过云端平台发布应用灰度任务，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**系统能力：** SystemCapability.HiviewDFX.HiRetrieval

## 导入模块

```TypeScript
import { hiRetrieval } from '@kit.PerformanceAnalysisKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getCurrentConfig](arkts-performanceanalysis-hiretrieval-getcurrentconfig-f.md) |
| [getLastParticipationTimestamp](arkts-performanceanalysis-hiretrieval-getlastparticipationtimestamp-f.md) |
| [init](arkts-performanceanalysis-hiretrieval-init-f.md) |
| [isParticipant](arkts-performanceanalysis-hiretrieval-isparticipant-f.md) |
| [participate](arkts-performanceanalysis-hiretrieval-participate-f.md) |
| [quit](arkts-performanceanalysis-hiretrieval-quit-f.md) |
| [run](arkts-performanceanalysis-hiretrieval-run-f.md) |

### 接口

| 名称 |
| --- |
| [HiRetrievalConfig](arkts-performanceanalysis-hiretrieval-hiretrievalconfig-i.md) |
