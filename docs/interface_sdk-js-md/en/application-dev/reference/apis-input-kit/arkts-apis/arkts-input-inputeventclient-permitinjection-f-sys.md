# permitInjection (System API)

## Modules to Import

```TypeScript
import { inputEventClient } from '@kit.InputKit';
```

## permitInjection

```TypeScript
function permitInjection(result: boolean): void
```

Specifies whether to authorize event injection.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.INJECT_INPUT_EVENT

<!--Device-inputEventClient-function permitInjection(result: boolean): void--><!--Device-inputEventClient-function permitInjection(result: boolean): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | boolean | Yes | Authorization result. The value **true** indicates that event injection is allowed, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

