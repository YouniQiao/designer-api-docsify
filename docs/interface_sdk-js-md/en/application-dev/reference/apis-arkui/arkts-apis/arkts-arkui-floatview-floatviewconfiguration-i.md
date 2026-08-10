# FloatViewConfiguration

创建标准悬浮窗控制器时需要提供的参数配置。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-floatView-interface FloatViewConfiguration--><!--Device-floatView-interface FloatViewConfiguration-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## context

```TypeScript
context: BaseContext
```

表示上下文环境。

**Type:** [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewConfiguration-context: BaseContext--><!--Device-FloatViewConfiguration-context: BaseContext-End-->

**System capability:** SystemCapability.Window.SessionManager

## isConfirmOnClose

```TypeScript
isConfirmOnClose?: boolean
```

控制关闭窗口时是否弹出确认对话框.如果为 true，则点击关闭按钮时需要用户确认；如果为 false，则不需要确认，直接关闭。默认值： 默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewConfiguration-isConfirmOnClose?: boolean--><!--Device-FloatViewConfiguration-isConfirmOnClose?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## templateType

```TypeScript
templateType: FloatViewTemplateType
```

标准悬浮窗的模板类型。

**Type:** [FloatViewTemplateType](arkts-arkui-floatview-floatviewtemplatetype-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewConfiguration-templateType: FloatViewTemplateType--><!--Device-FloatViewConfiguration-templateType: FloatViewTemplateType-End-->

**System capability:** SystemCapability.Window.SessionManager

