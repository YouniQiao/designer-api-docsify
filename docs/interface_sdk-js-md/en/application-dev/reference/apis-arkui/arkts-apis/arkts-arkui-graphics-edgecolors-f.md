# edgeColors

## edgeColors

```TypeScript
export declare function edgeColors(all: int): NodeEdges<int>
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function edgeColors(all: int): NodeEdges<int>--><!--Device-unnamed-export declare function edgeColors(all: int): NodeEdges<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| all | int | Yes | 边框颜色，ARGB格式，示例：0xffff00ff。&lt;br/&gt;取值范围：[0, 0xffffffff] |

**Return value:**

| Type | Description |
| --- | --- |
| [NodeEdges](arkts-arkui-graphics-nodeedges-i.md)&lt;int&gt; | 边框颜色均设置为传入值的边框颜色对象。 |

