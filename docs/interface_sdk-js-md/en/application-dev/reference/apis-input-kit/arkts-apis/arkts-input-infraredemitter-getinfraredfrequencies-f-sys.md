# getInfraredFrequencies (System API)

## Modules to Import

```TypeScript
import { infraredEmitter } from 'infraredEmitter';
```

## getInfraredFrequencies

```TypeScript
function getInfraredFrequencies(): Array<InfraredFrequency>
```

Queries the frequency range of IR signals supported by the device.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

<!--Device-infraredEmitter-function getInfraredFrequencies(): Array<InfraredFrequency>--><!--Device-infraredEmitter-function getInfraredFrequencies(): Array<InfraredFrequency>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InfraredEmitter

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InfraredFrequency](arkts-input-infraredemitter-infraredfrequency-i-sys.md)&gt; | Frequency range of IR signals, including multiple groups of maximum and minimum frequencies. <br>Since API version 23, one group of maximum and minimum frequencies, both of which are **0** Hz, are returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application.<br>**Applicable version:** 12 - 14 |

**Examples**

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
            let frequencies = infraredEmitter.getInfraredFrequencies();
            console.info(`frequencies: ${JSON.stringify(frequencies)}`);
          } catch (error) {
            console.error(`Get infrared frequencies failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

