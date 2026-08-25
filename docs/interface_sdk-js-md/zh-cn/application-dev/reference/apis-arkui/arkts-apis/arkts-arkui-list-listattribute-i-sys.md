# ListAttribute

除支持通用属性和滚动组件通用属性外，还支持 以下属性：

> **说明：**&gt;
> List组件通用属性clip的默认值为true。

**继承/实现关系：** ListAttribute extends ScrollableCommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## chainAnimationOptions

```TypeScript
default chainAnimationOptions(value: ChainAnimationOptions | undefined): this
```

设置链式联动动效选项。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ChainAnimationOptions](arkts-arkui-list-chainanimationoptions-i-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
