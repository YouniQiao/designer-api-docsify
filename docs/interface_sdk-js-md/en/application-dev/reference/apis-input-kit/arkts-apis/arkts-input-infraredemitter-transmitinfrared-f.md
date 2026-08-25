# transmitInfrared

## Modules to Import

```TypeScript
import { infraredEmitter } from 'kits/@kit.InputKit';
```

## transmitInfrared

```TypeScript
function transmitInfrared(infraredFrequency: number, pattern: Array<number>): void
```

Generates IR signals at the specified frequency and level.

**Since:** 15

**Required permissions:** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

**System capability:** SystemCapability.MultimodalInput.Input.InfraredEmitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| infraredFrequency | number | Yes |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | Array & lt;number & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
