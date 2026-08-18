# WakeupIntelligentVoiceEngine (System API)

Implements wakeup intelligent voice engine.

**Since:** 23

<!--Device-intelligentVoice-interface WakeupIntelligentVoiceEngine--><!--Device-intelligentVoice-interface WakeupIntelligentVoiceEngine-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## getParameter

```TypeScript
getParameter(key: string, callback: AsyncCallback<string>): void
```

Obtains the value of an intelligent voice parameter. This method uses an asynchronous callback to return the query result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-getParameter(key: string, callback: AsyncCallback<string>): void--><!--Device-WakeupIntelligentVoiceEngine-getParameter(key: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).getParameter('key', (err: BusinessError, data: string) => {
    if (err) {
      console.error(`Failed to get parameter, Code:${err.code}, message:${err.message}`);
    } else {
      let param: string = data;
      console.info(`Succeeded in getting parameter, param:${param}`);
    }
  });
}
```

## getParameter

```TypeScript
getParameter(key: string): Promise<string>
```

Obtains the value of an intelligent voice parameter. This method uses a promise to return the query result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-getParameter(key: string): Promise<string>--><!--Device-WakeupIntelligentVoiceEngine-getParameter(key: string): Promise<string>-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).getParameter('key').then((data: string) => {
    let param: string = data;
    console.info(`Succeeded in getting parameter, param:${param}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get parameter, Code:${err.code}, message:${err.message}`);
  });
}
```

## getPcm

```TypeScript
getPcm(): Promise<ArrayBuffer>
```

Gets pulse-code modulation audio. This method uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-getPcm(): Promise<ArrayBuffer>--><!--Device-WakeupIntelligentVoiceEngine-getPcm(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700101](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).getPcm().then((data: ArrayBuffer) => {
    let param: ArrayBuffer = data;
    console.info(`Succeeded in getting pcm, param:${param}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get pcm, Code:${err.code}, message:${err.message}`);
  });
}
```

## getSupportedRegions

```TypeScript
getSupportedRegions(callback: AsyncCallback<Array<string>>): void
```

Obtains the supported regions, This method uses an asynchronous callback to return the query result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-getSupportedRegions(callback: AsyncCallback<Array<string>>): void--><!--Device-WakeupIntelligentVoiceEngine-getSupportedRegions(callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).getSupportedRegions((err: BusinessError, data: Array<string>) => {
    if (err) {
      console.error(`Failed to get supported regions, Code:${err.code}, message:${err.message}`);
    } else {
      let regions: Array<string> = data;
      console.info(`Succeeded in getting supported regions, regions:${regions}.`);
    }
  });
}
```

## getSupportedRegions

```TypeScript
getSupportedRegions(): Promise<Array<string>>
```

Obtains the supported regions, This method uses a promise to return the query result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-getSupportedRegions(): Promise<Array<string>>--><!--Device-WakeupIntelligentVoiceEngine-getSupportedRegions(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).getSupportedRegions().then((data: Array<string>) => {
    let regions: Array<string> = data;
    console.info(`Succeeded in getting supported regions, regions:${regions}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get supported regions, Code:${err.code}, message:${err.message}`);
  });
}
```

## offWakeupIntelligentVoiceEvent

```TypeScript
offWakeupIntelligentVoiceEvent(callback?: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void
```

Unsubscribes wakeup intelligent voice events.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-offWakeupIntelligentVoiceEvent(callback?: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void--><!--Device-WakeupIntelligentVoiceEngine-offWakeupIntelligentVoiceEvent(callback?: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WakeupIntelligentVoiceEngineCallbackInfo](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceenginecallbackinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_wakeupIntelligentVoiceEvent

```TypeScript
off(type: 'wakeupIntelligentVoiceEvent', callback?: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void
```

Unsubscribes wakeup intelligent voice events.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-off(type: 'wakeupIntelligentVoiceEvent', callback?: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void--><!--Device-WakeupIntelligentVoiceEngine-off(type: 'wakeupIntelligentVoiceEvent', callback?: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'wakeupIntelligentVoiceEvent' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WakeupIntelligentVoiceEngineCallbackInfo](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceenginecallbackinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).off('wakeupIntelligentVoiceEvent');
}
```

## onWakeupIntelligentVoiceEvent

```TypeScript
onWakeupIntelligentVoiceEvent(callback: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void
```

Subscribes wakeup intelligent voice events. When wakeup intelligent voice events reach, the callback is invoked.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-onWakeupIntelligentVoiceEvent(callback: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void--><!--Device-WakeupIntelligentVoiceEngine-onWakeupIntelligentVoiceEvent(callback: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WakeupIntelligentVoiceEngineCallbackInfo](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceenginecallbackinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_wakeupIntelligentVoiceEvent

```TypeScript
on(type: 'wakeupIntelligentVoiceEvent', callback: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void
```

Subscribes wakeup intelligent voice events. When wakeup intelligent voice events reach, the callback is invoked.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-on(type: 'wakeupIntelligentVoiceEvent', callback: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void--><!--Device-WakeupIntelligentVoiceEngine-on(type: 'wakeupIntelligentVoiceEvent', callback: Callback<WakeupIntelligentVoiceEngineCallbackInfo>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'wakeupIntelligentVoiceEvent' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WakeupIntelligentVoiceEngineCallbackInfo](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceenginecallbackinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).on('wakeupIntelligentVoiceEvent',
    (info: intelligentVoice.WakeupIntelligentVoiceEngineCallbackInfo) => {
    let callbackInfo: intelligentVoice.WakeupIntelligentVoiceEngineCallbackInfo = info;
    console.info(`wakeup intelligentvoice event, info:${callbackInfo}`);
  });
}
```

## read

```TypeScript
read(): Promise<ArrayBuffer>
```

Reads the buffer from wakeup engine. This method uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-read(): Promise<ArrayBuffer>--><!--Device-WakeupIntelligentVoiceEngine-read(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [22700106](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700106-failed-to-read-data) |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700101](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).read().then((data: ArrayBuffer) => {
    let param: ArrayBuffer = data;
    console.info(`Succeeded in reading data, param:${param}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to read data, Code:${err.code}, message:${err.message}`);
  });
}
```

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the engine, This method uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-release(callback: AsyncCallback<void>): void--><!--Device-WakeupIntelligentVoiceEngine-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release wakeupIntelligentVoice engine, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in releasing wakeupIntelligentVoice engine.`);
    }
  });
}
```

## release

```TypeScript
release(): Promise<void>
```

Releases the engine, This method uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-release(): Promise<void>--><!--Device-WakeupIntelligentVoiceEngine-release(): Promise<void>-End-->

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).release().then(() => {
    console.info(`Succeeded in releasing wakeupIntelligentVoice engine.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to release wakeupIntelligentVoice engine, Code:${err.code}, message:${err.message}`);
  });
}
```

## setParameter

```TypeScript
setParameter(key: string, value: string, callback: AsyncCallback<void>): void
```

Sets an intelligent voice parameter. This method uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-setParameter(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-WakeupIntelligentVoiceEngine-setParameter(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).setParameter('scene', '0', (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set parameter, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in setting parameter`);
    }
  });
}
```

## setParameter

```TypeScript
setParameter(key: string, value: string): Promise<void>
```

Sets an intelligent voice parameter. This method uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-setParameter(key: string, value: string): Promise<void>--><!--Device-WakeupIntelligentVoiceEngine-setParameter(key: string, value: string): Promise<void>-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).setParameter('scene', '0').then(() => {
    console.info(`Succeeded in setting parameter`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set parameter, Code:${err.code}, message:${err.message}`);
  });
}
```

## setSensibility

```TypeScript
setSensibility(sensibility: SensibilityType, callback: AsyncCallback<void>): void
```

Sets sensibility, This method uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-setSensibility(sensibility: SensibilityType, callback: AsyncCallback<void>): void--><!--Device-WakeupIntelligentVoiceEngine-setSensibility(sensibility: SensibilityType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sensibility | [SensibilityType](arkts-basicservices-intelligentvoice-sensibilitytype-e-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).setSensibility(intelligentVoice.SensibilityType.LOW_SENSIBILITY, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set sensibility, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in setting sensibility.`);
    }
  });
}
```

## setSensibility

```TypeScript
setSensibility(sensibility: SensibilityType): Promise<void>
```

Sets sensibility, This method uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-setSensibility(sensibility: SensibilityType): Promise<void>--><!--Device-WakeupIntelligentVoiceEngine-setSensibility(sensibility: SensibilityType): Promise<void>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sensibility | [SensibilityType](arkts-basicservices-intelligentvoice-sensibilitytype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).setSensibility(intelligentVoice.SensibilityType.LOW_SENSIBILITY).then(() => {
    console.info(`Succeeded in setting sensibility.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set sensibility, Code:${err.code}, message:${err.message}`);
  });
}
```

## setWakeupHapInfo

```TypeScript
setWakeupHapInfo(info: WakeupHapInfo, callback: AsyncCallback<void>): void
```

Sets wakeup hap information, This method uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-setWakeupHapInfo(info: WakeupHapInfo, callback: AsyncCallback<void>): void--><!--Device-WakeupIntelligentVoiceEngine-setWakeupHapInfo(info: WakeupHapInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [WakeupHapInfo](arkts-basicservices-intelligentvoice-wakeuphapinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let hapInfo: intelligentVoice.WakeupHapInfo = {
  bundleName: 'com.wakeup',
  abilityName: 'WakeUpExtAbility',
}

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).setWakeupHapInfo(hapInfo, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set wakeup hap info, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in setting wakeup hap info.`);
    }
  });
}
```

## setWakeupHapInfo

```TypeScript
setWakeupHapInfo(info: WakeupHapInfo): Promise<void>
```

Sets wakeup hap information, This method uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-setWakeupHapInfo(info: WakeupHapInfo): Promise<void>--><!--Device-WakeupIntelligentVoiceEngine-setWakeupHapInfo(info: WakeupHapInfo): Promise<void>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [WakeupHapInfo](arkts-basicservices-intelligentvoice-wakeuphapinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let hapInfo: intelligentVoice.WakeupHapInfo = {
  bundleName: 'com.wakeup',
  abilityName: 'WakeUpExtAbility',
}
if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).setWakeupHapInfo(hapInfo).then(() => {
    console.info(`Succeeded in setting wakeup hap info.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set wakeup hap info, Code:${err.code}, message:${err.message}`);
  });
}
```

## startCapturer

```TypeScript
startCapturer(channels: number): Promise<void>
```

Starts the capturer. This method uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE and ohos.permission.MICROPHONE

<!--Device-WakeupIntelligentVoiceEngine-startCapturer(channels: int): Promise<void>--><!--Device-WakeupIntelligentVoiceEngine-startCapturer(channels: int): Promise<void>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| channels | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [22700105](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700105-failed-to-start-the-capturer) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700102](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700102-invalid-parameter) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).startCapturer(1).then(() => {
    console.info(`Succeeded in starting capturer`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to start capturer, Code:${err.code}, message:${err.message}`);
  });
}
```

## stopCapturer

```TypeScript
stopCapturer(): Promise<void>
```

Stops the capturer. This method uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-WakeupIntelligentVoiceEngine-stopCapturer(): Promise<void>--><!--Device-WakeupIntelligentVoiceEngine-stopCapturer(): Promise<void>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (wakeupIntelligentVoiceEngine != null) {
  (wakeupIntelligentVoiceEngine as intelligentVoice.WakeupIntelligentVoiceEngine).stopCapturer().then(() => {
    console.info(`Succeeded in stopping capturer`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to stop capturer, Code:${err.code}, message:${err.message}`);
  });
}
```
