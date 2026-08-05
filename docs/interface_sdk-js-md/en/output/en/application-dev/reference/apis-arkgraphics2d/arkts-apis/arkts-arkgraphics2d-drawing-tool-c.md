# Tool

A utility class that provides only static methods to convert data structs defined in other modules and [common2D]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. > **NOTE** > > - The initial APIs of this class are supported since API version 15. > > - This module uses the physical pixel unit, px. > > - The module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-drawing-class Tool--><!--Device-drawing-class Tool-End-->

**System capability:** SystemCapability.Graphics.Drawing

## makeColorFromResourceColor

```TypeScript
static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color
```

Converts a color value of the **ResourceColor** type to a **common2D.Color** object.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color--><!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceColor | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Color value of the **ResourceColor** type. (All four types of inputs are supported. The following provides 13 example inputs.) The fourth type of [Resource]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ supports only the construction method **\_\_\_ESCAPED\_DOLLAR\_\_\_r('belonging.type.name')**. Ensure that the resource has been defined in the **main/resources/base/element** directory. (The types **color**, **string**, and **integer** are available for the belonging **app**, whereas only the type **color** is available for the belonging **sys**.) |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | **Common2D.Color** object. If the conversion fails, a null pointer is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. |

## makeColorFromResourceColor

```TypeScript
static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined
```

Converts a color value of the ResourceColor type to a common2D.Color object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined--><!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceColor | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Color value of the ResourceColor type.(All four types of inputs are supported. The following provides 13 example inputs.)The fourth type of Resource supports only the construction method \_\_\_ESCAPED\_DOLLAR\_\_\_r('belonging.type.name').Ensure that the resource has been defined in the main/resources/base/element directory.(The types color, string, and integer are available for the belonging app,whereas only the type color is available for the belonging sys.) |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | Returns a 32-bit (ARGB) variable that describes the color. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. |

