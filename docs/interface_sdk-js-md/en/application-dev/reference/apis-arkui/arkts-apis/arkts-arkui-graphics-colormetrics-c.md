# ColorMetrics

用于混合颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ColorMetrics--><!--Device-unnamed-export declare class ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blendColor

```TypeScript
blendColor(overlayColor: ColorMetrics): ColorMetrics
```

在当前颜色的上方叠加上一层指定的颜色（overlayColor），并返回混合后的新颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-blendColor(overlayColor: ColorMetrics): ColorMetrics--><!--Device-ColorMetrics-blendColor(overlayColor: ColorMetrics): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| overlayColor | [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | Yes | 要叠加在上方的颜色对象。alpha属性决定叠加强度。1.0表示完全覆盖，0.0表示完全透明，混合结果为原色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | 新的颜色对象，其red、green、blue和alpha通道均为当前颜色与叠加颜色混合后的结果值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. The type of the input parameter is not ColorMetrics. |

## colorWithSpace

```TypeScript
static colorWithSpace(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics
```

使用colorSpace和rgba实例化ColorMetrics类。只有部分属性支持在display-p3 colorSpace中设置颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static colorWithSpace(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static colorWithSpace(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-colorspace-e.md) | Yes | 颜色空间，用于指定颜色的色彩空间。使用ColorSpace.DISPLAY_P3，需要对应窗口调用 [setWindowColorSpace](../../../reference/apis-arkui/arkts-apis-window-Window.md#setwindowcolorspace9-1)接口，将当前窗 口设置为广色域模式。 |
| red | double | Yes | 颜色的R分量（红色），值是0~1的浮动数值。 |
| green | double | Yes | 颜色的G分量（绿色），值是0~1的浮动数值。 |
| blue | double | Yes | 颜色的B分量（蓝色），值是0~1的浮动数值。 |
| alpha | double | No | 颜色的A分量（透明度），值是0.0~1.0的浮点数，默认值为1.0，不透明。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | ColorMetrics类的实例。 |

## numeric

```TypeScript
static numeric(value: int): ColorMetrics
```

使用颜色编号实例化ColorMetrics类

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static numeric(value: int): ColorMetrics--><!--Device-ColorMetrics-static numeric(value: int): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | HEX格式颜色。&lt;br/&gt;取值范围：支持rgb或者argb。 &lt;br&gt;取值限定为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | ColorMetrics 类的实例。 |

## resourceColor

```TypeScript
static resourceColor(color: ResourceColor): ColorMetrics
```

使用资源格式颜色实例化 ColorMetrics 类。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static resourceColor(color: ResourceColor): ColorMetrics--><!--Device-ColorMetrics-static resourceColor(color: ResourceColor): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes | 资源格式颜色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | ColorMetrics 类的实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 180003 | Failed to obtain the color resource. |
| 401 | Parameter error. Possible cause: 1. The type of the input color parameter is not ResourceColor. 2. The format of the input color string is not RGB or RGBA. |

## rgba

```TypeScript
static rgba(red: double, green: double, blue: double, alpha?: double): ColorMetrics
```

使用颜色rgb实例化ColorMetrics类

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static rgba(red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static rgba(red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| red | double | Yes | 颜色的R分量（红色），值是0~255的整数。 |
| green | double | Yes | 颜色的G分量（绿色），值是0~255的整数。 |
| blue | double | Yes | 颜色的B分量（蓝色），值是0~255的整数。 |
| alpha | double | No | 颜色的A分量（透明度），值是0.0~1.0的浮点数，默认值为1.0，不透明。&lt;br/&gt; **说明：** alpha小于0为全透明，大于1为不透明。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | ColorMetrics 类的实例。 |

## BLACK

```TypeScript
public static readonly BLACK: int
```

黑色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly BLACK: int--><!--Device-ColorMetrics-public static readonly BLACK: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BLUE

```TypeScript
public static readonly BLUE: int
```

蓝色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly BLUE: int--><!--Device-ColorMetrics-public static readonly BLUE: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BROWN

```TypeScript
public static readonly BROWN: int
```

棕色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly BROWN: int--><!--Device-ColorMetrics-public static readonly BROWN: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GRAY

```TypeScript
public static readonly GRAY: int
```

灰色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly GRAY: int--><!--Device-ColorMetrics-public static readonly GRAY: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GREEN

```TypeScript
public static readonly GREEN: int
```

绿色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly GREEN: int--><!--Device-ColorMetrics-public static readonly GREEN: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GREY

```TypeScript
public static readonly GREY: int
```

灰色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly GREY: int--><!--Device-ColorMetrics-public static readonly GREY: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ORANGE

```TypeScript
public static readonly ORANGE: int
```

橘色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly ORANGE: int--><!--Device-ColorMetrics-public static readonly ORANGE: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PINK

```TypeScript
public static readonly PINK: int
```

粉色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly PINK: int--><!--Device-ColorMetrics-public static readonly PINK: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RED

```TypeScript
public static readonly RED: int
```

红色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly RED: int--><!--Device-ColorMetrics-public static readonly RED: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TRANSPARENT

```TypeScript
public static readonly TRANSPARENT: string
```

透明度。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly TRANSPARENT: string--><!--Device-ColorMetrics-public static readonly TRANSPARENT: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WHITE

```TypeScript
public static readonly WHITE: int
```

白色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly WHITE: int--><!--Device-ColorMetrics-public static readonly WHITE: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## YELLOW

```TypeScript
public static readonly YELLOW: int
```

黄色。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly YELLOW: int--><!--Device-ColorMetrics-public static readonly YELLOW: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alpha

```TypeScript
get alpha(): int
```

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-get alpha(): int--><!--Device-ColorMetrics-get alpha(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blue

```TypeScript
get blue(): int
```

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-get blue(): int--><!--Device-ColorMetrics-get blue(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
get color(): string
```

获取ColorMetrics的颜色，返回的是rgba字符串的格式。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-get color(): string--><!--Device-ColorMetrics-get color(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## green

```TypeScript
get green(): int
```

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-get green(): int--><!--Device-ColorMetrics-get green(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## red

```TypeScript
get red(): int
```

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-get red(): int--><!--Device-ColorMetrics-get red(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

