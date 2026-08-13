# Normalizer

Provides the text normalization capabilities.

**Since:** 23

**Deprecated since:** -1

<!--Device-i18n-export class Normalizer--><!--Device-i18n-export class Normalizer-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getInstance

```TypeScript
static getInstance(mode: NormalizerMode): Normalizer
```

Obtains a **Normalizer** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Normalizer-static getInstance(mode: NormalizerMode): Normalizer--><!--Device-Normalizer-static getInstance(mode: NormalizerMode): Normalizer-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [NormalizerMode](arkts-localization-i18n-normalizermode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Normalizer](arkts-localization-i18n-normalizer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Normalizer.getInstance failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## normalize

```TypeScript
normalize(text: string): string
```

Normalizes input strings.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Normalizer-normalize(text: string): string--><!--Device-Normalizer-normalize(text: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
  let normalizedText: string = normalizer.normalize('\u1E9B\u0323'); // normalizedText = 'ẛ̣'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Normalizer.getInstance failed, error code: ${err.code}, message: ${err.message}.`);
}
```
