# remove (System API)

## Modules to Import

```TypeScript
import { recent } from 'kits/@kit.CoreFileKit';
```

## remove

```TypeScript
function remove(uri: string): void
```

将uri对应的文件从最近访问列表中移除。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-recent-function remove(uri: string): void--><!--Device-recent-function remove(uri: string): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 公共目录文件类URI。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900002 | No such file or directory |
| 13900042 | Unknown error |

## Examples

```TypeScript
let uri = 'file://docs/storage/Users/currentUser/<publicPath>';
recent.remove(uri);
```

