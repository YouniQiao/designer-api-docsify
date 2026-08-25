# SecurityUIExtensionComponent（系统接口）

## SecurityUIExtensionComponent

```TypeScript
export declare function SecurityUIExtensionComponent(
    want: Want, options?: SecurityUIExtensionOptions, 
    content_?: CustomBuilder,
): SecurityUIExtensionComponentAttribute
```

创建SecurityUIExtensionComponent组件，用于嵌入显示远程UIExtensionAbility提供的UI。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [SecurityUIExtensionOptions](arkts-arkui-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md) | 否 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md) |


## SecurityUIExtensionComponent

```TypeScript
export declare function SecurityUIExtensionComponent(
    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,
    content_?: CustomBuilder,
): SecurityUIExtensionComponentAttribute
```

定义SecurityUIExtensionComponent组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md)&gt; | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md) |
