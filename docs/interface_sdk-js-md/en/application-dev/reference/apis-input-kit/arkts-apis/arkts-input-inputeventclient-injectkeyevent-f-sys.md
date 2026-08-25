# injectKeyEvent (System API)

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## injectKeyEvent

```TypeScript
function injectKeyEvent(keyEvent: KeyEventData): void
```

Injects key events (for both single keys and combination keys).

**Since:** 11

**Required permissions:** 
- API version 12+: ohos.permission.INJECT_INPUT_EVENT

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [keyEvent](arkts-input-inputeventclient-keyeventdata-i-sys.md) | [KeyEventData](arkts-input-inputeventclient-keyeventdata-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
