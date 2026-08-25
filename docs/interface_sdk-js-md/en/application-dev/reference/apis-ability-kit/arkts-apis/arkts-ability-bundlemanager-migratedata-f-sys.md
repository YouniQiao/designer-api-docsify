# migrateData (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## migrateData

```TypeScript
function migrateData(sourcePaths: Array<string>, destinationPath: string): Promise<void>
```

Migrates files from the source path to the destination path. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.MIGRATE_DATA

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourcePaths | Array & lt;string & gt; | Yes |
| destinationPath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700080](../errorcode-bundle.md#17700080-invalid-source-paths) |
| [17700081](../errorcode-bundle.md#17700081-invalid-destination-path) |
| [17700082](../errorcode-bundle.md#17700082-user-authentication-failed) |
| [17700083](../errorcode-bundle.md#17700083-user-authentication-times-out) |
| [17700084](../errorcode-bundle.md#17700084-no-read-permissions-for-source-paths) |
| [17700085](../errorcode-bundle.md#17700085-no-write-permissions-for-the-destination-path) |
| [17700086](../errorcode-bundle.md#17700086-system-error) |
