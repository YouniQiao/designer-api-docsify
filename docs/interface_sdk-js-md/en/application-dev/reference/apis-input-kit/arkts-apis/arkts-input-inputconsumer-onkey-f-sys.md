# onKey (System API)

## Modules to Import

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## onKey

```TypeScript
function onKey(keyOptions: KeyOptions, callback: Callback<KeyOptions>): void
```

Subscribe system keys.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputConsumer-function onKey(keyOptions: KeyOptions, callback: Callback<KeyOptions>): void--><!--Device-inputConsumer-function onKey(keyOptions: KeyOptions, callback: Callback<KeyOptions>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyOptions | [KeyOptions](../../apis-test-kit/arkts-apis/arkts-test-uitest-keyoptions-i.md) | Yes | the key events about input which is to be subscribed. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;KeyOptions&gt; | Yes | callback function, receive reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |


## onKey

```TypeScript
function onKey(keyOptions: KeyOptions, callback:KeyCommandCallback): void
```

Subscribe system keys.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputConsumer-function onKey(keyOptions: KeyOptions, callback:KeyCommandCallback): void--><!--Device-inputConsumer-function onKey(keyOptions: KeyOptions, callback:KeyCommandCallback): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyOptions | [KeyOptions](../../apis-test-kit/arkts-apis/arkts-test-uitest-keyoptions-i.md) | Yes | the key events about input which is to be subscribed. |
| callback | [KeyCommandCallback](arkts-input-inputconsumer-keycommandcallback-t-sys.md) | Yes | callback function, receive reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

