# permitInjection

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## permitInjection

```TypeScript
function permitInjection(result: boolean): void
```

Specifies whether to authorize event injection.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INJECT_INPUT_EVENT

<!--Device-inputEventClient-function permitInjection(result: boolean): void--><!--Device-inputEventClient-function permitInjection(result: boolean): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | boolean | Yes | Authorization result. The value **true** indicates that event injection is allowed, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

