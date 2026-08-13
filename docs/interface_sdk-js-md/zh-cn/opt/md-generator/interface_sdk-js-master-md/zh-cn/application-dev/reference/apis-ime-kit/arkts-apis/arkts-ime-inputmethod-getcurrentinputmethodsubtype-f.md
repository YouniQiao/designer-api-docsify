# getCurrentInputMethodSubtype

## getCurrentInputMethodSubtype

```TypeScript
function getCurrentInputMethodSubtype(): InputMethodSubtype
```

获取当前输入法的子类型。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputMethod-function getCurrentInputMethodSubtype(): InputMethodSubtype--><!--Device-inputMethod-function getCurrentInputMethodSubtype(): InputMethodSubtype-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md) |

## 示例

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';

let currentImeSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
```
