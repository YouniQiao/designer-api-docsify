# getController

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## getController

```TypeScript
function getController(): InputMethodController
```

**起始版本：** 23

<!--Device-inputMethod-function getController(): InputMethodController--><!--Device-inputMethod-function getController(): InputMethodController-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) | 返回当前客户端实例。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) | input method controller error. Possible cause: create InputMethodController object failed. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
```

