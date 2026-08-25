# setEventConfig

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## setEventConfig

```TypeScript
function setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>
```

Sets event configuration. This method uses a promise to return the result. In the same lifecycle, you can set event configuration by event name.Configuration items vary depending on events. Currently, only the following events are supported:  
- **MAIN_THREAD_JANK** (For details about the parameter configuration, see  
[Main Thread Jank Event Overview](../../../dfx/hiappevent-watcher-mainthreadjank-events.md#parameters-of-seteventconfig).)  
- **APP_CRASH** (For details about the parameter configuration, see  
[Crash Log Configuration Parameters](../../../dfx/hiappevent-watcher-crash-events.md#customizing-crash-log-specifications).)  
- **RESOURCE_OVERLIMIT** (For details about the parameter configuration, see  
[Resource Leak Event Overview](../../../dfx/hiappevent-watcher-resourceleak-events.md#customizing-specifications).)

> **NOTE：**&gt;
> Since API version 26.0.0, all settings of this API are supported by
> [configEventPolicy](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md). You are advised to use
> [configEventPolicy](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md).

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| config | Record&lt;string, [ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
