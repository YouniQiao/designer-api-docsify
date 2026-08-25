# getAllSystemHotkeys

## Modules to Import

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## getAllSystemHotkeys

```TypeScript
function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>
```

Obtains all system shortcut keys. This API uses a promise to return the result.

**Since:** 14

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
