# getSetting

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## getSetting

```TypeScript
function getSetting(): InputMethodSetting
```

**起始版本：** 23

<!--Device-inputMethod-function getSetting(): InputMethodSetting--><!--Device-inputMethod-function getSetting(): InputMethodSetting-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) | 返回当前客户端设置实例。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800007](../errorcode-inputmethod-framework.md#12800007-输入法设置器异常) | input method setter error. Possible cause: create InputMethodSetting object failed. |

**示例**

```TypeScript
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
```

