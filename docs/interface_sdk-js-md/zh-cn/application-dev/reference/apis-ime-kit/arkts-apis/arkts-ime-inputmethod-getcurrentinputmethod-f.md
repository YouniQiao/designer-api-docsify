# getCurrentInputMethod

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## getCurrentInputMethod

```TypeScript
function getCurrentInputMethod(): InputMethodProperty
```

@brief 使用同步方法获取当前输入法。 <br> <br>含义/功能：获取当前正在使用的输入法属性信息。 <br> <br>使用场景：当应用需要知道当前活跃的输入法是哪个（如判断输入法名称、获取输入法id用于后续切换操作）时使用。 <br> <br>使用后效果：返回当前输入法的InputMethodProperty对象。

**起始版本：** 23

<!--Device-inputMethod-function getCurrentInputMethod(): InputMethodProperty--><!--Device-inputMethod-function getCurrentInputMethod(): InputMethodProperty-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | 返回当前输入法属性对象。 |

**示例**

```TypeScript
let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod(100);
  console.info('Succeeded in getting current input method, name: ' + currentIme.name + ', id: ' + currentIme.id);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to getCurrentInputMethod. Code: ${error.code}, message: ${error.message}`);
}
```

