# ShowParams

```TypeScript
declare class ShowParams
```

ShowParams可以用作用于显示UIAability的API的输入参数(例如，[showAbility()](arkts-ability-uiabilitycontext-c.md#showability-2))，用于指定目标UIAability的显示参数，包括但不限于窗口获得焦点其中启动了目标UIAability。

**起始版本：** 26.1.0

<!--Device-unnamed-declare class ShowParams--><!--Device-unnamed-declare class ShowParams-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { ShowParams } from '@kit.AbilityKit';
```

## windowShowParams

```TypeScript
windowShowParams: window.WindowShowParams
```

启动UIAbility界面参数说明。

**类型：** [window.WindowShowParams](../../apis-arkui/arkts-apis/arkts-arkui-window.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ShowParams-windowShowParams: window.WindowShowParams--><!--Device-ShowParams-windowShowParams: window.WindowShowParams-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
