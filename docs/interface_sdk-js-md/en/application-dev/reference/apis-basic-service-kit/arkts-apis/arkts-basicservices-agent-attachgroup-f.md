# attachGroup

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## attachGroup

```TypeScript
function attachGroup(gid: string, tids: string[]): Promise<void>
```

向指定分组id中绑定多个下载任务id。使用Promise异步回调。

如果任意一个任务id不满足添加条件，则所有列表中的任务都不会添加到分组中。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-agent-function attachGroup(gid: string, tids: string[]): Promise<void>--><!--Device-agent-function attachGroup(gid: string, tids: string[]): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gid | string | Yes | 目标分组id。 |
| tids | string[] | Yes | 待绑定的任务id列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| 21900008 | Group deleted or not found. |
| 21900006 | Task removed or not found. |
| 21900007 | Operation with wrong task state. |
| 21900005 | Operation with wrong task mode. |
| 13400003 | Task service ability error. |

