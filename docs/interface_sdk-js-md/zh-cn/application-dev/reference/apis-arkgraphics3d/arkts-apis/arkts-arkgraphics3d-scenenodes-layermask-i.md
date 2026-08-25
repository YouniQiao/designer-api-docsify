# LayerMask

用于定义节点的图层掩码。@interface LayerMask

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getEnabled

```TypeScript
getEnabled(index: number): boolean
```

获取指定图层下标图层掩码的使能状态。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setEnabled

```TypeScript
setEnabled(index: number, enabled: boolean): void
```

将特定下标的图层掩码使能。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| enabled | boolean | 是 |
