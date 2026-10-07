# RecoverDisposedRule（系统接口）

```TypeScript
export interface RecoverDisposedRule
```

描述应用程序恢复已处理的规则。

**起始版本：** 26.2.0

<!--Device-appControl-export interface RecoverDisposedRule--><!--Device-appControl-export interface RecoverDisposedRule-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { appControl } from '@kit.AbilityKit';
```

## priority

```TypeScript
priority: number
```

下发规则的优先级，用于对规则列表的查询结果进行排序。整数形式。数值越小优先级越高。取值限定为整数。

**类型：** number

**起始版本：** 26.2.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecoverDisposedRule-priority: int--><!--Device-RecoverDisposedRule-priority: int-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

## recoverComponentType

```TypeScript
recoverComponentType: RecoverComponentType
```

监听时启动的能力类型。

**类型：** [RecoverComponentType](arkts-ability-appcontrol-recovercomponenttype-e-sys.md)

**起始版本：** 26.2.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecoverDisposedRule-recoverComponentType: RecoverComponentType--><!--Device-RecoverDisposedRule-recoverComponentType: RecoverComponentType-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

## want

```TypeScript
want: Want
```

当应用程序被释放时显示的组件。

**类型：** [Want](arkts-ability-app-ability-want-want-c.md)

**起始版本：** 26.2.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecoverDisposedRule-want: Want--><!--Device-RecoverDisposedRule-want: Want-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。
