# Progress

Describes the data structure of the task progress.

**Since:** 23

<!--Device-agent-interface Progress--><!--Device-agent-interface Progress-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from 'request';
```

## extras

```TypeScript
readonly extras?: Record<string, string>
```

The extras for an interaction. Such as headers and body of response from server. But when the Content-Disposition header responded, <br>the body will be into the uri of its attachment only, the body here is empty. {"headers": {"key": v}, "body": "contents"}. The "body" field is not supported in cross-platform scenarios.

**Type:** Record&lt;string, string&gt;

**Since:** 23

<!--Device-Progress-readonly extras?: Record<string, string>--><!--Device-Progress-readonly extras?: Record<string, string>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## index

```TypeScript
readonly index: int
```

Index of the file that is being processed in the task.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly index: int--><!--Device-Progress-readonly index: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## processed

```TypeScript
readonly processed: long
```

Size of processed data in the current file in the task, in bytes.

**Type:** long

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly processed: long--><!--Device-Progress-readonly processed: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## sizes

```TypeScript
readonly sizes: Array<long>
```

Size of a file in a task, in bytes. If the server uses the chunk mode for data transmission and the total file size cannot be obtained from the request header, the value of **sizes** is treated as **-1**.

**Type:** Array&lt;long&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly sizes: Array<long>--><!--Device-Progress-readonly sizes: Array<long>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## state

```TypeScript
readonly state: State
```

Current task status.

**Type:** State

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly state: State--><!--Device-Progress-readonly state: State-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

