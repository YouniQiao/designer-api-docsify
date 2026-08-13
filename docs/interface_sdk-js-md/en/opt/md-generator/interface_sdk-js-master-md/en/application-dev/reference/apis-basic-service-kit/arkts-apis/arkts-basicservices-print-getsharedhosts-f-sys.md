# getSharedHosts (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## getSharedHosts

```TypeScript
function getSharedHosts(): Promise<SharedHost[]>
```

Get all available shared hosts.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function getSharedHosts(): Promise<SharedHost[]>--><!--Device-print-function getSharedHosts(): Promise<SharedHost[]>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SharedHost](arkts-basicservices-print-sharedhost-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
