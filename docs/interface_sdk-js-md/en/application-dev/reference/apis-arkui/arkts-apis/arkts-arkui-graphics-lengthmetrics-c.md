# LengthMetrics

用于设置长度属性，当长度单位为PERCENT时，值为1表示100%。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class LengthMetrics--><!--Device-unnamed-export declare class LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: double, unit?:LengthUnit)
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-constructor(value: double, unit?:LengthUnit)--><!--Device-LengthMetrics-constructor(value: double, unit?:LengthUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 长度属性的值。&lt;br/&gt;取值范围：[0, +∞) |
| unit | [LengthUnit](arkts-arkui-graphics-lengthunit-e.md) | No | 长度属性的单位。 |

## fp

```TypeScript
static fp(value: double): LengthMetrics
```

用fp单位初始化一个lengthMetrics。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static fp(value: double): LengthMetrics--><!--Device-LengthMetrics-static fp(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 长度属性的值。&lt;br/&gt;。 &lt;br&gt;取值范围：(-∞, +∞)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | LengthMetrics 类的实例。 |

## lpx

```TypeScript
static lpx(value: double): LengthMetrics
```

用lpx单位初始化一个lengthMetrics。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static lpx(value: double): LengthMetrics--><!--Device-LengthMetrics-static lpx(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 长度属性的值。&lt;br/&gt;。 &lt;br&gt;取值范围：(-∞, +∞)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | LengthMetrics 类的实例。 |

## percent

```TypeScript
static percent(value: double): LengthMetrics
```

初始化一个带有百分比单位的lengthMetrics。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static percent(value: double): LengthMetrics--><!--Device-LengthMetrics-static percent(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 长度属性的值。&lt;br/&gt;。 &lt;br&gt;取值范围：[0, 1]。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | LengthMetrics 类的实例。 |

## px

```TypeScript
static px(value: double): LengthMetrics
```

初始化一个带有px单位的lengthMetrics。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static px(value: double): LengthMetrics--><!--Device-LengthMetrics-static px(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 长度属性的值。&lt;br/&gt;。 &lt;br&gt;取值范围：(-∞, +∞)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | LengthMetrics 类的实例。 |

## resource

```TypeScript
static resource(value: Resource): LengthMetrics
```

用于生成Resource类型资源的长度属性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static resource(value: Resource): LengthMetrics--><!--Device-LengthMetrics-static resource(value: Resource): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes | 长度属性的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | LengthMetrics 类的实例。 |

## vp

```TypeScript
static vp(value: double): LengthMetrics
```

初始化一个带有vp单位的lengthMetrics。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static vp(value: double): LengthMetrics--><!--Device-LengthMetrics-static vp(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 长度属性的值。&lt;br/&gt;。 &lt;br&gt;取值范围：(-∞, +∞)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | LengthMetrics 类的实例。 |

## unit

```TypeScript
public unit: LengthUnit
```

长度属性的单位，默认为VP。

**Type:** [LengthUnit](arkts-arkui-graphics-lengthunit-e.md)

**Default:** VP

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-public unit: LengthUnit--><!--Device-LengthMetrics-public unit: LengthUnit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
public value: double
```

长度属性的值。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-public value: double--><!--Device-LengthMetrics-public value: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

