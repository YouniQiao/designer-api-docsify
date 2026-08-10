# WorkerOptions

Worker构造函数的选项，用于为Worker添加其他信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-export interface WorkerOptions--><!--Device-unnamed-export interface WorkerOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## name

```TypeScript
name?: string
```

Worker的名称。默认值为undefined，此时线程名称为'WorkerThread'。非默认值情况下，对应的线程名称带有'WorkerThread_'前缀。比如name为'testName'时，对应的线程名称为'WorkerThread_testName'。线程名称可通过HeapMemoryInfo的threadName获取。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WorkerOptions-name?: string--><!--Device-WorkerOptions-name?: string-End-->

**System capability:** SystemCapability.Utils.Lang

## priority

```TypeScript
priority?: ThreadWorkerPriority
```

表示Worker线程优先级。默认值为MEDIUM。

**Type:** [ThreadWorkerPriority](arkts-arkts-worker-threadworkerpriority-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-WorkerOptions-priority?: ThreadWorkerPriority--><!--Device-WorkerOptions-priority?: ThreadWorkerPriority-End-->

**System capability:** SystemCapability.Utils.Lang

## shared

```TypeScript
shared?: boolean
```

表示Worker共享功能，此接口暂不支持。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WorkerOptions-shared?: boolean--><!--Device-WorkerOptions-shared?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## type

```TypeScript
type?: 'classic' | 'module'
```

Worker执行脚本的模式类型，暂不支持module类型，默认值为classic。

**Type:** 'classic' \| 'module'

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WorkerOptions-type?: 'classic' | 'module'--><!--Device-WorkerOptions-type?: 'classic' | 'module'-End-->

**System capability:** SystemCapability.Utils.Lang

