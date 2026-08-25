# UIExtensionComponent（系统接口）

## UIExtensionComponent

```TypeScript
export declare function UIExtensionComponent(
    want: Want, options?: UIExtensionOptions
): UIExtensionComponentAttribute
```

定义UIExtensionComponent组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [UIExtensionOptions](arkts-arkui-uiextensioncomponent-uiextensionoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md) |


## UIExtensionComponent

```TypeScript
export declare function UIExtensionComponent(
    style: CustomBuilderT<UIExtensionComponentAttribute>
): UIExtensionComponentAttribute
```

定义UIExtensionComponent组件。它要求在组件属性设置开始时调用setUIExtensionComponentOptions， 并在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md) |
