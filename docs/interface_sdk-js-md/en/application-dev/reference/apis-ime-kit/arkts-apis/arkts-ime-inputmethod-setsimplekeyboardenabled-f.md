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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethod-function setSimpleKeyboardEnabled(enable: boolean): void--><!--Device-inputMethod-function setSimpleKeyboardEnabled(enable: boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | indicates enable simple keyboard or not. |

## Examples

```TypeScript
let enable: boolean = false;
  inputMethod.setSimpleKeyboardEnabled(enable);
```

