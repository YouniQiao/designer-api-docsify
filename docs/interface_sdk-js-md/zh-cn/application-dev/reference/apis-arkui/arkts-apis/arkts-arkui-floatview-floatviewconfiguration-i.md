# FloatViewConfiguration

```TypeScript
interface FloatViewConfiguration
```

创建闪控窗控制器时需要提供的参数配置。

**起始版本：** 26.0.0

<!--Device-floatView-interface FloatViewConfiguration--><!--Device-floatView-interface FloatViewConfiguration-End-->

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { floatView } from '@kit.ArkUI';
```

## context

```TypeScript
context: BaseContext
```

表示上下文环境，用于创建闪控窗控制器时关联的应用主窗口。必须传入有效的UIAbilityContext实例。

**类型：** [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewConfiguration-context: BaseContext--><!--Device-FloatViewConfiguration-context: BaseContext-End-->

**系统能力：** SystemCapability.Window.SessionManager

## isConfirmOnClose

```TypeScript
isConfirmOnClose?: boolean
```

点击关闭按钮时是否需要用户确认。true表示点击关闭按钮时需要用户确认，否则不需要确认。默认值为false。

**类型：** boolean

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewConfiguration-isConfirmOnClose?: boolean--><!--Device-FloatViewConfiguration-isConfirmOnClose?: boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

## templateType

```TypeScript
templateType: FloatViewTemplateType
```

闪控窗的模板类型。

**类型：** [FloatViewTemplateType](arkts-arkui-floatview-floatviewtemplatetype-e.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatViewConfiguration-templateType: FloatViewTemplateType--><!--Device-FloatViewConfiguration-templateType: FloatViewTemplateType-End-->

**系统能力：** SystemCapability.Window.SessionManager
