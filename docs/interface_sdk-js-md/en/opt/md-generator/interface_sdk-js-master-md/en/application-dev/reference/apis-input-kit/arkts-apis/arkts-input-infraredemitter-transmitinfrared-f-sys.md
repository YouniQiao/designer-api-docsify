# transmitInfrared (System API)

## Modules to Import

```TypeScript
import { infraredEmitter } from '@kit.InputKit';
```

## transmitInfrared

```TypeScript
function transmitInfrared(infraredFrequency: number, pattern: Array<number>): void
```

Generates IR signals at the specified frequency and level.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

<!--Device-infraredEmitter-function transmitInfrared(infraredFrequency: long, pattern: Array<long>): void--><!--Device-infraredEmitter-function transmitInfrared(infraredFrequency: long, pattern: Array<long>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InfraredEmitter

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| infraredFrequency | number | Yes |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | Array & lt;number & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { infraredEmitter } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Set the infrared carrier frequency and infrared level signal mode
            infraredEmitter.transmitInfrared(38000, [100, 200, 300, 400]);
          } catch (error) {
            console.error(`Failed to set infrared frequencies, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
