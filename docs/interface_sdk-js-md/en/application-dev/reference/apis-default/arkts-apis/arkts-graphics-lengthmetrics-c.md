# LengthMetrics

Defines the Length Metrics.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class LengthMetrics--><!--Device-unnamed-export declare class LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoRefresh

```TypeScript
autoRefresh(value: boolean): LengthMetrics
```

Sets automatic refresh for the LengthMetrics object. When enabled, the length value of the object created by LengthMetrics.resource() is automatically updated when the system configuration changes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-autoRefresh(value: boolean): LengthMetrics--><!--Device-LengthMetrics-autoRefresh(value: boolean): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | whether to automatically update the length value when the system configuration changes. <br>If set to true, the length value of the object created by LengthMetrics.resource() is automatically updated when the system configuration changes. If set to false, the length value of the object created by LengthMetrics.resource() is automatically updated when the system configuration changes. The default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Returns the LengthMetrics object for chaining. |

## constructor

```TypeScript
constructor(value: double, unit?:LengthUnit)
```

Constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-constructor(value: double, unit?:LengthUnit)--><!--Device-LengthMetrics-constructor(value: double, unit?:LengthUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The value of length. |
| unit | [LengthUnit](arkts-graphics-lengthunit-e.md) | No | The length unit. |

## fp

```TypeScript
static fp(value: double): LengthMetrics
```

Init a lengthMetrics with fp unit.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static fp(value: double): LengthMetrics--><!--Device-LengthMetrics-static fp(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The value of the length metrics. |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Returns the lengthMetrics object with unit fp. |

## lpx

```TypeScript
static lpx(value: double): LengthMetrics
```

Init a lengthMetrics with lpx unit.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static lpx(value: double): LengthMetrics--><!--Device-LengthMetrics-static lpx(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The value of the length metrics. |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Returns the lengthMetrics object with unit lpx. |

## percent

```TypeScript
static percent(value: double): LengthMetrics
```

Init a lengthMetrics with percent unit.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static percent(value: double): LengthMetrics--><!--Device-LengthMetrics-static percent(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The value of the length metrics. |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Returns the lengthMetrics object with unit percent. |

## px

```TypeScript
static px(value: double): LengthMetrics
```

Init a lengthMetrics with px unit.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static px(value: double): LengthMetrics--><!--Device-LengthMetrics-static px(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The value of the length metrics. |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Returns the lengthMetrics object with unit px. |

## resource

```TypeScript
static resource(value: Resource): LengthMetrics
```

Init a lengthMetrics with Resource unit.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static resource(value: Resource): LengthMetrics--><!--Device-LengthMetrics-static resource(value: Resource): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes | The value of the length metrics. |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Returns the lengthMetrics object with unit Resource. |

## vp

```TypeScript
static vp(value: double): LengthMetrics
```

Init a lengthMetrics with vp unit.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-static vp(value: double): LengthMetrics--><!--Device-LengthMetrics-static vp(value: double): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The value of the length metrics. |

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Returns the lengthMetrics object with unit vp. |

## unit

```TypeScript
public unit: LengthUnit
```

The unit of the LengthMetrics. The default value is VP.

**Type:** [LengthUnit](arkts-graphics-lengthunit-e.md)

**Default:** VP

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-public unit: LengthUnit--><!--Device-LengthMetrics-public unit: LengthUnit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
public value: double
```

The value of the LengthMetrics.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthMetrics-public value: double--><!--Device-LengthMetrics-public value: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

