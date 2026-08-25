# query

## 导入模块

```TypeScript
import { FaultLogger } from 'kits/@kit.PerformanceAnalysisKit';
```

## query

```TypeScript
function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void
```

获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10600001](../errorcode-faultlogger.md#10600001-服务未启动或故障) |


## query

```TypeScript
function query(faultType: FaultType): Promise<Array<FaultLogInfo>>
```

获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10600001](../errorcode-faultlogger.md#10600001-服务未启动或故障) |
