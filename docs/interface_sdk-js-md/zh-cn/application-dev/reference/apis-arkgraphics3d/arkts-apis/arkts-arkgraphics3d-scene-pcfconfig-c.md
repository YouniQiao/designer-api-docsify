# PCFConfig

```TypeScript
export declare class PCFConfig extends SoftShadowConfig
```

PCF（Percentage Closer Filtering，百分比邻近过滤）软阴影配置类，继承自[SoftShadowConfig](arkts-arkgraphics3d-scene-softshadowconfig-c.md)。

**继承/实现关系：** PCFConfig extends [SoftShadowConfig](arkts-arkgraphics3d-scene-softshadowconfig-c.md)

**起始版本：** 26.0.0

<!--Device-unnamed-export declare class PCFConfig extends SoftShadowConfig--><!--Device-unnamed-export declare class PCFConfig extends SoftShadowConfig-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## shadowSampleCount

```TypeScript
get shadowSampleCount(): number | undefined
```

采样数量，决定了每个像素采样阴影图的次数，数量越多，阴影质量越高，但性能开销越大。默认值为16。取值范围：0 ~ 64。  
- 设置为0时，不进行PCF采样，无阴影效果。  
- 设置为负数时为无效赋值，本次设置不生效，属性保留当前值不变（例如传入-16，属性值和渲染效果仍保持设置前的状态）。  
- 设置大于64的值不会被拒绝，属性按实际传入值保存（例如传入65可设置成功），但渲染时按上限64计算，阴影效果与设置为64时一致。  
- 设置为undefined时，恢复默认值16进行渲染。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PCFConfig-get shadowSampleCount(): int | undefined--><!--Device-PCFConfig-get shadowSampleCount(): int | undefined-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

```TypeScript
set shadowSampleCount(value: number | undefined)
```

采样数量，决定了每个像素采样阴影图的次数，数量越多，阴影质量越高，但性能开销越大。默认值为16。取值范围：0 ~ 64。  
- 设置为0时，不进行PCF采样，无阴影效果。  
- 设置为负数时为无效赋值，本次设置不生效，属性保留当前值不变（例如传入-16，属性值和渲染效果仍保持设置前的状态）。  
- 设置大于64的值不会被拒绝，属性按实际传入值保存（例如传入65可设置成功），但渲染时按上限64计算，阴影效果与设置为64时一致。  
- 设置为undefined时，恢复默认值16进行渲染。

**类型：** number

**默认值：** 16

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PCFConfig-set shadowSampleCount(value: int | undefined)--><!--Device-PCFConfig-set shadowSampleCount(value: int | undefined)-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## shadowSampleRadius

```TypeScript
get shadowSampleRadius(): number | undefined
```

采样半径，决定了阴影边缘模糊的范围，半径越大，阴影边缘越柔和。采样半径过大会导致阴影过度模糊，失去阴影形状特征。默认值为5.0。取值范围：&gt;= 0。  
- 设置为0时，不进行PCF采样，无阴影效果。  
- 设置为负数时为无效赋值，本次设置不生效，属性保留当前值不变。  
- 设置为undefined时，恢复默认值5.0进行渲染。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PCFConfig-get shadowSampleRadius(): double | undefined--><!--Device-PCFConfig-get shadowSampleRadius(): double | undefined-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

```TypeScript
set shadowSampleRadius(value: number | undefined)
```

采样半径，决定了阴影边缘模糊的范围，半径越大，阴影边缘越柔和。采样半径过大会导致阴影过度模糊，失去阴影形状特征。默认值为5.0。取值范围：&gt;= 0。  
- 设置为0时，不进行PCF采样，无阴影效果。  
- 设置为负数时为无效赋值，本次设置不生效，属性保留当前值不变。  
- 设置为undefined时，恢复默认值5.0进行渲染。

**类型：** number

**默认值：** 5.0

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PCFConfig-set shadowSampleRadius(value: double | undefined)--><!--Device-PCFConfig-set shadowSampleRadius(value: double | undefined)-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D
