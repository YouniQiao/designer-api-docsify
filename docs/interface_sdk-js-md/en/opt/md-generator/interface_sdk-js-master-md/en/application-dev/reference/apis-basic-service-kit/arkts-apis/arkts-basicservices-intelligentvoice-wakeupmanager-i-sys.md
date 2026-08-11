# WakeupManager (System API)

Implements wakeup management.

**Since:** 12

<!--Device-intelligentVoice-interface WakeupManager--><!--Device-intelligentVoice-interface WakeupManager-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { intelligentVoice } from 'kits/@kit.BasicServicesKit';
```

## clearUserData

```TypeScript
clearUserData(): Promise<void>
```

Clears user data.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupManager-clearUserData(): Promise<void>--><!--Device-WakeupManager-clearUserData(): Promise<void>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupManager != null) {
  (wakeupManager as intelligentVoice.WakeupManager).clearUserData().then(() => {
    console.info(`Succeeded in clearing user data.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to clear user data, Code:${err.code}, message:${err.message}`);
  });
}
```

## enrollWithWakeupFilesForResult

```TypeScript
enrollWithWakeupFilesForResult(wakeupFiles: Array<WakeupSourceFile>, wakeupInfo: string): Promise<EnrollResult>
```

Enrolls with wakeup files for result. This method uses a promise to return the enroll result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupManager-enrollWithWakeupFilesForResult(wakeupFiles: Array<WakeupSourceFile>, wakeupInfo: string): Promise<EnrollResult>--><!--Device-WakeupManager-enrollWithWakeupFilesForResult(wakeupFiles: Array<WakeupSourceFile>, wakeupInfo: string): Promise<EnrollResult>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wakeupFiles | Array&lt;WakeupSourceFile&gt; | Yes |
| wakeupInfo | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;EnrollResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |
| [22700101](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filesInfo: Array<intelligentVoice.WakeupSourceFile> = [];
filesInfo[0] = {filePath: "", fileContent: new ArrayBuffer(100)};
let wakeupInfo: string = "version: 123"

if (wakeupManager != null) {
  (wakeupManager as intelligentVoice.WakeupManager).enrollWithWakeupFilesForResult(
    filesInfo, wakeupInfo).then(
    (data: intelligentVoice.EnrollResult) => {
      let param: intelligentVoice.EnrollResult = data;
      console.info(`Succeeded in enrolling with wakeup files for result, param:${param}`);
    }).catch((err: BusinessError) => {
    console.error(`Failed to enroll with wakeup files for result, Code:${err.code}, message:${err.message}`);
  });
}
```

## getParameter

```TypeScript
getParameter(key: string): Promise<string>
```

Obtains the value of an intelligent voice parameter. This method uses a promise to return the query result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupManager-getParameter(key: string): Promise<string>--><!--Device-WakeupManager-getParameter(key: string): Promise<string>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupManager != null) {
  (wakeupManager as intelligentVoice.WakeupManager).getParameter('isEnrolled').then((data: string) => {
    let param: string = data;
    console.info(`Succeeded in getting parameter, param:${param}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get parameter, Code:${err.code}, message:${err.message}`);
  });
}
```

## getUploadFiles

```TypeScript
getUploadFiles (maxCount: number): Promise<Array<UploadFile>>
```

Obtains files needed to upload. This method uses a promise to return the files needed to upload.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupManager-getUploadFiles (maxCount: int): Promise<Array<UploadFile>>--><!--Device-WakeupManager-getUploadFiles (maxCount: int): Promise<Array<UploadFile>>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxCount | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;UploadFile&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |
| [22700101](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupManager != null) {
  (wakeupManager as intelligentVoice.WakeupManager).getUploadFiles(2).then((data: Array<intelligentVoice.UploadFile>) => {
    let param: Array<intelligentVoice.UploadFile> = data;
    console.info(`Succeeded in getting upload files, param:${param}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get upload files, Code:${err.code}, message:${err.message}`);
  });
}
```

## getWakeupSourceFiles

```TypeScript
getWakeupSourceFiles(): Promise<Array<WakeupSourceFile>>
```

Obtains wakeup source files. This method uses a promise to return the wakeup source files.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupManager-getWakeupSourceFiles(): Promise<Array<WakeupSourceFile>>--><!--Device-WakeupManager-getWakeupSourceFiles(): Promise<Array<WakeupSourceFile>>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;WakeupSourceFile&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700101](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupManager != null) {
  (wakeupManager as intelligentVoice.WakeupManager).getWakeupSourceFiles().then(
    (data: Array<intelligentVoice.WakeupSourceFile>) => {
    let param: Array<intelligentVoice.WakeupSourceFile> = data;
    console.info(`Succeeded in getting wakeup source files, param:${param}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get wakeup source files, Code:${err.code}, message:${err.message}`);
  });
}
```

## setParameter

```TypeScript
setParameter(key: string, value: string): Promise<void>
```

Sets an intelligent voice parameter. This method uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupManager-setParameter(key: string, value: string): Promise<void>--><!--Device-WakeupManager-setParameter(key: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupManager != null) {
  (wakeupManager as intelligentVoice.WakeupManager).setParameter('wakeup_phrase', 'xiaohuaxiaohua').then(() => {
    console.info(`Succeeded in setting parameter`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set parameter, Code:${err.code}, message:${err.message}`);
  });
}
```
