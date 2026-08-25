# createEnrollIntelligentVoiceEngine (System API)

## Modules to Import

```TypeScript
import { intelligentVoice } from 'kits/@kit.BasicServicesKit';
```

## createEnrollIntelligentVoiceEngine

```TypeScript
function createEnrollIntelligentVoiceEngine(descriptor: EnrollIntelligentVoiceEngineDescriptor, callback: AsyncCallback<EnrollIntelligentVoiceEngine>): void
```

Obtains an [EnrollIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-enrollintelligentvoiceengine-i-sys.md) instance. This method uses an asynchronous callback to return the EnrollIntelligentVoiceEngine instance.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | [EnrollIntelligentVoiceEngineDescriptor](arkts-basicservices-intelligentvoice-enrollintelligentvoiceenginedescriptor-i-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[EnrollIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-enrollintelligentvoiceengine-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22700101](../errorcode-intelligentVoice.md#22700101-insufficient-memory) |
| [22700102](../errorcode-intelligentVoice.md#22700102-invalid-parameter) |


## createEnrollIntelligentVoiceEngine

```TypeScript
function createEnrollIntelligentVoiceEngine(descriptor: EnrollIntelligentVoiceEngineDescriptor): Promise<EnrollIntelligentVoiceEngine>
```

Obtains an [EnrollIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-enrollintelligentvoiceengine-i-sys.md) instance. This method uses a promise to return the EnrollIntelligentVoiceEngine instance.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | [EnrollIntelligentVoiceEngineDescriptor](arkts-basicservices-intelligentvoice-enrollintelligentvoiceenginedescriptor-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EnrollIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-enrollintelligentvoiceengine-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22700101](../errorcode-intelligentVoice.md#22700101-insufficient-memory) |
| [22700102](../errorcode-intelligentVoice.md#22700102-invalid-parameter) |
