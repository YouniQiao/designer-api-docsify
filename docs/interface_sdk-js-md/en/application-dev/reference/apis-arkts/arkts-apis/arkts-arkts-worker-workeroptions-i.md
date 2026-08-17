# WorkerOptions

Provides options that can be set for the Worker instance to create.

**Since:** 7

<!--Device-unnamed-export interface WorkerOptions--><!--Device-unnamed-export interface WorkerOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { DedicatedWorkerGlobalScope } from 'DedicatedWorkerGlobalScope';
import { ErrorEvent } from 'ErrorEvent';
import { Event } from 'Event';
import { EventListener } from 'EventListener';
import { EventTarget } from 'EventTarget';
import { MessageEvent } from 'MessageEvent';
import { MessageEvents } from 'MessageEvents';
import { PostMessageOptions } from 'PostMessageOptions';
import { ThreadWorkerGlobalScope } from 'ThreadWorkerGlobalScope';
import { WorkerEventListener } from 'WorkerEventListener';
import { WorkerEventTarget } from 'WorkerEventTarget';
import { WorkerOptions } from 'WorkerOptions';
import { ThreadWorkerPriority } from 'ThreadWorkerPriority';
import { Priority } from 'Priority';
```

## name

```TypeScript
name?: string
```

Name of the Worker thread. The default value is undefined.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WorkerOptions-name?: string--><!--Device-WorkerOptions-name?: string-End-->

**System capability:** SystemCapability.Utils.Lang

## priority

```TypeScript
priority?: ThreadWorkerPriority
```

Priority of the Worker thread.

**Type:** [ThreadWorkerPriority](arkts-arkts-worker-threadworkerpriority-e.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-WorkerOptions-priority?: ThreadWorkerPriority--><!--Device-WorkerOptions-priority?: ThreadWorkerPriority-End-->

**System capability:** SystemCapability.Utils.Lang

## shared

```TypeScript
shared?: boolean
```

Whether sharing of the Worker instance is enabled. Currently, sharing is not supported.

**Type:** boolean

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WorkerOptions-shared?: boolean--><!--Device-WorkerOptions-shared?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## type

```TypeScript
type?: 'classic' | 'module'
```

Mode in which the Worker instance executes the script. The module type is not supported yet. The default value is classic.

**Type:** 'classic' \| 'module'

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WorkerOptions-type?: 'classic' | 'module'--><!--Device-WorkerOptions-type?: 'classic' | 'module'-End-->

**System capability:** SystemCapability.Utils.Lang

