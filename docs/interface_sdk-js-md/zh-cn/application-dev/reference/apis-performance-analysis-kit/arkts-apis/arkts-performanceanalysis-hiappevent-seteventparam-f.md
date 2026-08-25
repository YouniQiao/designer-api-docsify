# setEventParam

## 导入模块

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## setEventParam

```TypeScript
function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>
```

事件自定义参数设置方法，使用Promise方式作为异步回调。在同一生命周期中，可以通过事件领域和事件名称关联系统事件和应用事件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | Record&lt;string, [ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md)&gt; | 是 |
| domain | string | 是 |
| name | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11100001](../errorcode-hiappevent.md#11100001-打点功能被关闭) |
| [11101001](../errorcode-hiappevent.md#11101001-非法的事件领域名称) |
| [11101002](../errorcode-hiappevent.md#11101002-非法的事件名称) |
| [11101004](../errorcode-hiappevent.md#11101004-非法的事件参数字符串长度) |
| [11101005](../errorcode-hiappevent.md#11101005-非法的事件参数名称) |
| [11101007](../errorcode-hiappevent.md#11101007-非法的事件自定义参数数量) |
