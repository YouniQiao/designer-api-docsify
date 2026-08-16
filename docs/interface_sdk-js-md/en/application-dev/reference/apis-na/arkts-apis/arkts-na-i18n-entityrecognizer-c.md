# EntityRecognizer

Provide some functions to find named entity in text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-i18n-export class EntityRecognizer--><!--Device-i18n-export class EntityRecognizer-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale?: string)
```

Creates an entityRecognizer object. This object is used to recognize entities in the text for the specified locale.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EntityRecognizer-constructor(locale?: string)--><!--Device-EntityRecognizer-constructor(locale?: string)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | No | Locale ID, which consists of the language, script, and country/region, for example, "zh-Hans-CN". The default value is the current system locale. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## findEntityInfo

```TypeScript
findEntityInfo(text: string): Array<EntityInfoItem>
```

Obtains entity information in the text object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EntityRecognizer-findEntityInfo(text: string): Array<EntityInfoItem>--><!--Device-EntityRecognizer-findEntityInfo(text: string): Array<EntityInfoItem>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text object. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[EntityInfoItem](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-entityinfoitem-i.md)&gt; | List of entities in the text. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

