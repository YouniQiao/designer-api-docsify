# Normalizer

Provides the API for text encoding normalization.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-i18n-export class Normalizer--><!--Device-i18n-export class Normalizer-End-->

**System capability:** SystemCapability.Global.I18n

## getInstance

```TypeScript
static getInstance(mode: NormalizerMode): Normalizer
```

Obtains a Normalizer object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Normalizer-static getInstance(mode: NormalizerMode): Normalizer--><!--Device-Normalizer-static getInstance(mode: NormalizerMode): Normalizer-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [NormalizerMode](arkts-na-i18n-normalizermode-e.md) | Yes | Text normalization mode. |

**Return value:**

| Type | Description |
| --- | --- |
| [Normalizer](arkts-na-i18n-normalizer-c.md) | Normalizer object for text normalization. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

## normalize

```TypeScript
normalize(text: string): string
```

Normalizes input strings.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Normalizer-normalize(text: string): string--><!--Device-Normalizer-normalize(text: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Input strings. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Normalized strings. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

