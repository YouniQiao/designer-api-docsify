# createFileAccessHelper (System API)

## Modules to Import

```TypeScript
import { fileAccess } from 'kits/@kit.CoreFileKit';
```

## createFileAccessHelper

```TypeScript
function createFileAccessHelper(context: Context): FileAccessHelper
```

Creates a **Helper** object to bind with all file management services in the system. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileAccessHelper](arkts-corefile-fileaccess-fileaccesshelper-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |


## createFileAccessHelper

```TypeScript
function createFileAccessHelper(context: Context, wants: Array<Want>): FileAccessHelper
```

Creates a **Helper** object to bind with the specified Wants. This API returns the result synchronously. The **Helper** object provides file access and management capabilities.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| wants | Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileAccessHelper](arkts-corefile-fileaccess-fileaccesshelper-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |
