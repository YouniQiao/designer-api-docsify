# Component3D properties/events

**Inheritance/Implementation:** Component3DAttribute extends CommonMethod<Component3DAttribute>

**Since:** 12

<!--Device-unnamed-declare class Component3DAttribute--><!--Device-unnamed-declare class Component3DAttribute-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## Modules to Import

```TypeScript
```

## customRender

```TypeScript
customRender(uri: ResourceStr, selfRenderUpdate: boolean)
```

Set render pipeline of 3D scene render.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Component3DAttribute-customRender(uri: ResourceStr, selfRenderUpdate: boolean): Component3DAttribute--><!--Device-Component3DAttribute-customRender(uri: ResourceStr, selfRenderUpdate: boolean): Component3DAttribute-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |
| selfRenderUpdate | boolean | Yes |

## environment

```TypeScript
environment(uri: ResourceStr)
```

Load 3D model environment resource.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Component3DAttribute-environment(uri: ResourceStr): Component3DAttribute--><!--Device-Component3DAttribute-environment(uri: ResourceStr): Component3DAttribute-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

## renderHeight

```TypeScript
renderHeight(value: Dimension)
```

Set render height resolution.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Component3DAttribute-renderHeight(value: Dimension): Component3DAttribute--><!--Device-Component3DAttribute-renderHeight(value: Dimension): Component3DAttribute-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | Yes |

## renderWidth

```TypeScript
renderWidth(value: Dimension)
```

Set render width resolution.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Component3DAttribute-renderWidth(value: Dimension): Component3DAttribute--><!--Device-Component3DAttribute-renderWidth(value: Dimension): Component3DAttribute-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | Yes |

## shader

```TypeScript
shader(uri: ResourceStr)
```

Load shader uri.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Component3DAttribute-shader(uri: ResourceStr): Component3DAttribute--><!--Device-Component3DAttribute-shader(uri: ResourceStr): Component3DAttribute-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

## shaderImageTexture

```TypeScript
shaderImageTexture(uri: ResourceStr)
```

Load shader texture uri.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Component3DAttribute-shaderImageTexture(uri: ResourceStr): Component3DAttribute--><!--Device-Component3DAttribute-shaderImageTexture(uri: ResourceStr): Component3DAttribute-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

## shaderInputBuffer

```TypeScript
shaderInputBuffer(buffer: Array<number>)
```

Buffer input for shader animation

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Component3DAttribute-shaderInputBuffer(buffer: Array<number>): Component3DAttribute--><!--Device-Component3DAttribute-shaderInputBuffer(buffer: Array<number>): Component3DAttribute-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | Array & lt;number & gt; | Yes |
