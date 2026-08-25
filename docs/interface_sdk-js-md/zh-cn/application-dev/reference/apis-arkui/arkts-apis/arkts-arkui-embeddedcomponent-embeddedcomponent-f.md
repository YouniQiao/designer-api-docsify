# EmbeddedComponent

## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    loader: Want, type?: EmbeddedType
): EmbeddedComponentAttribute
```

创建跨进程嵌入式组件，用于显示同包名或满足跨应用权限条件的EmbeddedUIExtensionAbility的UI。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| type | [EmbeddedType](arkts-arkui-embeddedtype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md) |


## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions
): EmbeddedComponentAttribute
```

创建跨进程嵌入式组件，用于显示同包名或满足跨应用权限条件的EmbeddedUIExtensionAbility的UI。相对于API version 12的接口，新增options参数用于传递构造参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| type | [EmbeddedType](arkts-arkui-embeddedtype-e.md) | 否 |
| options | [EmbeddedOptions](arkts-arkui-embeddedcomponent-embeddedoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md) |


## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    style: CustomBuilderT<EmbeddedComponentAttribute>
): EmbeddedComponentAttribute
```

定义EmbeddedComponent组件。需要在组件属性设置开始时调用setEmbeddedComponentOptions， 并在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md) |
