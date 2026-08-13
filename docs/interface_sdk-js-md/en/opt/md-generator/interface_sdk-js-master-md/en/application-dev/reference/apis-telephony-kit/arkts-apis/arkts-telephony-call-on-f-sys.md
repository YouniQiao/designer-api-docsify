# on (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## on('callDetailsChange')

```TypeScript
function on(type: 'callDetailsChange', callback: Callback<CallAttributeOptions>): void
```

Subscribes to **callDetailsChange** events. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'callDetailsChange', callback: Callback<CallAttributeOptions>): void--><!--Device-call-function on(type: 'callDetailsChange', callback: Callback<CallAttributeOptions>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callDetailsChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallAttributeOptions](arkts-telephony-call-callattributeoptions-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
call.on('callDetailsChange', (data: call.CallAttributeOptions) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('callEventChange')

```TypeScript
function on(type: 'callEventChange', callback: Callback<CallEventOptions>): void
```

Subscribes to **callEventChange** events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'callEventChange', callback: Callback<CallEventOptions>): void--><!--Device-call-function on(type: 'callEventChange', callback: Callback<CallEventOptions>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callEventChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallEventOptions](arkts-telephony-call-calleventoptions-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
call.on('callEventChange', (data: call.CallEventOptions) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('callDisconnectedCause')

```TypeScript
function on(type: 'callDisconnectedCause', callback: Callback<DisconnectedDetails>): void
```

Subscribes to **callDisconnectedCause** events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'callDisconnectedCause', callback: Callback<DisconnectedDetails>): void--><!--Device-call-function on(type: 'callDisconnectedCause', callback: Callback<DisconnectedDetails>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callDisconnectedCause' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DisconnectedDetails](arkts-telephony-call-disconnecteddetails-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
call.on('callDisconnectedCause', (data: call.DisconnectedDetails) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('mmiCodeResult')

```TypeScript
function on(type: 'mmiCodeResult', callback: Callback<MmiCodeResults>): void
```

Subscribes to **mmiCodeResult** events. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'mmiCodeResult', callback: Callback<MmiCodeResults>): void--><!--Device-call-function on(type: 'mmiCodeResult', callback: Callback<MmiCodeResults>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mmiCodeResult' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MmiCodeResults](arkts-telephony-call-mmicoderesults-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
call.on('mmiCodeResult', (data: call.MmiCodeResults) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('audioDeviceChange')

```TypeScript
function on(type: 'audioDeviceChange', callback: Callback<AudioDeviceCallbackInfo>): void
```

Subscribes to audio device change events. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'audioDeviceChange', callback: Callback<AudioDeviceCallbackInfo>): void--><!--Device-call-function on(type: 'audioDeviceChange', callback: Callback<AudioDeviceCallbackInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioDeviceChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceCallbackInfo](arkts-telephony-call-audiodevicecallbackinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
call.on('audioDeviceChange', (data: call.AudioDeviceCallbackInfo) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('postDialDelay')

```TypeScript
function on(type: 'postDialDelay', callback: Callback<string>): void
```

Subscribes to **postDialDelay** events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'postDialDelay', callback: Callback<string>): void--><!--Device-call-function on(type: 'postDialDelay', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'postDialDelay' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
call.on('postDialDelay', (data: string) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('imsCallModeChange')

```TypeScript
function on(type: 'imsCallModeChange', callback: Callback<ImsCallModeInfo>): void
```

Subscribes to **imsCallModeChange** events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'imsCallModeChange', callback: Callback<ImsCallModeInfo>): void--><!--Device-call-function on(type: 'imsCallModeChange', callback: Callback<ImsCallModeInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imsCallModeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ImsCallModeInfo](arkts-telephony-call-imscallmodeinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.on('imsCallModeChange', (data: call.ImsCallModeInfo) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('callSessionEvent')

```TypeScript
function on(type: 'callSessionEvent', callback: Callback<CallSessionEvent>): void
```

Subscribes to **callSessionEvent** events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'callSessionEvent', callback: Callback<CallSessionEvent>): void--><!--Device-call-function on(type: 'callSessionEvent', callback: Callback<CallSessionEvent>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callSessionEvent' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallSessionEvent](arkts-telephony-call-callsessionevent-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.on('callSessionEvent', (data: call.CallSessionEvent) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('peerDimensionsChange')

```TypeScript
function on(type: 'peerDimensionsChange', callback: Callback<PeerDimensionsDetail>): void
```

Subscribes to **peerDimensionsChange** events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'peerDimensionsChange', callback: Callback<PeerDimensionsDetail>): void--><!--Device-call-function on(type: 'peerDimensionsChange', callback: Callback<PeerDimensionsDetail>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'peerDimensionsChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PeerDimensionsDetail](arkts-telephony-call-peerdimensionsdetail-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.on('peerDimensionsChange', (data: call.PeerDimensionsDetail) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## on('cameraCapabilitiesChange')

```TypeScript
function on(type: 'cameraCapabilitiesChange', callback: Callback<CameraCapabilities>): void
```

Subscribes to **cameraCapabilitiesChange** events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function on(type: 'cameraCapabilitiesChange', callback: Callback<CameraCapabilities>): void--><!--Device-call-function on(type: 'cameraCapabilitiesChange', callback: Callback<CameraCapabilities>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cameraCapabilitiesChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CameraCapabilities](arkts-telephony-call-cameracapabilities-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
call.on('cameraCapabilitiesChange', (data: call.CameraCapabilities) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```
