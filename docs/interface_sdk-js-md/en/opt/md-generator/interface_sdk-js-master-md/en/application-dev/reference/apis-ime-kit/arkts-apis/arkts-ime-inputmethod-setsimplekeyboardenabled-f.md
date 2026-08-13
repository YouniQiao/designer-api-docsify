# setSimpleKeyboardEnabled

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## setSimpleKeyboardEnabled

```TypeScript
function setSimpleKeyboardEnabled(enable: boolean): void
```

Set simple keyboard mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-inputMethod-function setSimpleKeyboardEnabled(enable: boolean): void--><!--Device-inputMethod-function setSimpleKeyboardEnabled(enable: boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## Examples

```TypeScript
let enable: boolean = false;
  inputMethod.setSimpleKeyboardEnabled(enable);
```
