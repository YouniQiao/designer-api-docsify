# InputMethodExtensionAbility

**起始版本：** 23

<!--Device-unnamed-declare class InputMethodExtensionAbility--><!--Device-unnamed-declare class InputMethodExtensionAbility-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { InputMethodExtensionAbility } from '@kit.IMEKit';
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionAbility-onCreate(want: Want): void--><!--Device-InputMethodExtensionAbility-onCreate(want: Want): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | 当前Extension相关的Want类型信息，包括Ability名称、bundle名称等。 |

**示例**

```TypeScript
import { InputMethodExtensionAbility, InputMethodAbility, KeyboardDelegate, PanelInfo, PanelType, PanelFlag, inputMethodEngine } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    console.info(`onCreate, want: ${want.abilityName}`);

    // 获取输入法能力对象
    let ability: InputMethodAbility = inputMethodEngine.getInputMethodAbility();

    // 获取键盘代理对象
    let keyboardDelegate: KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();

    // 创建面板
    let panelInfo: PanelInfo = {
      type: PanelType.SOFT_KEYBOARD,
      flag: PanelFlag.FLG_FIXED
    };
    ability.createPanel(this.context, panelInfo, (err, panel) => {
      if (err) {
        console.error(`Failed to create panel: ${err.code}`);
        return;
      }
      console.info('Succeeded in creating panel.');
    });

    // 订阅输入法绑定事件
    ability.on('inputStart', (kbController, inputClient) => {
      console.info('Input method bound to client.');
    });
  }
}
```

## onDestroy

```TypeScript
onDestroy(): void
```

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionAbility-onDestroy(): void--><!--Device-InputMethodExtensionAbility-onDestroy(): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例**

```TypeScript
import { InputMethodExtensionAbility } from '@kit.IMEKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onDestroy(): void {
    // 销毁面板、取消事件订阅等清理工作
    console.info('onDestroy');
  }
}
```

## context

```TypeScript
context: InputMethodExtensionContext
```

**类型：** [InputMethodExtensionContext](arkts-ime-inputmethodextensioncontext-c.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionAbility-context: InputMethodExtensionContext--><!--Device-InputMethodExtensionAbility-context: InputMethodExtensionContext-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

