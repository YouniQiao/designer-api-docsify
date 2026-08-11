# @ohos.hiviewdfx.hiRetrieval

本模块提供应用灰度故障维测能力，支持以下故障类型：RSS内存泄漏、ArkTS-OOM、FD内存泄漏、GPU内存泄漏。应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成应用灰度功能后，该应用可参与应用灰度活动。通过云端平台发布应用灰度任务，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

**起始版本：** 26.0.0

<!--Device-unnamed-declare namespace hiRetrieval--><!--Device-unnamed-declare namespace hiRetrieval-End-->

**系统能力：** SystemCapability.HiviewDFX.HiRetrieval

## 汇总

### 函数

| 名称 |
| --- |
| [getCurrentConfig](arkts-performanceanalysis-hiretrieval-getcurrentconfig-f.md#getcurrentconfig) |
| [getLastParticipationTimestamp](arkts-performanceanalysis-hiretrieval-getlastparticipationtimestamp-f.md#getlastparticipationtimestamp) |
| [init](arkts-performanceanalysis-hiretrieval-init-f.md#init) |
| [isParticipant](arkts-performanceanalysis-hiretrieval-isparticipant-f.md#isparticipant) |
| [participate](arkts-performanceanalysis-hiretrieval-participate-f.md#participate) |
| [quit](arkts-performanceanalysis-hiretrieval-quit-f.md#quit) |
| [run](arkts-performanceanalysis-hiretrieval-run-f.md#run) |

### 接口

| 名称 |
| --- |
| [HiRetrievalConfig](arkts-performanceanalysis-hiretrieval-hiretrievalconfig-i.md) |
