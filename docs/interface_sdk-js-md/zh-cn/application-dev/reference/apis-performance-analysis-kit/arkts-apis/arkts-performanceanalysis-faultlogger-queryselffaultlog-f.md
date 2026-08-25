# querySelfFaultLog

## 导入模块

```TypeScript
import { FaultLogger } from 'kits/@kit.PerformanceAnalysisKit';
```

## querySelfFaultLog

```TypeScript
function querySelfFaultLog(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void
```

获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** query

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md)&gt;&gt; | 是 |


## querySelfFaultLog

```TypeScript
function querySelfFaultLog(faultType: FaultType): Promise<Array<FaultLogInfo>>
```

获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** query

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md)&gt;&gt; |
