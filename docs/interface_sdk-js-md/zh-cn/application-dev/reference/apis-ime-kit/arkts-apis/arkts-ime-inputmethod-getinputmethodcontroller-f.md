# getInputMethodController

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getInputMethodController

```TypeScript
function getInputMethodController(): InputMethodController
```

获取客户端实例[InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md)。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [getController](arkts-ime-inputmethod-getcontroller-f.md)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getInputMethodController();
```
