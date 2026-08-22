# addPreferredLanguage

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## addPreferredLanguage

```TypeScript
export function addPreferredLanguage(language: string, index?: int): boolean
```

Adds a preferred language to the specified position on the preferred language list.

**Since:** 8

**Deprecated since:** 9

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-i18n-export function addPreferredLanguage(language: string, index?: int): boolean--><!--Device-i18n-export function addPreferredLanguage(language: string, index?: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | Preferred language to add. |
| index | int | No | Position to which the preferred language is added. The default value is the length of the preferred language list. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the operation is successful, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// Add zh-CN to the preferred language list.
let language: string = 'zh-CN';
let index: number = 0;
let success: boolean = i18n.addPreferredLanguage(language, index);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// Add zh-CN to the preferred language list.
let language = 'zh-CN';
let index = 0;
try {
  i18n.System.addPreferredLanguage(language, index); // Add zh-CN to the first place in the preferred language list.
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.addPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

