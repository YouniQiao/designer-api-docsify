# WakeupManager (System API)

Implements wakeup management.

**Since:** 12

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

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700107](../errorcode-intelligentVoice.md#22700107-system-error) |

## enrollWithWakeupFilesForResult

```TypeScript
enrollWithWakeupFilesForResult(wakeupFiles: Array<WakeupSourceFile>, wakeupInfo: string): Promise<EnrollResult>
```

Enrolls with wakeup files for result. This method uses a promise to return the enroll result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wakeupFiles | Array&lt;[WakeupSourceFile](arkts-basicservices-intelligentvoice-wakeupsourcefile-i-sys.md)&gt; | Yes |
| wakeupInfo | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EnrollResult](arkts-basicservices-intelligentvoice-enrollresult-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22700101](../errorcode-intelligentVoice.md#22700101-insufficient-memory) |
| [22700102](../errorcode-intelligentVoice.md#22700102-invalid-parameter) |
| [22700107](../errorcode-intelligentVoice.md#22700107-system-error) |

## getParameter

```TypeScript
getParameter(key: string): Promise<string>
```

Obtains the value of an intelligent voice parameter. This method uses a promise to return the query result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22700102](../errorcode-intelligentVoice.md#22700102-invalid-parameter) |
| [22700107](../errorcode-intelligentVoice.md#22700107-system-error) |

## getUploadFiles

```TypeScript
getUploadFiles (maxCount: number): Promise<Array<UploadFile>>
```

Obtains files needed to upload. This method uses a promise to return the files needed to upload.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxCount | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[UploadFile](arkts-basicservices-intelligentvoice-uploadfile-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22700101](../errorcode-intelligentVoice.md#22700101-insufficient-memory) |
| [22700102](../errorcode-intelligentVoice.md#22700102-invalid-parameter) |
| [22700107](../errorcode-intelligentVoice.md#22700107-system-error) |

## getWakeupSourceFiles

```TypeScript
getWakeupSourceFiles(): Promise<Array<WakeupSourceFile>>
```

Obtains wakeup source files. This method uses a promise to return the wakeup source files.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[WakeupSourceFile](arkts-basicservices-intelligentvoice-wakeupsourcefile-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700101](../errorcode-intelligentVoice.md#22700101-insufficient-memory) |
| [22700107](../errorcode-intelligentVoice.md#22700107-system-error) |

## setParameter

```TypeScript
setParameter(key: string, value: string): Promise<void>
```

Sets an intelligent voice parameter. This method uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

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
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22700102](../errorcode-intelligentVoice.md#22700102-invalid-parameter) |
| [22700107](../errorcode-intelligentVoice.md#22700107-system-error) |
