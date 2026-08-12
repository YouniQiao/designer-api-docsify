# erase (System API)

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## erase

```TypeScript
function erase(volumeId: string): Promise<void>
```

Erases a volume. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function erase(volumeId: string): Promise<void>--><!--Device-volumeManager-function erase(volumeId: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600010 |
| 13600026 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600002 |
| 13600001 |
