# FloatingBallConfiguration

```TypeScript
interface FloatingBallConfiguration
```

创建闪控球控制器时需要提供的参数配置。

**起始版本：** 20

<!--Device-floatingBall-interface FloatingBallConfiguration--><!--Device-floatingBall-interface FloatingBallConfiguration-End-->

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { floatingBall } from '@kit.ArkUI';
```

## context

```TypeScript
context: BaseContext
```

表示上下文环境，用于创建闪控球控制器时关联的应用主窗口。该参数不能为空，通常传入UIAbilityContext对象。

**类型：** [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md)

**起始版本：** 20

<!--Device-FloatingBallConfiguration-context: BaseContext--><!--Device-FloatingBallConfiguration-context: BaseContext-End-->

**系统能力：** SystemCapability.Window.SessionManager
