# AttributeUpdater

为AttributeModifier的实现类，开发者需要自定义class继承AttributeUpdater。

其中C代表组件的构造函数类型，比如Text组件的TextInterface，Image组件的ImageInterface等，仅在使用updateConstructorParams时才需要传递C类型。

**继承/实现关系：** AttributeUpdater implements AttributeModifier<T>

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class AttributeUpdater--><!--Device-unnamed-export declare class AttributeUpdater-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initializeModifier

```TypeScript
initializeModifier(instance: T): void
```

AttributeUpdater首次设置给组件时提供的样式。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AttributeUpdater-initializeModifier(instance: T): void--><!--Device-AttributeUpdater-initializeModifier(instance: T): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 |  |

## onComponentChanged

```TypeScript
onComponentChanged(component: T): void
```

绑定相同的自定义的Modifier对象，组件发生切换时，通过该接口通知到应用。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AttributeUpdater-onComponentChanged(component: T): void--><!--Device-AttributeUpdater-onComponentChanged(component: T): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| component | T | 是 |  |

