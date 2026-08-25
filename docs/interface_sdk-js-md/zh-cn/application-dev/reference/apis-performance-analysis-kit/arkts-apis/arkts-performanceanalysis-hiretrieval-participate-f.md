# participate

## 导入模块

```TypeScript
import { hiRetrieval } from '@kit.PerformanceAnalysisKit';
```

## participate

```TypeScript
function participate(config: HiRetrievalConfig): void
```

设置此设备参与应用灰度活动。调用后向服务器发送参与灰度消息和应用灰度活动配置，服务器标记此设备为可圈选并记录该应用灰度活动配置作为算法参数。 多次调用将更新为最新的应用灰度活动配置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiRetrieval

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [HiRetrievalConfig](arkts-performanceanalysis-hiretrieval-hiretrievalconfig-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| 36000001 |
