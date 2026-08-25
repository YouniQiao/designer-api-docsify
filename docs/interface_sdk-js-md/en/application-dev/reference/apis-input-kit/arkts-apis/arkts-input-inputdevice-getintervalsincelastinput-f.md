# getIntervalSinceLastInput

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getIntervalSinceLastInput

```TypeScript
function getIntervalSinceLastInput(): Promise<number>
```

Obtains the interval (including the device sleep time) elapsed since the last system input event. This API uses a promise to return the result.

**Since:** 14

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |
