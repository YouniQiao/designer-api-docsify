# RootInfo (System API)

Provides APIs for managing the device's root attribute information.

**Since:** 9

**Deprecated since:** 23

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fileAccess } from 'kits/@kit.CoreFileKit';
```

## listFile

```TypeScript
listFile(filter?: Filter): FileIterator
```

Obtains a **FileIterator** object that lists the next-level files or directories matching the specified conditions of this directory. This API returns the result synchronously. [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md) is returned by [next()](arkts-corefile-fileaccess-fileiterator-i-sys.md#next). Currently, only built-in storage devices support the file filter.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** listFile

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |

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
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## scanFile

```TypeScript
scanFile(filter?: Filter): FileIterator
```

Obtains a **FileIterator** object that recursively retrieves the files matching the specified conditions from the device root directory. This API returns the result synchronously. [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md) is returned by [next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next). Currently, this API supports only built-in storage devices.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |

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
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## deviceFlags

```TypeScript
deviceFlags: number
```

Capabilities supported by the device.

**Type:** number

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## deviceType

```TypeScript
deviceType: number
```

Capabilities supported by the device.

**Type:** number

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## displayName

```TypeScript
displayName: string
```

Capabilities supported by the device.

**Type:** string

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## relativePath

```TypeScript
relativePath: string
```

Relative path of the root directory.

**Type:** string

**Since:** 10

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## uri

```TypeScript
uri: string
```

Capabilities supported by the device.

**Type:** string

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.
