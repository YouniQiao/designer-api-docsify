# getSharedHosts (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## getSharedHosts

```TypeScript
function getSharedHosts(): Promise<SharedHost[]>
```

获取所有可用的共享主机。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function getSharedHosts(): Promise<SharedHost[]>--><!--Device-print-function getSharedHosts(): Promise<SharedHost[]>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SharedHost[]&gt; | Promise that resolves with the list of shared hosts. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 202 | not system application. |

