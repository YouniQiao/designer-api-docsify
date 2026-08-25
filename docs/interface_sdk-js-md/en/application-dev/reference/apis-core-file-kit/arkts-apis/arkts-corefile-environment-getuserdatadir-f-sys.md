# getUserDataDir (System API)

## Modules to Import

```TypeScript
import { Environment } from '@kit.CoreFileKit';
```

## getUserDataDir

```TypeScript
function getUserDataDir(): Promise<string>
```

Obtains the root directory of user files. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.File.Environment

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900020 |
| 13900042 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
Environment.getUserDataDir().then((path: string) => {
  console.info("getUserDataDir successfully, Path: " + path);
}).catch((err: BusinessError) => {
  console.error("getUserDataDir failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
Environment.getUserDataDir((err: BusinessError, path: string) => {
  if (err) {
    console.error("getUserDataDir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("getUserDataDir successfully, Path: " + path);
  }
});
```


## getUserDataDir

```TypeScript
function getUserDataDir(callback: AsyncCallback<string>): void
```

Obtains the root directory of user files. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.File.Environment

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900020 |
| 13900042 |

**Examples**

See [getUserDataDir](#getuserdatadir)
