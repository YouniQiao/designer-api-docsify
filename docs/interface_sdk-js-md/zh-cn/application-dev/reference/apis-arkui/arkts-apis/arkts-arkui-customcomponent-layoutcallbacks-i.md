# LayoutCallbacks

Defining interface of LayoutCallbacks for custom component, when decorate with @Layoutable.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onPlaceChildren

```TypeScript
onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void {}
```

Custom component override this method to layout each of its sub components.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selfLayoutInfo | [GeometryInfo](../arkts-components/arkts-arkui-geometryinfo-i.md) | 是 |
| children | Array&lt;[Layoutable](../arkts-components/arkts-arkui-layoutable-i.md)&gt; | 是 |
| constraint | [ConstraintSizeOptions](arkts-arkui-constraintsizeoptions-i.md) | 是 |
