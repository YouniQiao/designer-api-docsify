# write（系统接口）

## 导入模块

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## write

```TypeScript
function write(info: SysEventInfo): Promise<void>
```

系统事件打点方法，接收[SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md)类型的对象作为事件参数，使用promise方式作为异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.HiviewDFX.HiSysEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11200001](../errorcode-hisysevent-sys.md#11200001-非法的事件领域) |
| [11200002](../errorcode-hisysevent-sys.md#11200002-非法的事件名称) |
| [11200003](../errorcode-hisysevent-sys.md#11200003-环境异常) |
| [11200004](../errorcode-hisysevent-sys.md#11200004-事件长度超过限制) |
| [11200051](../errorcode-hisysevent-sys.md#11200051-非法的事件参数) |
| [11200052](../errorcode-hisysevent-sys.md#11200052-字符串类型的事件参数值的长度超过限制) |
| [11200053](../errorcode-hisysevent-sys.md#11200053-事件参数的数量超过限制) |
| [11200054](../errorcode-hisysevent-sys.md#11200054-数组类型的事件参数值的长度超过限制) |


## write

```TypeScript
function write(info: SysEventInfo, callback: AsyncCallback<void>): void
```

系统事件打点方法，接收[SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md)类型的对象作为事件参数，使用callback方式作为异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.HiviewDFX.HiSysEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11200001](../errorcode-hisysevent-sys.md#11200001-非法的事件领域) |
| [11200002](../errorcode-hisysevent-sys.md#11200002-非法的事件名称) |
| [11200003](../errorcode-hisysevent-sys.md#11200003-环境异常) |
| [11200004](../errorcode-hisysevent-sys.md#11200004-事件长度超过限制) |
| [11200051](../errorcode-hisysevent-sys.md#11200051-非法的事件参数) |
| [11200052](../errorcode-hisysevent-sys.md#11200052-字符串类型的事件参数值的长度超过限制) |
| [11200053](../errorcode-hisysevent-sys.md#11200053-事件参数的数量超过限制) |
| [11200054](../errorcode-hisysevent-sys.md#11200054-数组类型的事件参数值的长度超过限制) |
