# setSecurityLabel

## Modules to Import

```TypeScript
import { securityLabel } from '@kit.CoreFileKit';
```

## setSecurityLabel

```TypeScript
function setSecurityLabel(path: string, type: DataLevel): Promise<void>
```

Sets the data security level for a file or directory. The level can only be adjusted from low to high, or set to the same level. This API uses a promise to return the result.

**Since:** 9

<!--Device-securityLabel-function setSecurityLabel(path: string, type: DataLevel): Promise<void>--><!--Device-securityLabel-function setSecurityLabel(path: string, type: DataLevel): Promise<void>-End-->

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
| 13900020 |
| 13900037 |
| 13900007 |
| 13900001 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabel(filePath, "s0").then(() => {
  console.info("setSecurityLabel successfully");
}).catch((err: BusinessError) => {
  console.error("setSecurityLabel failed with error message: " + err.message + ", error code: " + err.code);
});
```


## setSecurityLabel

```TypeScript
function setSecurityLabel(path: string, type: DataLevel, callback: AsyncCallback<void>): void
```

Sets the data security level for a file or directory. The level can only be adjusted from low to high, or set to the same level. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-securityLabel-function setSecurityLabel(path: string, type: DataLevel, callback: AsyncCallback<void>): void--><!--Device-securityLabel-function setSecurityLabel(path: string, type: DataLevel, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900037 |
| 13900007 |
| 13900001 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabel(filePath, "s0", (err: BusinessError) => {
  if (err) {
    console.error("setSecurityLabel failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("setSecurityLabel successfully.");
  }
});
```
