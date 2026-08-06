# RectShape

Defines a rect drawing class.

**Inheritance/Implementation:** RectShape extends [BaseShape](arkts-arkui-arkui-shape-baseshape-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RectShape extends BaseShape--><!--Device-unnamed-export declare class RectShape extends BaseShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: RectShapeOptions | RoundRectShapeOptions)
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)--><!--Device-RectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| RoundRectShapeOptions | No |  |

## radius

```TypeScript
radius(radius: double | string | Array<double | string>): this
```

Sets the corner radius for RectShape.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShape-radius(radius: double | string | Array<double | string>): this--><!--Device-RectShape-radius(radius: double | string | Array<double | string>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | double \| string \| Array&lt;double \| string&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radiusHeight

```TypeScript
radiusHeight(rHeight: double | string): this
```

Sets the height of the corner radius for RectShape.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShape-radiusHeight(rHeight: double | string): this--><!--Device-RectShape-radiusHeight(rHeight: double | string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rHeight | double \| string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radiusWidth

```TypeScript
radiusWidth(rWidth: double | string): this
```

Sets the width of the corner radius for RectShape.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShape-radiusWidth(rWidth: double | string): this--><!--Device-RectShape-radiusWidth(rWidth: double | string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rWidth | double \| string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

