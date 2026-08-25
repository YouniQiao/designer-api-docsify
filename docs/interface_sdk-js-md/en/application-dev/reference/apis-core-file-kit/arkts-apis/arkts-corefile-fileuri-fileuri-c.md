# FileUri

FileUri represents the uri of the file.@extends uri.URI

**Inheritance/Implementation:** FileUri extends uri.URI

**Since:** 15

**System capability:** SystemCapability.FileManagement.AppFileService

## Modules to Import

```TypeScript
import { fileUri } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor(uriOrPath: string)
```

Constructor for obtaining the instance of the FileUri class.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.FileManagement.AppFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uriOrPath | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900020 |
| 13900042 |
| 14300002 |

## getFullDirectoryUri

```TypeScript
getFullDirectoryUri(): string
```

Get the full directory uri where the file URI is located

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.FileManagement.AppFileService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900012 |
| 13900042 |

## isRemoteUri

```TypeScript
isRemoteUri(): boolean
```

Check whether the incoming URI is a remote URI

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.FileManagement.AppFileService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900042 |

## name

```TypeScript
get name(): string
```

Obtains the file name of uri.

**Type:** string

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.FileManagement.AppFileService
