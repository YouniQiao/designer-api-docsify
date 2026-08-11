# transmitInfrared

## Modules to Import

```TypeScript
import { infraredEmitter } from 'kits/@kit.InputKit';
```

## transmitInfrared

```TypeScript
function transmitInfrared(infraredFrequency: long, pattern: Array<long>): void
```

Generates IR signals at the specified frequency and level.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

<!--Device-infraredEmitter-function transmitInfrared(infraredFrequency: long, pattern: Array<long>): void--><!--Device-infraredEmitter-function transmitInfrared(infraredFrequency: long, pattern: Array<long>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InfraredEmitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| infraredFrequency | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | IR frequency, in Hz. |
| pattern | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;long&gt; | Yes | Infrared level signal, in microseconds (μs). The number of infrared level signals ranges from 0 to 1024. The value of this parameter must be greater than 0. If this parameter is set to **0**, the API does not take effect. &lt;br/&gt;For example, in the level signal array [100,200,300,400], **100** indicates a high-level signal, **200** indicates a low-level signal, **300** is a high-level signal, and **400** is a low -level signal. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application.<br>**Applicable version:** 12 - 14 |

## Examples

```TypeScript
import { infraredEmitter } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            infraredEmitter.transmitInfrared(38000, [100, 200, 300, 400]);
          } catch (error) {
            console.error(`transmitInfrared failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

