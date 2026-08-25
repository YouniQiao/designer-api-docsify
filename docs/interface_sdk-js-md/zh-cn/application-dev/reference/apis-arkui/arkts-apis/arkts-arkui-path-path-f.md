# Path

## Path

```TypeScript
export declare function Path(
    options?: PathOptions
): PathAttribute
```

路径绘制组件，根据绘制路径生成封闭的自定义形状。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PathOptions](arkts-arkui-path-pathoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) |


## Path

```TypeScript
export declare function Path(
    style: CustomBuilderT<PathAttribute>,
): PathAttribute
```

Defines Path Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[PathAttribute](arkts-arkui-path-pathattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) |
