# Component3DAttribute

Component3DAttribute属性接口。@extends CommonMethod @interface Component3DAttribute

**继承/实现关系：** Component3DAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<Component3DAttribute>
      | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修改器

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md) |

## customRender

```TypeScript
default customRender(uri: ResourceStr | undefined, selfRenderUpdate: boolean | undefined): this
```

设置3D场景渲染的渲染管线。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |
| selfRenderUpdate | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md) |

## environment

```TypeScript
default environment(uri: ResourceStr | undefined): this
```

加载3D模型环境资源。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md) |

## renderHeight

```TypeScript
default renderHeight(value: Dimension | undefined): this
```

设置渲染高度分辨率。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md) |

## renderWidth

```TypeScript
default renderWidth(value: Dimension | undefined): this
```

设置渲染宽度分辨率。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md) |

## shader

```TypeScript
default shader(uri: ResourceStr | undefined): this
```

加载着色器URI。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md) |

## shaderImageTexture

```TypeScript
default shaderImageTexture(uri: ResourceStr | undefined): this
```

加载着色器纹理URI。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md) |

## shaderInputBuffer

```TypeScript
default shaderInputBuffer(buffer: Array<double> | undefined): this
```

着色器动画的缓冲区输入

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | Array & lt;double & gt; \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [Component3DAttribute](arkts-arkui-component3d-component3dattribute-i.md) |
