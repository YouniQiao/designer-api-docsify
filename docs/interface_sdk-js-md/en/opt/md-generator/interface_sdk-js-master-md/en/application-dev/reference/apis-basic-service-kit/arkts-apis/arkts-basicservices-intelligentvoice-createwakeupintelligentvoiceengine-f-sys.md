# createWakeupIntelligentVoiceEngine (System API)

## Modules to Import

```TypeScript
import { intelligentVoice } from '@kit.BasicServicesKit';
```

## createWakeupIntelligentVoiceEngine

```TypeScript
function createWakeupIntelligentVoiceEngine(descriptor: WakeupIntelligentVoiceEngineDescriptor, callback: AsyncCallback<WakeupIntelligentVoiceEngine>): void
```

Obtains an [WakeupIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceengine-i-sys.md#WakeupIntelligentVoiceEngine-(System-API)) instance. This method uses an asynchronous callback to return the WakeupIntelligentVoiceEngine instance.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-intelligentVoice-function createWakeupIntelligentVoiceEngine(descriptor: WakeupIntelligentVoiceEngineDescriptor, callback: AsyncCallback<WakeupIntelligentVoiceEngine>): void--><!--Device-intelligentVoice-function createWakeupIntelligentVoiceEngine(descriptor: WakeupIntelligentVoiceEngineDescriptor, callback: AsyncCallback<WakeupIntelligentVoiceEngine>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | [WakeupIntelligentVoiceEngineDescriptor](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceenginedescriptor-i-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[WakeupIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceengine-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |
| [22700101](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let wakeupEngineDescriptor: intelligentVoice.WakeupIntelligentVoiceEngineDescriptor = {
  needReconfirm: true,
  wakeupPhrase: 'Xiaohua Xiaohua',
}
let wakeupIntelligentVoiceEngine: intelligentVoice.WakeupIntelligentVoiceEngine | null = null;
intelligentVoice.createWakeupIntelligentVoiceEngine(wakeupEngineDescriptor, (err: BusinessError, data: intelligentVoice.WakeupIntelligentVoiceEngine) => {
  if (err) {
    console.error(`Failed to create wakeupIntelligentVoice engine, Code:${err.code}, message:${err.message}`);
  } else {
    console.info(`Succeeded in creating wakeupIntelligentVoice engine.`);
    wakeupIntelligentVoiceEngine = data;
  }
});
```


## createWakeupIntelligentVoiceEngine

```TypeScript
function createWakeupIntelligentVoiceEngine(descriptor: WakeupIntelligentVoiceEngineDescriptor): Promise<WakeupIntelligentVoiceEngine>
```

Obtains an [WakeupIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceengine-i-sys.md#WakeupIntelligentVoiceEngine-(System-API)) instance. This method uses a promise to return the WakeupIntelligentVoiceEngine instance.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-intelligentVoice-function createWakeupIntelligentVoiceEngine(descriptor: WakeupIntelligentVoiceEngineDescriptor): Promise<WakeupIntelligentVoiceEngine>--><!--Device-intelligentVoice-function createWakeupIntelligentVoiceEngine(descriptor: WakeupIntelligentVoiceEngineDescriptor): Promise<WakeupIntelligentVoiceEngine>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | [WakeupIntelligentVoiceEngineDescriptor](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceenginedescriptor-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[WakeupIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceengine-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |
| [22700101](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let wakeupEngineDescriptor: intelligentVoice.WakeupIntelligentVoiceEngineDescriptor = {
  needReconfirm: true,
  wakeupPhrase: 'Xiaohua Xiaohua',
}
let wakeupIntelligentVoiceEngine: intelligentVoice.WakeupIntelligentVoiceEngine | null = null;
intelligentVoice.createWakeupIntelligentVoiceEngine(wakeupEngineDescriptor).then((data: intelligentVoice.WakeupIntelligentVoiceEngine) => {
  wakeupIntelligentVoiceEngine = data;
  console.info(`Succeeded in creating wakeupIntelligentVoice engine.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create wakeupIntelligentVoice engine, Code:${err.code}, message:${err.message}`);
});
```
