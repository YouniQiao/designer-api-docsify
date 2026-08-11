# Progress

Describes the data structure of the task progress.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-agent-interface Progress--><!--Device-agent-interface Progress-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## extras

```TypeScript
readonly extras?: object
```

Extra information of the task, for example, the header and body of the response from the server. The default value is empty.

**Type:** object

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly extras?: object--><!--Device-Progress-readonly extras?: object-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## index

```TypeScript
readonly index: int
```

Index of the file that is being processed in the task.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly index: int--><!--Device-Progress-readonly index: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## processed

```TypeScript
readonly processed: long
```

Size of processed data in the current file in the task, in bytes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly processed: long--><!--Device-Progress-readonly processed: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## sizes

```TypeScript
readonly sizes: Array<long>
```

Size of a file in a task, in bytes. If the server uses the chunk mode for data transmission and the total file size cannot be obtained from the request header, the value of **sizes** is treated as **-1**.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;long&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly sizes: Array<long>--><!--Device-Progress-readonly sizes: Array<long>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## state

```TypeScript
readonly state: State
```

Current task status.

**Type:** [State](arkts-basicservices-agent-state-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Progress-readonly state: State--><!--Device-Progress-readonly state: State-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

