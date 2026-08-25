# DynamicComponent（系统接口）

## DynamicComponent

```TypeScript
export declare function DynamicComponent(
    options: DynamicOptions
): DynamicComponentAttribute
```

创建DynamicComponent组件，用于显示Worker线程中运行的Abc UI。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DynamicOptions](arkts-arkui-dynamiccomponent-dynamicoptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DynamicComponentAttribute](arkts-arkui-dynamiccomponent-dynamiccomponentattribute-i-sys.md) |


## DynamicComponent

```TypeScript
export declare function DynamicComponent(
    style: CustomBuilderT<DynamicComponentAttribute>
): DynamicComponentAttribute
```

定义DynamicComponent组件。要求在组件属性设置开始时调用setDynamicComponentOptions， 在组件属性设置结束时 调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[DynamicComponentAttribute](arkts-arkui-dynamiccomponent-dynamiccomponentattribute-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DynamicComponentAttribute](arkts-arkui-dynamiccomponent-dynamiccomponentattribute-i-sys.md) |
