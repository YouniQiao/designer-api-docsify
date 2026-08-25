# setSecurityLabel

## Modules to Import

```TypeScript
import { securityLabel } from 'kits/@kit.CoreFileKit';
```

## setSecurityLabel

```TypeScript
function setSecurityLabel(path: string, type: DataLevel): Promise<void>
```

Sets the data security level for a file or directory. The level can only be adjusted from low to high, or set to the same level. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900007 |
| 13900015 |
| 13900020 |
| 13900025 |
| 13900037 |
| 13900041 |
| 13900042 |


## setSecurityLabel

```TypeScript
function setSecurityLabel(path: string, type: DataLevel, callback: AsyncCallback<void>): void
```

Sets the data security level for a file or directory. The level can only be adjusted from low to high, or set to the same level. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900007 |
| 13900015 |
| 13900020 |
| 13900025 |
| 13900037 |
| 13900041 |
| 13900042 |
