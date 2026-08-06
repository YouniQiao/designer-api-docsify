# Magnifier

Provides the method for magnifier capabilities.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class Magnifier--><!--Device-unnamed-export declare class Magnifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bind

```TypeScript
bind(id: string): void
```

Bind magnifier to a component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Magnifier-bind(id: string): void--><!--Device-Magnifier-bind(id: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | component id. |

## show

```TypeScript
show(x: double, y: double): void
```

Set the position of the magnified content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Magnifier-show(x: double, y: double): void--><!--Device-Magnifier-show(x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | the x position of the magnified content relative to the component. The unit of x is vp. |
| y | double | Yes | the y position of the magnified content relative to the component. The unit of y is vp. |

## unbind

```TypeScript
unbind(): void
```

Unbind the magnifier from its associated component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Magnifier-unbind(): void--><!--Device-Magnifier-unbind(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

