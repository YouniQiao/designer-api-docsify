# setSimpleKeyboardEnabled

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## setSimpleKeyboardEnabled

```TypeScript
function setSimpleKeyboardEnabled(enable: boolean): void
```

编辑框应用设置简单键盘标志。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-inputMethod-function setSimpleKeyboardEnabled(enable: boolean): void--><!--Device-inputMethod-function setSimpleKeyboardEnabled(enable: boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 简单键盘是否使能标志，true标识简单键盘使能，false标识简单键盘去使能。&lt;br/&gt; 原生编辑框组件在下一次点击获焦时生效；自绘控件在下一次调用 [attach](arkts-ime-inputmethod-inputmethodcontroller-i.md#attach) 绑定输入法时生效。 |

## Examples

```TypeScript
let enable: boolean = false;
  inputMethod.setSimpleKeyboardEnabled(enable);
```

